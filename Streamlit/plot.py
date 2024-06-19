import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as  px
import plotly.figure_factory as ff

st.header('1. Altair Scatter Plot')
chart_data=pd.DataFrame(np.random.randn(500,5),columns=['a','b','c','d','e'])
chart=alt.Chart(chart_data).mark_circle().encode(x='a',y='b', size='c', tooltip=['a','b','c','d','e'])
st.altair_chart(chart)


st.header("2.Interactive Charts")
st.subheader("2.1 Line Chart")
df=pd.read_csv('H.csv')
patient=df.columns.tolist()
patient_details_choices=st.multiselect('Choose your Patient Details', patient)
new_df=df[patient_details_choices]
st.line_chart(new_df)

st.subheader("2.2 Area chart")
st.area_chart(new_df)


st.header("3.Data Visualisation with plotly")
st.subheader("3.1 Displaying the Dataset")
df=pd.read_csv("titanic.csv")
st.dataframe(df.head())

st.subheader("3.2 Pie Chart")
fig=px.pie(df,values='Survived', names='Embarked')
st.plotly_chart(fig)


st.subheader("3.3 Pie Chart with Multiple Parameters")
fig=px.pie(df,values='Survived', names='Embarked', opacity=.7, color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.subheader("3.4 Histograms")
x1=np.random.randn(200)
x2=np.random.randn(200)
x3=np.random.randn(200)

hist_data=[x1,x2,x3]
group_labels=['group-1','group-2','group-3']
fig=ff.create_distplot(hist_data, group_labels, bin_size=[.1,.25,.5])

st.plotly_chart(fig)





