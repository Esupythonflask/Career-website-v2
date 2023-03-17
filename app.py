from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
{

'id': 1,
'title': 'Data Analyst',
  'location': 'Addis Ababa, Ethiopia',
  'Salary': 'ETB. 225,000' 
},
  {

'id': 4,
'title': 'Data Scientist',
  'location': 'Virginia,United Sates',
  'Salary': ' $125,000' 
},
  {
  'id': 4,
'title': 'Frontend Engineer',
  'location': 'Gondar, Ethiopia',
  'Salary': 'ETB. 120,000' 
},
  {
'id': 3,
'title': 'Backend Engineer',
  'location': 'Bahirdar, Ethiopia',
  'Salary': 'ETB. 155,000' 
},
  {
'id': 5,
'title': 'Quality Assurance Tester',
  'location': 'London, United Kingdom',
  'Salary': '£67,000' 
} 
  
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name ='Esubalew')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

if __name__ == '__main__':
  app.run(host ='0.0.0.0', debug =True)  