---

# Movie Recommendation System (TF-IDF and LSI)

Welcome to the **Movie Recommendation System** project! This project uses both TF-IDF and LSI models to recommend movies based on textual descriptions. Below, you'll find all the information you need to set up and run the project.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
  - [TF-IDF Model](#tf-idf-model)
  - [LSI Model](#lsi-model)
- [Architecture](#architecture)
- [Credits](#credits)

## Project Structure

```plaintext
movie_recommendation/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── movies.csv
├── requirements.txt
└── .srcenv/
```

- **app.py**: The main Flask application file.
- **templates/index.html**: The HTML template for the web interface.
- **static/style.css**: The CSS file for styling the web interface.
- **movies.csv**: The dataset containing movie information.
- **requirements.txt**: The file listing all Python dependencies.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/movie_recommendation.git
cd movie_recommendation
```

2. **Create a virtual environment** (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
```

3. **Install the required packages**:

```bash
pip install -r requirements.txt
```

4. **Run the Flask application**:

```bash
python app.py
```

5. **Access the application**:

Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

1. Open the web application in your browser.
2. Enter a description or keywords related to the type of movie you're looking for.
3. Click the "Search" button.
4. The system will display a list of recommended movies based on the provided description.

## Models

### TF-IDF Model

#### What is TF-IDF?

TF-IDF stands for Term Frequency-Inverse Document Frequency. It is a numerical statistic intended to reflect how important a word is to a document in a collection or corpus. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus.

#### Mathematical Formulation

The TF-IDF value is calculated as:

$$ \text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D) $$

Where:
- ${TF}(t, d)$ is the term frequency of term $(t)$ in document $(d)$.
- ${IDF}(t, D)$ is the inverse document frequency of term $(t)$ across all documents $(D)$.

The term frequency ${TF}(t, d)$ is calculated as:

$$ \text{TF}(t, d) = \frac{\text{Number of times term } t \text{ appears in document } d}{\text{Total number of terms in document } d} $$

The inverse document frequency ${IDF}(t, D)$ is calculated as:

$$ \text{IDF}(t, D) = \log \left( \frac{N}{|\{d \in D : t \in d\}|} \right) $$

Where:
- $N$ is the total number of documents.
- $\{d \in D : t \in d\}$ is the number of documents where the term $(t)$ appears.

### LSI Model

#### What is LSI?

Latent Semantic Indexing (LSI) is a technique in natural language processing for analyzing relationships between a set of documents and the terms they contain by producing a set of concepts related to the documents and terms. LSI uses singular value decomposition (SVD) to reduce the dimensions of the term-document matrix, capturing the underlying structure in the data.

#### Mathematical Formulation

LSI uses Singular Value Decomposition (SVD) on the term-document matrix \( A \):

$$ A = U \Sigma V^T $$

Where:
- \( U \) is a matrix where each column is a left singular vector (document-topic matrix).
- \( \Sigma \) is a diagonal matrix of singular values.
- \( V \) is a matrix where each column is a right singular vector (term-topic matrix).

By truncating \( \Sigma \) to the top k singular values, we obtain a reduced-rank approximation of \( A \) which captures the most significant relationships.

## Architecture

The architecture of the Movie Recommendation System focuses on the data flow and the operations of the TF-IDF and LSI models:

```mermaid
graph TD
  A[Movie Dataset] -->|Load Data| B[Data Preprocessing]
  B -->|Create Combined Text Column| C[TF-IDF Vectorizer]
  B -->|Create Combined Text Column| D[LSI Model]

  subgraph TF-IDF
    C -->|Transform Text Data| E[TF-IDF Matrix]
    E -->|User Input| F[TF-IDF Vectorizer]
    F -->|Compute Similarity| G[Cosine Similarity]
    G -->|Top Recommendations| H[TF-IDF Recommendations]
  end

  subgraph LSI
    D -->|Transform Text Data| I[Term-Document Matrix]
    I -->|SVD| J[LSI Matrix]
    J -->|User Input| K[LSI Vectorizer]
    K -->|Compute Similarity| L[Cosine Similarity]
    L -->|Top Recommendations| M[LSI Recommendations]
  end

  H --> N[Final Recommendations]
  M --> N
```

1. **Movie Dataset**: Contains movie information.
2. **Data Preprocessing**: Prepares the data, creating a combined text column for each movie.
3. **TF-IDF Vectorizer**: Converts the text data into a TF-IDF matrix.
4. **LSI Model**: Converts the text data into a term-document matrix and applies SVD to reduce dimensions.
5. **TF-IDF Matrix**: Represents the importance of terms in each document.
6. **LSI Matrix**: Represents the reduced-rank approximation capturing the significant relationships.
7. **User Input**: User-provided description or keywords.
8. **TF-IDF Vectorizer**: Transforms the user input into the TF-IDF space.
9. **LSI Vectorizer**: Transforms the user input into the LSI space.
10. **Cosine Similarity**: Computes similarity scores between the user input and the movies in the dataset.
11. **Top Recommendations**: Generates the top movie recommendations based on similarity scores.
12. **Final Recommendations**: Combines the top recommendations from both models.

## Credits

This project is developed by [Sibasish Dey](https://github.com/Jishu15) and [Riddhiman Dutta](https://github.com/cdnjmusic). Contributions are welcome! Please fork the repository and create a pull request with your enhancements.

Feel free to reach out with any questions or feedback. Enjoy exploring and happy movie watching!

---
