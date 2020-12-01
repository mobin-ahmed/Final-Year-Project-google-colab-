# import numpy as np
from flask import Flask,render_template,request,jsonify
import json

# import sys
# import time

# from autokiddobot import AutoKiddobot
# import matplotlib.pyplot as plt

app=Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/saveData', methods=["GET","POST"])
def save():
    if request.method=="POST":
        # print('data received. test')
        d=request.form
        name=d['name']
        # print(name)
        data=d.to_dict(flat=False)
        # print(data)
        x=data['x'][0]
        y=data['y'][0]

        # print('data1=', data['x'][0])
        # print('data2=', data['y'][0])
        filename="textfilesDraw/"+str(name)+".txt"
        # filename="kk.txt"
        file=open(filename,"w")
        for i in range(1,len(x)-1):
            # print(i)
            file.write(str(x[i]))
        file.write("\n")
        for i in range(1,len(y)-1):
            # print(i)
            file.write(str(y[i]))
        file.close()




        # file=open(filename,"r")

        # a1=file.readline()
        # f1=a1.split(',')
        # x=[]
        # for i in range(len(f1)):
        #     x.append(int(f1[i]))
        # a2=file.readline()
        # f2=a2.split(',')
        # y=[]
        # for i in range(len(f2)):
        #     y.append(int(f2[i]))
        # plt.scatter(x,y)
                
        return "data saved successfully"

if __name__=="__main__":
    app.run(host='0.0.0.0')

#host='0.0.0.0'
#debug = True