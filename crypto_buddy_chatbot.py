
# CryptoBuddy - Simple AI Chatbot for Crypto Advice

crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8  
    }  
}

def chatbot_response(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 Invest in {recommend}! It’s eco-friendly and has long-term potential!"

    elif "trending" in user_query or "growth" in user_query or "long-term" in user_query:
        trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        if trending:
            return f"🚀 Consider investing in {trending[0]}! It’s on the rise with a strong market cap!"
        else:
            return "📊 No high market cap cryptos are trending up right now."

    else:
        return "🤖 I’m CryptoBuddy! Ask me about trends, sustainability, or what’s hot in the crypto world!"

# Sample interactions
print(chatbot_response("Which crypto should I buy for long-term growth?"))
print(chatbot_response("What’s the most sustainable coin?"))
