from recommendation import recommend
import streamlit as st

st.title("Movie Recommendation System")

movie_name = st.text_input("Enter Movie Name")

if st.button("Recommend"):

    recommendations = recommend(movie_name)

    st.write("Recommended Movies:")

    for movie in recommendations:
        st.write(movie)