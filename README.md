Certainly! Here's the updated README to include both the TF-IDF and LSI models, along with the combined architecture.

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

Latent Semantic Indexing (LSI) is a technique in natural language processing of analyzing relationships between a set of documents and the terms they contain by producing a set of concepts related to the documents and terms. LSI uses singular value decomposition (SVD) to reduce the dimensions of the term-document matrix, capturing the underlying structure in the data.

#### Mathematical Formulation

LSI uses Singular Value Decomposition (SVD) on the term-document matrix \( A \):

$$ A = U \Sigma V^T $$

Where:
- \( U \) is a matrix where each column is a left singular vector (document-topic matrix).
- \( \Sigma \) is a diagonal matrix of singular values.
- \( V \) is a matrix where each column is a right singular vector (term-topic matrix).

By truncating \( \Sigma \) to the top k singular values, we obtain a reduced-rank approximation of \( A \) which captures the most significant relationships.

## Architecture

The architecture of the Movie Recommendation System is depicted below:

```mermaid
graph LR
A[User] --> B[Web Interface]
B --> C[Flask App]
C --> D1[TF-IDF Model]
C --> D2[LSI Model]
D1 --> E[Movie Recommendations]
D2 --> E[Movie Recommendations]
```

1. **User**: Interacts with the web interface.
2. **Web Interface**: Captures user input and displays recommendations.
3. **Flask App**: Processes the input and communicates with both the TF-IDF and LSI models.
4. **TF-IDF Model**: Computes similarity scores based on the input and movie descriptions.
5. **LSI Model**: Computes similarity scores based on the input and latent semantic analysis.
6. **Movie Recommendations**: Generated list of recommended movies.

## Credits

This project is developed by [Sibasish Dey](https://github.com/Jishu15) and [Riddhiman Dutta](https://github.com/cdnjmusic). Contributions are welcome! Please fork the repository and create a pull request with your enhancements.

Feel free to reach out with any questions or feedback. Enjoy exploring and happy movie watching!

---
