from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# FAQ dataset
faqs = [
    {
        "questions": [
            "How can I track my order?",
            "Where is my order?",
            "Where can I track my package?",
            "How do I track my package?",
            "Can I track my order?",
            "What is the status of my order?"
        ],
        "answer": "You can track your order using the tracking option in your account."
    },
    {
        "questions": [
            "What is the return policy?",
            "Can I return an item?",
            "How can I return a product?",
            "Can I return something I bought?",
            "How many days do I have to return a product?",
            "I want to return my order."
        ],
        "answer": "Eligible products can be returned within 7 days of delivery."
    },
    {
        "questions": [
            "How can I cancel my order?",
            "Can I cancel my order?",
            "I want to cancel my order.",
            "How do I cancel an order?",
            "Can I cancel an item?"
        ],
        "answer": "You can cancel your order from the Orders section before it is shipped."
    },
    {
        "questions": [
            "What payment methods do you accept?",
            "What payment options are available?",
            "How can I pay?",
            "Can I pay using UPI?",
            "Do you accept credit cards?",
            "Do you accept debit cards?"
        ],
        "answer": "We accept credit cards, debit cards, UPI, and other available online payment methods."
    },
    {
        "questions": [
            "How long does delivery take?",
            "When will my order arrive?",
            "How many days does delivery take?",
            "When will I receive my order?",
            "What is the delivery time?",
            "How long will my package take?"
        ],
        "answer": "Standard delivery usually takes 3 to 7 business days."
    },
    {
        "questions": [
            "Can I change my delivery address?",
            "How can I change my address?",
            "I entered the wrong address.",
            "Can I update my delivery address?",
            "How do I change my shipping address?"
        ],
        "answer": "You can change your delivery address before your order is shipped."
    },
    {
        "questions": [
            "How can I contact customer support?",
            "How do I contact support?",
            "Where can I contact customer service?",
            "I need customer support.",
            "How can I get help?"
        ],
        "answer": "You can contact customer support through the Help or Contact Us section."
    },
    {
        "questions": [
            "Do you offer cash on delivery?",
            "Is cash on delivery available?",
            "Can I pay cash when my order arrives?",
            "Do you have COD?",
            "Can I use cash on delivery?"
        ],
        "answer": "Cash on delivery is available for eligible products and locations."
    }
]


# Text preprocessing
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# Create a list containing all FAQ variations
all_questions = []
faq_indexes = []

for index, faq in enumerate(faqs):
    for question in faq["questions"]:
        all_questions.append(preprocess_text(question))
        faq_indexes.append(index)


# Convert questions into TF-IDF vectors
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    stop_words="english"
)

faq_vectors = vectorizer.fit_transform(all_questions)


# Get chatbot response
def get_response(user_question):

    user_question = preprocess_text(user_question)

    if not user_question:
        return "Please enter a question."

    user_vector = vectorizer.transform([user_question])

    similarities = cosine_similarity(user_vector, faq_vectors)

    best_match_index = similarities.argmax()
    best_score = similarities[0][best_match_index]

    matched_faq_index = faq_indexes[best_match_index]

    # Confidence threshold
    if best_score < 0.15:
        return (
            "Sorry, I don't have an answer for that question. "
            "Please ask about orders, returns, payments, delivery, "
            "address changes, or customer support."
        )

    return faqs[matched_faq_index]["answer"]


# Run chatbot
if __name__ == "__main__":

    print("\n===================================")
    print("      E-COMMERCE FAQ CHATBOT")
    print("===================================")
    print("Type 'exit' to stop the chatbot.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower().strip() == "exit":
            print("Chatbot: Goodbye!")
            break

        response = get_response(user_input)

        print("Chatbot:", response)