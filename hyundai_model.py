import numpy as np
import pandas as pd
import joblib 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv(r"C:\Users\Sneh\Documents\Project\Hyundai\data\Hyundai_ml.csv")

x = df.drop('price',axis=1)
y = df['price']

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=51)

sc = StandardScaler()
q = sc.fit(x_train)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)

l = list(x.columns)
l = l[1:]
ml_model = joblib.load(r"hyundai_ml_model.pkl")
#print(l)
#print(len(l))

def car_price(year,total_run,tax,engineSize,mileage,car_model,trans,fule):
    
    arr = np.zeros(len(x.columns))
    
    arr[0] = year
    arr[1] = total_run
    arr[2] = tax
    arr[3] = engineSize
    arr[4] = mileage
    
    if "model_ " + car_model in x.columns:
        index = np.where(x.columns == "model_ " + car_model)
        arr[index]=1
        
    if "transmission_" + trans in x.columns:
        index = np.where(x.columns == "transmission_" + trans)
        arr[index]=1
        
    if "fule_" + fule in x.columns:
        index = np.where(x.columns == "fule_" + fule)
        arr[index]=1
    
    arr = sc.transform([arr])
    return ml_model.predict(arr)[0]