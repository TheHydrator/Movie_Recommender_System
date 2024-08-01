# Movie_Recommender_System

**Project Description**
This project is a **Movie Recommender System** built using the TMDb (The Movie Database) dataset from Kaggle. The system employs recommendation algorithms to suggest movies to users based on their preferences. The project features a web application developed with Streamlit that allows users to interact with the recommender system and receive personalized movie suggestions.

**Key Features**
Personalized Movie Recommendations: Utilizes collaborative filtering and content-based methods to recommend movies based on a user’s selected movie.
Movie Details: Displays movie posters and provides Google search links for more information.
Interactive Web Interface: Built with Streamlit, offering a user-friendly experience for movie recommendations.

**How It Works**
**User Input:** Users select a movie they like from a dropdown menu.
**Recommendation Engine:** The system processes the input using pre-trained models and generates a list of recommended movies.
**Display Results:** The recommended movies, along with their posters and Google search links, are displayed to the user.

**Technologies Used**
Data Science: Python, Pandas
Machine Learning: Scikit-Learn, Surprise Library
Web Development: Streamlit
Deployment: Heroku
APIs: TMDb API for fetching movie details and posters
Setup and Installation
To run this project locally:

**Deployment**
The application is deployed on Heroku. You can access the live application at Heroku App URL.

**Files Included**
app.py: Main script to run the Streamlit app.
movie_dict.pkl: Pickled file containing movie data.
similarity.pkl: Pickled file containing similarity matrix.
.streamlit/config.toml: Configuration file for Streamlit.
requirements.txt: Lists the required Python packages.
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request. For any issues or feature requests, open an issue on GitHub.

**License**
This project is licensed under the MIT License. See the LICENSE file for more details.

**Acknowledgements**
TMDb Dataset: Data provided by Kaggle.
Streamlit: Framework used for building the web interface.
Heroku: Platform used for deployment.
