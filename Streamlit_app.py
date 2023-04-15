import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import streamlit as st

import altair as alt

st.write('Hello world!')

st.write("""
# Weather Model Day 2
Below is my Weather model
""")

st.header('st.button Header DAy 3')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')



st.header('st.write Day 5')

# Example 1
st.write(" *Example 1*")

st.write('Hello, *World!* :sunglasses:')

# Example 2
st.write(" *Example 2 (numbers)*")
st.write(1234)

# Example 3


st.write(" *Example 3 (DataFrame)*")
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4
st.write(" *Example 4 (DataFrame 2)*")
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5
st.write(" *Example 5 (chart)*")
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

mycode= """If tojcbj:
     second line of code tojcbj

l=5
"""
st.code(mycode, language='python')


















# df = pd.read_csv('Uganda_merged_2023-3-28.csv')
# df.tail()

# df.columns= ["Station Name","SubDivision1","SubDivision2","Date","Average Humidity","Minimum Humidity","Maximum Humidity","Unit Humidity","Average Temperature","Maximum Temperature","Minimum Temperature","Unit Temperature","Precipitation","Unit Precipitation","Windspeed","Unit Windspeed"]

# filtered_df = df[df["Station Name"] == "BIHYA I -1"].copy()

# filtered_df.index=pd.to_datetime(filtered_df.Date)
# filtered_df.index

# filtered_df.loc[:, "Target"] = filtered_df["Average Temperature"].shift(-1)

# filtered_df=filtered_df.drop(["Average Temperature"], axis=1)

# core_df=filtered_df[["Minimum Humidity","Maximum Humidity","Maximum Temperature","Minimum Temperature","Precipitation","Windspeed","Target"]]
# core_df.head()

# core_df.index.year
# core_df.columns=['min_hum', 'max_hum', 'max_temp', 'min_temp', 'precip', 'windspeed','Target']
# core_df[["min_temp","max_temp"]].plot()


# core_df[["precip"]].plot()

# # Training the Model

# from sklearn.linear_model import Ridge
# reg = Ridge(alpha=.1)

# predictors = ['min_hum', 'max_hum', 'max_temp', 'min_temp', 'precip', 'windspeed']

# def create_predictions(predictors, core_df, reg):
#     train= core_df.loc[:"2001-06"]
#     test= core_df.loc["2001-07":]
#     reg.fit(train[predictors],train["Target"])
#     predictions= reg.predict(test[predictors])
#     error= mean_absolute_error(test["Target"], predictions)
#     combined = pd.concat([test["Target"], pd.Series(predictions, index=test.index)], axis=1)
#     combined.columns= ["Actual", "Predictions"]
#     return error, combined









