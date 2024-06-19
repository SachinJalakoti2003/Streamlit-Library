import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

chart_data=pd.DataFrame(np.random.randn(20,3), columns=['Line-1','Line-2','Line-3'])
st.header("1.Charts with random numbers")

st.subheader("1.1-Line_Chart")
st.line_chart(chart_data)


st.subheader("1.2-Area Chart")
st.area_chart(chart_data)

st.subheader("1.3-Bar chart")
st.bar_chart(chart_data)

st.subheader("1.4-Scatter chart")
st.scatter_chart(chart_data)

st.header("2.Data Visiualization with Matplotlib & Seaborn Library")
st.subheader("2.1-Loading the DataFrame")
df=pd.read_csv("Details.csv")
st.dataframe(df.head())

st.subheader("2.2 Distribution Plot using matplotlib")
fig=plt.figure(figsize=(15,8))
df['Quantity'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader("2.3 Distribution plot using seaborn")
fig=plt.figure(figsize=(15,8))
sns.distplot(df['Quantity'])
st.pyplot(fig)

st.header("3.Multiple Graphs using")
st.subheader("3.1 ")

col1,col2 = st.columns(2)

with col1:
    col1.header='KDE=false'
    fig1=plt.figure(figsize=(5,5))
    sns.distplot(df['Quantity'],kde=False)
    st.pyplot(fig1)

with col2:
    col2.header='Hist=false'
    fig2=plt.figure(figsize=(5,5))
    sns.distplot(df['Quantity'],hist=False)
    st.pyplot(fig2)


st.header("4.Changing the style of the graph")
col1,col2 = st.columns(2)

with col1:
    fig1=plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['Quantity'],hist=False)
    st.pyplot(fig1)

with col2:
    fig2=plt.figure()
    sns.set_theme(context='poster',style='darkgrid')
    sns.distplot(df['Quantity'],hist=False)
    st.pyplot(fig2)


st.header("5.Exploring Different Graphs")
st.subheader('5.1 Scatter Plot')
fig,ax= plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)


st.subheader('5.2 Count-plot')
fig= plt.figure(figsize=(15,8))
sns.countplot(data=df, x='PaymentMode')
st.pyplot(fig)


st.subheader('5.3 Box-Plot')
fig= plt.figure(figsize=(15,8))
sns.boxplot(data=df, x='PaymentMode', y='Sub-Category', saturation=1)
st.pyplot(fig)


st.subheader('5.4 Violin-Plot')
fig= plt.figure(figsize=(15,8))
sns.violinplot(data=df, x='PaymentMode', y='Sub-Category', saturation=1)
st.pyplot(fig)



