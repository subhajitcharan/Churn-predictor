from ml_model.loder import load_model

def predict(data):
    model=load_model()
    pred=model.predict(data)
    return pred
