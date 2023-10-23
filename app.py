from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS =[
    {
      'id':1,
      'title':'Data Analyst',
      'location':'Bengaluru,India',
      'salary':'$50,000',

    },
    {
  'id':2,
  'title':'Data Scientist',
  'location':'Delhi,India',
  'salary':'$70,000',
    },
    {
    'id':3,
    'title':'FrontEnd Engineer',
    'location':'Remote',
    'salary':'$70,000',
    },
    {
    'id':4,
    'title':'BackEnd Engineer',
    'location':'San Francisco',
    'salary':'$70,000',
     }
]
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
@app.route("/")
def hello_world():
  return render_template('home.html', jobs= JOBS )

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)