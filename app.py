import numpy as np
from flask import Flask, request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model_pickle.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('newhome.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    data1 = request.form.get('rating')
    data2 = request.form.get("role1")
    data3 = request.form.get("role2")
    data4 = request.form.get("role3")
    data5 = request.form.get('skill1')
    data6 = request.form.get('skill2')
    data7 = request.form.get('skill3')
    data8 = request.form.get('skill4')
    
    print(data2,data3,data4)
    
    if(data2=="1"):
        data2=1
        data3=0
        data4=0
     
    
    elif(data3=="1"):
        data2=0
        data3=1
        data4=0

    elif(data4=="1"):
        data2=0
        data3=0
        data4=1
    
    
    count=0
    for x in range(4):
        if(data5=="python_job"):
            count=1
        if(data6=="sql_job"):
            count=2
        if(data7=="tableau_job"):
            count=3
        if(data8=="aws_job"):
            count=4
    
    if(count==1):
        data5=1
        data6=0
        data7=0
        data8=0
    
    if(count==2):
        data5=1
        data6=1
        data7=0
        data8=0

    if(count==3):
        data5=1
        data6=1
        data7=1
        data8=0

    if(count==4):
        data5=1
        data6=1
        data7=1
        data8=1


    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8]])
    #arr = np.array([[3, 0, 0, 1, 1, 1, 0, 1]])
    pred = int(model.predict(arr))
    print(arr)
    return render_template('after.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)   
