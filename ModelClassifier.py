import pandas as pd

import os

#os.chdir('C:\\Users\\leven\\Desktop\\Streamlit_ML')
 
train = pd.read_csv('train_ctrUa4K.csv') 
train.head()


train['Gender']= train['Gender'].map({'Male':0, 'Female':1})
train['Married']= train['Married'].map({'No':0, 'Yes':1})
train['Loan_Status']= train['Loan_Status'].map({'N':0, 'Y':1})


train = train.dropna()
#train.isnull().sum()

X = train[['Gender', 'Married', 'ApplicantIncome', 'LoanAmount', 'Credit_History']]
y = train.Loan_Status


from sklearn.model_selection import train_test_split
x_train, x_cv, y_train, y_cv = train_test_split(X,y, test_size = 0.2, random_state = 10)


from sklearn.ensemble import RandomForestClassifier 
model = RandomForestClassifier(max_depth=4, random_state = 10) 
model.fit(x_train, y_train)


from sklearn.metrics import accuracy_score
pred_cv = model.predict(x_cv)
accuracy_score(y_cv,pred_cv)

pred_train = model.predict(x_train)
accuracy_score(y_train,pred_train)

import pickle 
pickle_out = open("classifier.pkl", mode = "wb") 
pickle.dump(model, pickle_out) 
pickle_out.close()



