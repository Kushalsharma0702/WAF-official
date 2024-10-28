from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import logging
import re

# Initialize Flask and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules.db'
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(filename='blocked_requests.log', level=logging.INFO)

# Define the Rule model
class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pattern = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Rule {self.pattern}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Function to check requests against rules
def check_request(request):
    rules = Rule.query.all()
    for rule in rules:
        if re.search(rule.pattern, request.data.decode('utf-8'), re.DOTALL):
            return True
    return False

@app.before_request
def filter_requests():
    if check_request(request):
        app.logger.warning(f'Blocked request: {request.method} {request.url} - {request.data}')
        return jsonify({"error": "Request blocked"}), 403

@app.route('/')
def index():
    return render_template('index.html')  # Ensure you have an index.html file

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    success_message = None
    error_message = None

    if request.method == 'POST':
        new_rule = request.form.get('new_rule')
        if new_rule:
            try:
                rule = Rule(pattern=new_rule)
                db.session.add(rule)
                db.session.commit()
                success_message = "Rule added successfully!"
            except Exception as e:
                error_message = "Failed to add rule. Please ensure it is valid."

    rules = Rule.query.all()
    return render_template('admin.html', rules=rules, success_message=success_message, error_message=error_message)

@app.route('/delete_rule/<int:rule_id>', methods=['POST'])
def delete_rule(rule_id):
    rule = Rule.query.get(rule_id)
    if rule:
        db.session.delete(rule)
        db.session.commit()
        return redirect(url_for('admin'))
    return jsonify({"error": "Rule not found"}), 404

@app.route('/some_endpoint', methods=['POST'])
def some_endpoint():
    return "Request received!"

@app.route('/test', methods=['POST'])
def test():
    return "Test endpoint received the request!"

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
