import re

# Example of valid patterns for SQL injection and XSS
VALID_PATTERNS = [
    r"'.*;--",                  # SQL injection example
    r"<script.*?>.*?</script>", # XSS example
    r"(?i)union.*select",       # SQL union select
    r"(?i)drop.*table"          # SQL drop table
]

def is_valid_rule(rule):
    # Check if the rule matches any of the valid patterns
    for pattern in VALID_PATTERNS:
        if re.search(pattern, rule):
            return True
    return False

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    success_message = None
    error_message = None

    if request.method == 'POST':
        new_rule = request.form.get('new_rule')
        if new_rule:
            if is_valid_rule(new_rule):
                try:
                    rule = Rule(pattern=new_rule)
                    db.session.add(rule)
                    db.session.commit()
                    success_message = "Rule added successfully!"
                    return redirect(url_for('admin'))
                except Exception:
                    error_message = "Failed to add rule. Please try again."
            else:
                error_message = "Invalid rule format. Please enter a valid security rule."

    rules = Rule.query.all()
    return render_template('admin.html', rules=rules, success_message=success_message, error_message=error_message)
