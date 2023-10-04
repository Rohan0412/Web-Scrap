""" 
to start the server run:
        uvicorn api:app --reload 
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from textblob import TextBlob

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-sentiment")
def get_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    label = ""
    if sentiment_score > 0.1:
        label = "POSITVE"
    elif sentiment_score < -0.1:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"

    return {"Sentiment": label, "Polarity": blob.sentiment.polarity, "Subjectivity": blob.sentiment.subjectivity}

if __name__ == "__main__":
    app.run(debug=True, port=8000)
