from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pattern = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Rule {self.pattern}>'
