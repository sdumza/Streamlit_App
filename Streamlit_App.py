#created main python file
import streamlit as st
import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.title('My Mom\'s  New Healthy Diner')
st.header('Breakfast Menu')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text(' 🐔Hard-Boiled Free-Range Egg')
st.text ('🥑🍞 Advocado toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
pd.DataFrame(my_fruit_list)
