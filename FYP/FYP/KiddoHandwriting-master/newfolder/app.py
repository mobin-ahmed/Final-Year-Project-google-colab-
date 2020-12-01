from flask import Flask, render_template, request
import numpy as np
import os
from flask import Response
import json
app = Flask(__name__,)

@app.route('/')
def draw():
   return render_template('draw.html')
  
def shape(result):
	f=open(result.get("name")+'.txt', 'a+')
	a="xcor"
	f.writelines(result['xcor'])
	# f.writelines(',')
	# f.writelines(result['ycor'])
	f.writelines('\n')
	f.close()

	return Response(json.dumps(True), mimetype='application/json')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      #print(result['Name'])
      return shape(result)



# @app.route('/shape',methods = ['POST', 'GET'])
# def shape():
# 	with open ('sore_o.txt') as file:
# 		lines=file.readlines()
# 		arr=np.array(lines)
# 		n=len(arr)

# 		data2=[]
# 		for item in arr:
# 			item=item.strip()
# 			num=item.split(',')
		    
# 			data2.append(num)
# 		data2=np.array(data2)
# 		r=[]
# 		for i in data2:
# 			e=(len(i))
# 			r.append(e)
# 		r=np.array(r)
# 		print(r)
# 		t=min(r)
# 		f=int(t/2)

# 		def resize(a,b):
# 			s=a.shape[0]
# 			z=b.shape[0]
# 			c=s-f
# 			index= np.random.choice(s, c, replace=False) 
# 			index=np.array(index)

# 			d1=[]
# 			d2=[]
# 			for i in range(s):
# 				if i not in index:
# 					item=float(a[i])
# 					d1.append(item)
		            
# 			for j in range(z):
# 				if j not in index:
# 					item=float(b[j])
# 					d2.append(item)
	  
	                
# 			d1=np.array(d1)
# 			d2=np.array(d2)

# 			return d1,d2

# 		def shifting(s):
# 			b=[]
# 			for i in range(len(s)):
# 				for j in range(len(s[i])):
# 					m=max(s[i])
# 					n=min(s[i])
# 					r=m+n
# 					t=(m+n)/2
		        
# 			for f in range(len(s)):
# 				g=s[f]-t
# 				b.append(g)
		            
# 			b=np.array(b)
# 			d=b.reshape(-1)
# 			return d

# 		def split_list(a_list):
# 			half = len(a_list)//2
# 			return a_list[:half], a_list[half:]


# 		data=[]
# 		v=[]
# 		for i in arr:
# 			e=i.strip().split(',')
# 			p,q=split_list(e)
# 			p=np.array(p)
# 			q=np.array(q)
# 			r=resize(p,q)
# 			r=np.array(r)
# 			s=shifting(r)
# 			data.append(s)

# 		avg=np.mean(data,axis=0)
# 		avg=np.array(avg)

# 		trainset=data-avg
# 		trainset.shape
# 		def covMatrix(matrix,mean):
		    
# 			covM=np.dot(trainset.T,trainset)
# 			covM=covM/(len(trainset)-1)	
# 			return covM

# 		cov=covMatrix(data,avg)

# 		def eigenV(cm):
# 			ne,EV=np.linalg.eig(cm)
# 			EV=EV[::-1]
# 			return EV

# 		EV=eigenV(cov)
# 		pc=[]
# 		for x in  trainset:
# 			newx=[]
# 			for i in range(t):
# 				npc=np.dot(EV[i],x)
# 				newx.append(npc)
# 			pc.append(newx)
# 		pc=np.array(pc)

# 		def drawPCA(cont1,con2,con3):
# 			pc1=EV[:,0]
# 			pc2=EV[:,1]
# 			pc3=EV[:,2]
# 			nsp=avg+pc1*cont1+pc2*con2+pc3*con3

# 			return nsp


# 		gen_shape=drawPCA(0.4,1.6,3.8)
# 		x=gen_shape[:f]
# 		y=gen_shape[f:]
# 		x=np.array(x)
# 		y=np.array(y)
		
# 		nmin=min(gen_shape)
# 		print(nmin)
# 		newy=[]
# 		for i in range(len(y)):
# 			if(y[i]>0):
# 				ny=y[i]
# 			else:
# 				ny=y[i]-nmin
		        
# 			newy.append(ny)
# 		newy=np.array(newy)
# 		print(newy)	

# 		a=np.concatenate((x,newy),axis=0)

# 		file = open('C:\\Users\\L E N O V O\\Desktop\\Flask\\gen.txt', 'a+')
# 		rd=''
# 		for i in a:
# 			rd+=str(i)
# 			rd+=','
# 		file.writelines(rd)
# 		file.close()			

# 		return render_template('draw.html')


# @app.route('/art',methods = ['POST', 'GET'])
# def art():
# 	with open ('gen.txt') as file:
# 		con = file.readlines()
		
# 		return Response(json.dumps(con), mimetype='application/json')


if __name__ == '__main__':

	app.run(debug = True)
	