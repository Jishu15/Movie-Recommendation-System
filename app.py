from flask import Flask, request, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        user_input = request.form['user_input']
        # Transform the user input to match the vectorizer's format
        user_tfidf = tfidf.transform([user_input])
        
        # Compute the cosine similarity between user input and movie descriptions
        cosine_similarities = linear_kernel(user_tfidf, tfidf_matrix).flatten()
        
        # Get top 5 movie indices
        related_docs_indices = cosine_similarities.argsort()[:-6:-1]
        recommendations = movies.iloc[related_docs_indices]
        
        # Calculate the average cosine similarity score for the recommendations
        avg_score = cosine_similarities[related_docs_indices].mean()
        
        # Normalize the cosine similarity score to a 0-100 scale
        norm_avg_score = np.interp(avg_score, (cosine_similarities.min(), cosine_similarities.max()), (0, 100))
        
        return render_template('index.html', recommendations=recommendations.to_dict('records'), accuracy=round(norm_avg_score, 2))
    except KeyError as e:
        app.logger.error(f"KeyError: {e}")
        return "There was an error processing your request.", 400
    except Exception as e:
        app.logger.error(f"Exception: {e}")
        return "An unexpected error occurred.", 500

if __name__ == '__main__':
    app.run(debug=True)
