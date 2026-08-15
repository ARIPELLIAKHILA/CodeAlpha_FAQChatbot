\# E-Commerce FAQ Chatbot



\## Project Overview



This project is an AI-based FAQ Chatbot developed as part of the CodeAlpha Artificial Intelligence Internship.



The chatbot uses Natural Language Processing (NLP) techniques to understand user questions and provide the most relevant answer from a predefined FAQ dataset.



\## Objective



The objective of this project is to develop a chatbot that can match user questions with the most similar frequently asked question and provide an appropriate response.



\## Technologies Used



\- Python

\- Flask

\- NLTK

\- Scikit-learn

\- HTML

\- CSS

\- JavaScript



\## AI/NLP Techniques



\- Text Preprocessing

\- TF-IDF Vectorization

\- Cosine Similarity

\- Natural Language Processing



\## Features



\- Interactive chatbot interface

\- FAQ-based question answering

\- NLP-based question matching

\- TF-IDF text vectorization

\- Cosine similarity for finding the best matching question

\- Response for questions outside the available FAQ dataset



\## How It Works



1\. The user enters a question in the chatbot.

2\. The question is preprocessed and cleaned.

3\. FAQ questions are converted into TF-IDF vectors.

4\. Cosine similarity is used to compare the user's question with the FAQ dataset.

5\. The chatbot identifies the most similar question.

6\. The corresponding answer is displayed to the user.

7\. If no suitable match is found, the chatbot provides a fallback response.



\## Example Questions



\- How do I track my package?

\- Can I return something I bought?

\- What payment options do you have?

\- When will my package arrive?

\- Can I change my delivery address?

\- How can I contact customer support?



\## Project Structure



```text

CodeAlpha\_FAQChatbot/

│

├── app.py

├── chatbot.py

├── requirements.txt

├── README.md

│

├── templates/

│   └── index.html

│

└── static/

&#x20;   └── style.css
## Installation

1. Clone the repository.

YOUR_GITHUB_REPOSITORY_URL

2. Open the project folder.

    cd CodeAlpha_FAQChatbot

3. Create a virtual environment.

    python -m venv venv

4. Activate the virtual environment on Windows.

    venv\Scripts\activate

5. Install the required packages.

    pip install -r requirements.txt


## Run the Project

Run the following command:

    python app.py

Then open this address in your browser:

    http://127.0.0.1:5000


## Future Improvements

- Add more FAQs
- Add voice input
- Add voice responses
- Add multilingual support
- Improve intent classification
- Add a larger FAQ dataset


## Internship

This project was developed as part of the CodeAlpha Artificial Intelligence Internship.
