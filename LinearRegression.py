import numpy as np
import pandas as pd
# matrix=np.array([],[])

def mse(Yexpected,Ypred):
    return np.sum((Yexpected - Ypred) ** 2) / len(Yexpected)

#generating a random dataset
np.random.seed(42)
Input=2*np.random.rand(100,1)


Weights=np.random.randn()*0.1
Bias=np.random.randn()*0.1

#updatingg values for weights and biases

# Weights=2.48040145480617
# Bias=2.119494115705277
true_w=4
true_b=3

#finished generating a dataset


Yexpected=true_w*Input+true_b
# print(Input,Yexpected)
n=0
Ypred=(Weights*Input)+Bias
MSE=mse(Yexpected,Ypred)
print('MSE = ', MSE)
print (Yexpected[0],Ypred[0])
#creating  a csv file for convinience

df=pd.DataFrame(np.hstack((Input,Yexpected)),columns=['X','Y'])
df.to_csv('dataset.csv',index=False)
epochs=100
alpha=0.01
for i in range(epochs):
    dw = (-2 / len(Input)) * np.sum(Input* (Yexpected - Ypred))
    db = (-2 / len(Input)) * np.sum(Yexpected - Ypred)
    Weights=Weights-alpha*dw
    Bias=Bias-alpha*db
    Ypred=(Weights*Input)+Bias
    print("Updated Value")
    print (Yexpected[6],Ypred[6])
    # print(Weights,Bias)
    MSE=mse(Yexpected,Ypred)
    print('MSE = ', MSE)


