import streamlit as st
import pandas as pd
import pickle
import requests # connecting with tmdb

# loading pkl model
movies = pickle.load(open("movies_dict.pkl", "rb"))
movies_df = pd.DataFrame(movies)
similarity = pickle.load(open("simi_score.pkl","rb"))

# API fetching images
def fetch_img(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=5de01b953b61da4a0f98ba5a04b1737a&language=en-US")
    data = response.json()
    return "https://image.tmdb.org/t/p/original"+ data["poster_path"]


def recommendation(movie):
    l = []
    poster_l = []
    movie_index = movies_df[movies_df["title"]==movie].index[0]
    simi_score = list(enumerate(similarity[movie_index]))
    simi_score = sorted(simi_score, key= lambda x: x[1], reverse=True)
    for i in simi_score[1:12]:
        name = movies_df.iloc[i[0], 1]
        l.append(name)
        movie_id = movies_df.iloc[i[0], 0] # getting movie_id for poster fetching
        img_url = fetch_img(movie_id) # fetching poster from function
        poster_l.append(img_url)
    return l, poster_l


def main():
    st.title("Movie Recommendation System")
    st.sidebar.title("Content Based")
    st.sidebar.markdown("It recommends you based on content that you like")
  
    movie_name = st.sidebar.selectbox("Enter your movie name here ", movies_df["title"].values)
    # global num
    # num = st.sidebar.number_input("Number of Recommendations", step=1, min_value=5, max_value=50)
  
    st.sidebar.checkbox("Consider the Plots ?", True, key = 1)

    #recommendation value
    recommend = None

    if st.sidebar.button("Recommend me!"):
        recommend_movies, recommend_poster = recommendation(movie_name)
        st.write(f"movies similar to *{movie_name.title()}*")
        # print(recommend_poster[:5])
        col1, col2, col3, col4, col5  = st.columns(5)
        with col1:
            st.write(recommend_movies[0])
            st.image(recommend_poster[0])
        with col2:
            st.write(recommend_movies[1])
            st.image(recommend_poster[1])
        with col3:
            st.write(recommend_movies[2])
            st.image(recommend_poster[2])
        with col4:
            st.write(recommend_movies[3])
            st.image(recommend_poster[3])
        with col5:
            st.write(recommend_movies[4])
            st.image(recommend_poster[4])
        with st.expander("More +"):
            col1, col2, col3, col4, col5  = st.columns(5)
            with col1:
                st.write(recommend_movies[5])
                st.image(recommend_poster[5])
            with col2:
                st.write(recommend_movies[6])
                st.image(recommend_poster[6])
            with col3:
                st.write(recommend_movies[7])
                st.image(recommend_poster[7])
            with col4:
                st.write(recommend_movies[8])
                st.image(recommend_poster[8])
            with col5:
                st.write(recommend_movies[9])
                st.image(recommend_poster[9])
            
            


    else:
        st.markdown("![You're like this!](https://i.gifer.com/JUd.gif)")
        st.write("*Meanwhile my System*")

    st.sidebar.write("## Thank you for Visiting \nProject by Nikhil J")
    st.sidebar.markdown("<h1 style='text-align: right; color: #d7e3fc; font-size: small;'><a href='https://github.com/Nikhil-Jagtap619/Recommendation-System'>Looking for Source Code?</a></h1>", unsafe_allow_html=True)
  # st.markdown("<h1 style='text-align: right; color: white; font-size: small'>you can find it on my GitHub</h1>", unsafe_allow_html=True)

    


if __name__=="__main__":
    main()
