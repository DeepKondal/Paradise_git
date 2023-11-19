import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle


def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    import pickle
    from sklearn.ensemble import RandomForestClassifier
    x= [[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    randomforest  =pickle.load(open('titanic_model.sav','rb'))
    prediction = randomforest.predict(x)
    if prediction == 0:
        prediction = "didn't Survive"
    elif prediction ==1:
        prediction = 'Survived'
    else:
        prediction = 'Error'
    return prediction