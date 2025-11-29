Product Recommendation AI Agent
An intelligent Streamlit app that recommends products based on user preferences using rule-based and AI-driven logic.
<p align="center"> <img src="https://dummyimage.com/900x200/0a66c2/ffffff&text=Product+Recommendation+AI+Agent" /> </p>
⭐ Badges
<p align="left"> <img src="https://img.shields.io/badge/Python-3.10+-blue" /> <img src="https://img.shields.io/badge/Streamlit-1.0+-brightgreen" /> <img src="https://img.shields.io/badge/Status-Active-success" /> <img src="https://img.shields.io/badge/License-MIT-lightgrey" /> </p>
📌 Project Overview

The Product Recommendation AI Agent is a smart system built with Streamlit that analyzes user preferences and recommends products in real-time.

It uses:

🎯 User preference matching

🧠 Rule-based filtering

⚙️ Modular agent architecture

💾 JSON-based preference storage

⚡ Fast, interactive UI built with Streamlit

Perfect for e-commerce demos, AI agent portfolios, or internship projects.

🧩 Features

✔ Select from multiple preference categories

✔ Get instant product recommendations

✔ Clean & simple user interface

✔ Fully customizable JSON data

✔ Easy to deploy anywhere (GitHub, Streamlit Cloud, etc.)


📁 Project Structure
product-recommendation-agent/
│── app.py
│── agent.py
│── preferences.json
│── requirements.txt
│── README.md

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/product-recommendation-agent
cd product-recommendation-agent

2. Install dependencies
pip install -r requirements.txt

3. Run Streamlit
streamlit run app.py

🧠 How It Works
1. User selects preferences

Price range

Brand

Category

Style

Color

2. Agent processes input

The agent matches the selected preferences with the dataset stored in preferences.json.

3. App displays recommendations

A list of most relevant items is shown with descriptions and reasons for suggestion.

🔧 Customization
Modify product database

Simply edit the preferences.json file:

{
  "products": [
    {
      "name": "Wireless Headphones Pro",
      "category": "electronics",
      "price_range": "mid",
      "brand": "SoundMax",
      "style": "modern"
    }
  ]
}

📝 Future Improvements

🤖 AI-powered NLP recommendations

🔍 Search bar + product filters

⭐ User rating system

🛒 Add-to-cart simulation

🚚 Shipping / delivery estimation

📸 Screenshots

Place your images in a screenshots/ folder then reference like:

![Home Screen](screenshots/home.png)
![Preferences Page](screenshots/preferences.png)
![Recommendations](screenshots/recommendations.png)

👨‍💻 Author

Sinchana M
💼 AI Developer | ML Enthusiast
📧 (optional: add your email)
🌐 (optional: portfolio link)

📄 License

This project is licensed under the MIT License.
