import streamlit as st
import pandas as pd
import pickle

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Netflix Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv("dataset/netflix_with_tags.csv")

df = load_data()

# ============================================================
# LOAD MODELS
# ============================================================

with open("models/cosine_similarity.pkl", "rb") as f:
    cosine_sim = pickle.load(f)

with open("models/title_indices.pkl", "rb") as f:
    indices = pickle.load(f)

# ============================================================
# NETFLIX THEME
# ============================================================

st.markdown("""
<style>

.stApp{
    background-color:#141414;
    color:white;
}

h1,h2,h3{
    color:#E50914;
}

[data-testid="stMetricValue"]{
    color:#E50914;
}

.stButton>button{
    background-color:#E50914;
    color:white;
    border:none;
    border-radius:8px;
    width:100%;
}

.stButton>button:hover{
    background-color:#B20710;
}

.movie-card{
    background-color:#1f1f1f;
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    "<h1 style='text-align:center;'>🎬 NETFLIX RECOMMENDATION SYSTEM</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Netflix Analytics + Machine Learning Recommendation Engine</p>",
    unsafe_allow_html=True
)

# ============================================================
# KPI SECTION
# ============================================================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Titles", len(df))

col2.metric(
    "Movies",
    len(df[df["type"]=="Movie"])
)

col3.metric(
    "TV Shows",
    len(df[df["type"]=="TV Show"])
)

col4.metric(
    "Countries",
    df["country"].nunique()
)

st.markdown("---")

# ============================================================
# RECOMMEND BY TITLE
# ============================================================

def recommend_by_title(title, n=10):

    title_map = {
        t.lower(): t
        for t in df["title"]
    }

    title = title.lower().strip()

    if title not in title_map:
        return None

    actual_title = title_map[title]

    idx = indices[actual_title]

    sim_scores = list(
        enumerate(cosine_sim[idx])
    )

    sim_scores = sorted(
        sim_scores,
        key=lambda x:x[1],
        reverse=True
    )

    sim_scores = sim_scores[1:n+1]

    movie_indices = [
        i[0]
        for i in sim_scores
    ]

    return df.iloc[movie_indices][
        [
            "title",
            "type",
            "listed_in",
            "release_year",
            "rating",
            "description"
        ]
    ]

# ============================================================
# TABS
# ============================================================

tab1, tab2 = st.tabs(
    [
        "🎯 Recommend By Title",
        "🎯 Recommend By Preferences"
    ]
)

# ============================================================
# TAB 1
# ============================================================

with tab1:

    st.subheader("Content Based Recommendation")

    movie_name = st.selectbox(
        "Select Netflix Title",
        sorted(df["title"].unique())
    )

    if st.button("Recommend Similar Titles"):

        recs = recommend_by_title(movie_name)

        if recs is None:
            st.error("Title not found")
        else:

            st.success(
                f"Top Recommendations for {movie_name}"
            )

            for _, row in recs.iterrows():

                st.markdown(f"""
                <div class='movie-card'>
                <h4>{row['title']}</h4>
                <p><b>Type:</b> {row['type']}</p>
                <p><b>Genre:</b> {row['listed_in']}</p>
                <p><b>Year:</b> {row['release_year']}</p>
                <p><b>Rating:</b> {row['rating']}</p>
                <p>{row['description']}</p>
                </div>
                """, unsafe_allow_html=True)

# ============================================================
# TAB 2
# ============================================================

with tab2:

    st.subheader("Preference Based Recommendation")

    genres = sorted(
        df["listed_in"].dropna().unique()
    )

    types = sorted(
        df["type"].dropna().unique()
    )

    ratings = sorted(
        df["rating"].dropna().unique()
    )

    countries = sorted(
        df["country"].dropna().unique()
    )

    col1, col2 = st.columns(2)

    with col1:

        selected_type = st.selectbox(
            "Content Type",
            ["All"] + types
        )

        selected_genre = st.selectbox(
            "Genre",
            ["All"] + genres
        )

    with col2:

        selected_rating = st.selectbox(
            "Rating",
            ["All"] + ratings
        )

        selected_country = st.selectbox(
            "Country",
            ["All"] + countries
        )

    year_range = st.slider(
        "Release Year",
        int(df["release_year"].min()),
        int(df["release_year"].max()),
        (
            2015,
            int(df["release_year"].max())
        )
    )

    num_recs = st.slider(
        "Number of Recommendations",
        5,
        20,
        10
    )

    if st.button("Get Personalized Recommendations"):

        filtered_df = df.copy()

        if selected_type != "All":
            filtered_df = filtered_df[
                filtered_df["type"]
                == selected_type
            ]

        if selected_genre != "All":
            filtered_df = filtered_df[
                filtered_df["listed_in"]
                .str.contains(
                    selected_genre,
                    case=False,
                    na=False
                )
            ]

        if selected_rating != "All":
            filtered_df = filtered_df[
                filtered_df["rating"]
                == selected_rating
            ]

        if selected_country != "All":
            filtered_df = filtered_df[
                filtered_df["country"]
                .str.contains(
                    selected_country,
                    case=False,
                    na=False
                )
            ]

        filtered_df = filtered_df[
            (filtered_df["release_year"]
             >= year_range[0])
            &
            (filtered_df["release_year"]
             <= year_range[1])
        ]

        if len(filtered_df) == 0:
            st.error(
                "No matching content found."
            )

        else:

            results = filtered_df.sample(
                min(num_recs,
                    len(filtered_df))
            )

            st.success(
                f"Found {len(results)} recommendations"
            )

            for _, row in results.iterrows():

                st.markdown(f"""
                <div class='movie-card'>
                <h4>{row['title']}</h4>
                <p><b>Type:</b> {row['type']}</p>
                <p><b>Genre:</b> {row['listed_in']}</p>
                <p><b>Year:</b> {row['release_year']}</p>
                <p><b>Rating:</b> {row['rating']}</p>
                <p>{row['description']}</p>
                </div>
                """, unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
"""
<center>
Built using Python • Streamlit • TF-IDF • Cosine Similarity • Power BI
</center>
""",
unsafe_allow_html=True
)