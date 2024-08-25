from flask import Flask,render_template,jsonify
app=Flask(__name__)

JOBS=[
    {
        'id':1,
        'title':'Data analyst',
        'salary': '10,00,000',
        'location': 'BBSR'
    },
    {
        'id':2,
        'title':'ML',
        'salary': '12,00,000',
        'location': 'BBSR'
    },
    {
        'id':3,
        'title':'Frontend',
        'salary': '15,00,000',
        'location': 'BLR'
    },
    {
        'id':4,
        'title':'Backend',
        'salary': '20,00,000',
        'location': 'Delhi'
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS,company_name='🐼')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

print(__name__)
if __name__=="__main__":
    print("I m inside if now")
    app.run(host='0.0.0.0',debug=True)