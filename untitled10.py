import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r"C:\Users\kursa\Downloads\reklam.csv")
print(data)
x= data.iloc[:,1:-1].values
y=data.iloc[:,1:-1].values
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=22)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)

yhead=lr.predict(x_test)

import streamlit as st

st.title("reklamharcama")
st.write("veri başlığı")
st.write(data.head())

tv_input=st.number_input("tv rekalm",min_value=0,value=44)
radyo_input=st.number_input("tv rekalm",min_value=0,value=48)
gazete_input=st.number_input("tv rekalm",min_value=0,value=35)

value=np.array([[tv_input,radyo_input,gazete_input]])

predict_value=lr.predict(value)

st.write("verilsad",predict_value)