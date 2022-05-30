
import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favourites')
streamlit.text('🥣omega 2 & Blueberry Oatmeal')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.header('Fruityvice Fruit Advice!')

miport requests
fruityvice_response = requests.get("https://fruitvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
