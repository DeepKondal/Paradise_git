#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import pickle




df = pd.read_csv('train.csv')


def get_title(name):
    if '.' in name:
        return name.split(',')[1].split('.')[0].strip()
    else:
        return 'no title in name'
    
    
titles = set([x for x in df.Name.map(lambda x : get_title(x))])



def replace_titles(x):
    title = x['Title']
    if title in ['Capt','Col','Major']:
        return 'Officer'
    elif title in ['Jonkheer','Don','the Countess','Lady','Dona','Sir']:
        return 'Royality'
    elif title =='Mme':
        return 'Mrs'
    elif title in ['Mlle','Ms']:
        return 'Miss'
    else:
        return title
    
    
    
df['Title'] = df['Name'].map(lambda x : get_title(x))
df['Title'] = df.apply(replace_titles,axis=1)


df['Age'].fillna(df['Age'].median(),inplace=True)
df['Fare'].fillna(df['Fare'].median(),inplace=True)
df['Embarked'].fillna("S",inplace=True)
df.drop('Ticket',axis=1,inplace=True)
df.drop('Cabin',axis=1, inplace=True)
df.drop('Name',axis=1,inplace=True)
df.Sex.replace(('male','female'),(0,1),inplace=True)
df.Embarked.replace(('S','C','Q'),(0,1,2),inplace=True)
df.Title.replace(('Mr','Miss','Mrs','Master','Dr','Rev','Officer','Royality'),(0,1,2,3,4,5,6,7),inplace=True)




predictiors = df.drop(['Survived','PassengerId'],axis=1)
target = df['Survived']
x_train,x_val,y_train,y_val = train_test_split(predictiors,target,test_size=0.22,random_state=0)



randomforest = RandomForestClassifier()
randomforest.fit(x_train,y_train)
y_pred = randomforest.predict(x_val)



filename = 'titanic_model.sav'
pickle.dump(randomforest,open(filename,'wb'))



# In[ ]:




