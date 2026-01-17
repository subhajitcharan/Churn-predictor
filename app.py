from fastapi import FastAPI
from src.scemas import data
from src.preprocessing import preprocess
from src.predict import predict
app=FastAPI()

@app.get('/')
def home_Page():
    return {"message":"api is online"}

@app.post("/predict")
def prediction(data:data):
    x=data.model_dump()
    x=preprocess(x)
    pred=predict(x)
    if pred==[1]:
         return {"message":"this customer is likely to churn"}
    if pred==[0]:
         return {"message":"this customer not likely to churn"}