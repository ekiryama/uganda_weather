import pandas as pd
import numpy as np
from datetime import time, datetime
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

st.header('st.slider Day 8')
# Example 1
st.write(" *Example 1 (Integer slider)*")
st.subheader('Slider')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
# Example 2
st.subheader('Range slider')
values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
# Example 3
st.subheader('Range time slider')
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)
# Example 4
st.subheader('Datetime slider')
start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


st.header('Line chart Day 9')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.header('st.selectbox Day 10')
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))
st.write('Your favorite color is ', option)

st.header('st.multiselect Day 11')
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
st.write('You selected:', options)

st.header('st.checkbox Day 12')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")
if coffee: 
     st.write("Okay, here's some coffee ☕")
if cola:
     st.write("Here you go 🥤")
st.header('st.latex Day 15')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
st.title('Customizing the theme of Streamlit apps Day 16')
st.write('Contents of the `.streamlit/config.toml` file of this app')
st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)

st.title('st.secrets Day 17')
st.write(st.secrets['message'])
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

