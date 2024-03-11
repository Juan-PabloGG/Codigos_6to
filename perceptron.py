w1=1
w2=1
w3=1
x0=[1,1,1,1]
x1=[-1,-1,1,1]
x2=[-1,1,-1,1]
y=[-1,-1,-1,1]
wr1=[]
wr2=[]
wr3=[]

import numpy as np                  
    
def entrenamiento(w1,w2,w3,x0,x1,x2,k):
    z=(w1*x0[k]) + (w2*x1[k]) + (w3*x2[k])
    ye=np.sign(z)
    return ye

def prediccion(w1,w2,w3,ye,k):
    w1=w1+0.5*(y[k]-ye)*x0[k]
    w2=w2+0.5*(y[k]-ye)*x1[k]
    w3=w3+0.5*(y[k]-ye)*x2[k]
    wres=[w1,w2,w3]
    return wres

ye1=entrenamiento(w1,w2,w3,x0,x1,x2,0)
ye2=entrenamiento(w1,w2,w3,x0,x1,x2,1)
ye3=entrenamiento(w1,w2,w3,x0,x1,x2,2)
ye4=entrenamiento(w1,w2,w3,x0,x1,x2,3)

wr1=prediccion(w1,w2,w3,ye1,0)
wr2=prediccion(wr1[0],wr1[1],wr1[2],ye2,1)
wr3=prediccion(wr2[0],wr2[1],wr2[2],ye2,2)
wr4=prediccion(wr3[0],wr3[1],wr3[2],ye2,3)
