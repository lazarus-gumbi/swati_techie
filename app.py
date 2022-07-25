from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.sqlite3'
db = SQLAlchemy(app)

class Blog(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	topic = db.Column(db.String(500),unique=False,nullable=False)
	content = db.Column(db.String(1000),unique=False,nullable=False)
	image_link = db.Column(db.String(200),unique=False,nullable=False)
	last_update = db.Column(db.DateTime,default=db.func.current_timestamp(),onupdate=db.func.current_timestamp(),unique=False,nullable=False)

	# def __repr__(self):
	# 	return f"{self.id} - {self.topic} - {self.content} - {self.image_link} - {self.last_update}"

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/create_post')
def create_post():
	
	return render_template('post.html')

if __name__ == '__main__':
	app.run(debug=True)
    
