import streamlit as st
from agent import ProductAgent

st.title("🛒 AI Product Recommendation Agent")

agent = ProductAgent()

st.subheader("Choose your preferences")

category = st.selectbox("Select a category", ["electronics", "fashion", "books"])

budget = st.number_input("Maximum Budget ($)", min_value=0, value=500)

rating = st.slider("Minimum Rating", 0.0, 5.0, 4.0)

if st.button("Get Recommendations"):
    results = agent.recommend(category, budget, rating)

    st.subheader("🧠 Recommended Products:")
    for item in results:
        if isinstance(item, str):
            st.error(item)
        else:
            st.write(f"**{item['name']}**")
            st.write(f"Price: ${item['price']}")
            st.write(f"Rating: ⭐ {item['rating']}")
            st.write("---")
