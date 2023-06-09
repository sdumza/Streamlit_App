#created main python file
import streamlit as st
import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
st.title('My Mom\'s  New Healthy Diner')
st.header('Breakfast Menu')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text(' 🐔Hard-Boiled Free-Range Egg')
st.text ('🥑🍞 Advocado toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

st.dataframe(my_fruit_list)

fruits_to_show = my_fruit_list.loc[fruits_selected]
st.header ('Your selected fruits') 
st.dataframe(fruits_to_show)
