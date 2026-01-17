from ml_model.loder import load_scaler
import pandas as pd
features1=['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts','EstimatedSalary']
       
feature2=['Gender','HasCrCard', 'IsActiveMember','Geography_Germany','Geography_Spain']
def preprocess(payload):
    data=[]
    for i in features1:
        data.append(payload[i])
    if payload['Gender']=="Male":
        data.append(1)
    else:
        data.append(0)
    if payload['HasCrCard']=="Yes":
        data.append(1)
    else:
        data.append(0)
    if payload['IsActiveMember']=="Yes":
        data.append(1)
    else:
        data.append(0)
    if payload['Geography']=="France":
        data.append(0)
        data.append(0)
    elif payload['Geography']=="Germany":
        data.append(1)
        data.append(0)
    else:
        data.append(0)
        data.append(1)
    columns=features1+feature2
    dataset=pd.DataFrame([data],columns=columns)
    scaler=load_scaler()
    dataset[features1]=scaler.transform(dataset[features1])



    return dataset


