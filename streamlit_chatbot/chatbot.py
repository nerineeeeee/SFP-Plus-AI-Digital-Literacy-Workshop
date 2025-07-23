
import streamlit as st
import pandas as pd

# Set page title
st.title("Yeppuda AI")

# Add header
st.header("🌸💗 Annyeong! Welcome to ✨ Yeppuda AI ✨ 💗🌸")

# Add text
st.write("This is a simple demonstration of Yeppuda AI capabilities")

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
def get_skincare_response(user_input):
    user_input = user_input.lower()

    if "dry" in user_input:
        return "You mentioned dry skin 🌵! I recommend using a hydrating toner and a moisturizer with hyaluronic acid 💧."
    elif "oily" in user_input:
        return "Oily skin? 🍟 Let’s keep that shine under control! Try a lightweight gel cleanser and a niacinamide serum 💦."
    elif "acne" in user_input:
        return "Acne problems? 😣 Use products with salicylic acid or Centella Asiatica to calm your skin 🌿."
    elif "routine" in user_input:
        return "A basic K-beauty routine includes: Cleanser → Toner → Essence → Serum → Moisturizer → SPF (daytime only!) ☀️"
    else:
        return "Yeppuda AI is here to help! 💗 Tell me your skin concerns or what you’re looking for."

def main():
    st.title("✨ Yeppuda AI - Your Korean Skincare Bestie ✨")
    st.caption("Ask me anything about skincare! 💆‍♀️🧴")

    initialize_session_state()

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

if prompt := st.chat_input("What's your skin concern today?"):
        # Show user message
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate bot response
        response = get_skincare_response(prompt)
        with st.chat_message("assistant"):
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()