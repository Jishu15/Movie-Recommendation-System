from flask import Flask, request, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel
import numpy as np

app = Flask(__name__)

# Load movie data
movies = pd.read_csv('movies.csv')

# Create a combined text column for TF-IDF
movies['combined'] = movies['movie_title'] + ' ' + movies['director_name'] + ' ' + \
                     movies['actor_1_name'] + ' ' + movies['actor_2_name'] + ' ' + \
                     movies['actor_3_name'] + ' ' + movies['genres'] + ' ' + movies['comb']

# Initialize the TF-IDF Vectorizer using the 'combined' column
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['combined'])

# Initialize the LSI model using TruncatedSVD
svd = TruncatedSVD(n_components=100)
lsi_matrix = svd.fit_transform(tfidf_matrix)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        user_input = request.form['user_input']
        # Transform the user input to match the vectorizer's format
        user_tfidf = tfidf.transform([user_input])
        
        # Compute the cosine similarity between user input and movie descriptions for TF-IDF
        tfidf_cosine_similarities = linear_kernel(user_tfidf, tfidf_matrix).flatten()
        
        # Get top 5 movie indices for TF-IDF
        tfidf_related_docs_indices = tfidf_cosine_similarities.argsort()[:-6:-1]
        tfidf_recommendations = movies.iloc[tfidf_related_docs_indices]
        
        # Calculate the average cosine similarity score for TF-IDF recommendations
        tfidf_avg_score = tfidf_cosine_similarities[tfidf_related_docs_indices].mean()
        tfidf_norm_avg_score = np.interp(tfidf_avg_score, (tfidf_cosine_similarities.min(), tfidf_cosine_similarities.max()), (0, 100))
        
        # Transform the user input to LSI space
        user_lsi = svd.transform(user_tfidf)
        
        # Compute the cosine similarity between user input and movie descriptions for LSI
        lsi_cosine_similarities = cosine_similarity(user_lsi, lsi_matrix).flatten()
        
        # Get top 5 movie indices for LSI
        lsi_related_docs_indices = lsi_cosine_similarities.argsort()[:-6:-1]
        lsi_recommendations = movies.iloc[lsi_related_docs_indices]
        
        # Calculate the average cosine similarity score for LSI recommendations
        lsi_avg_score = lsi_cosine_similarities[lsi_related_docs_indices].mean()
        lsi_norm_avg_score = np.interp(lsi_avg_score, (lsi_cosine_similarities.min(), lsi_cosine_similarities.max()), (0, 100))
        
        return render_template('index.html', 
                               tf_idf_recommendations=tfidf_recommendations.to_dict('records'), 
                               tf_idf_accuracy=round(tfidf_norm_avg_score, 2),
                               lsi_recommendations=lsi_recommendations.to_dict('records'), 
                               lsi_accuracy=round(lsi_norm_avg_score, 2))
    except KeyError as e:
        app.logger.error(f"KeyError: {e}")
        return "There was an error processing your request.", 400
    except Exception as e:
        app.logger.error(f"Exception: {e}")
        return "An unexpected error occurred.", 500

if __name__ == '__main__':
    app.run(debug=True)
