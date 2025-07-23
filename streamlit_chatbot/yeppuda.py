import streamlit as st
import google.generativeai as genai
import os
GOOGLE_API_KEY = "AIzaSyDEvnIf0aI2TSY1azxKPA8yjXDSMsR2WvI"

# --- Configuration for Yeppuda AI ---
# Set the page title and icon for your Streamlit app
st.set_page_config(
    page_title="💖 Yeppuda AI Skincare Advisor 💖",
    page_icon="✨", # A cute sparkle icon!
    layout="centered" # Keep it neat and centered
)

# --- API Key Setup ---
# It's super important to keep your API key safe!
# Streamlit secrets are the best way to do this.
# Make sure you have a .streamlit/secrets.toml file in your project
# with a line like: GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
# If running locally, you can also set it as an environment variable.
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except KeyError:
    # Fallback to environment variable if not found in secrets.toml
    api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("Oopsie! 🥺 It looks like your Google API key isn't set up yet!")
    st.error("Please add it to your Streamlit secrets.toml file or as an environment variable.")
    st.info("You can get your API key from Google AI Studio: https://aistudio.google.com/app/apikey")
    st.stop() # Stop the app if no API key is found

# Configure the generative AI model with your API key
genai.configure(api_key="AIzaSyDEvnIf0aI2TSY1azxKPA8yjXDSMsR2WvI")

# Initialize the Generative Model
# We're using 'gemini-pro' for text generation, it's super smart!
model = genai.GenerativeModel('gemini-2.5-flash')

# --- Yeppuda AI's Cutesy Interface ---

# Title and a warm, cutesy welcome!
st.markdown(
    """
    <div style="text-align: center;">
        <h1>💖 Welcome to Yeppuda AI! 💖</h1>
        <p style="font-size: 1.2em;">
            Your ultimate cutesy skincare bestie is here to help you glow! ✨
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Placeholder image for the banner. You can replace this with a real image URL if you have one!
st.image("https://placehold.co/600x200/FFC0CB/FFFFFF?text=Yeppuda+AI+Banner", caption="Yeppuda AI is ready to help you shine!", use_column_width=True)


st.markdown("---") # A little separator for neatness

# --- User Input Area ---
st.subheader("Tell Yeppuda AI about your skin concerns! 🌸")
user_concern = st.text_area(
    "What's bothering your lovely skin today? (e.g., 'I have oily skin and breakouts,' 'My skin feels dry and dull,' 'I'm looking for anti-aging tips')",
    height=150,
    placeholder="Share your skin secrets here, bestie! I'm all ears! 👂"
)

# --- Generate Advice Button ---
if st.button("Get Skincare Advice from Yeppuda AI! ✨"):
    if user_concern:
        with st.spinner("Yeppuda AI is thinking super hard to give you the best advice... 💭"):
            try:
                # Crafting the perfect prompt for our cutesy advisor!
                prompt = f"""
                You are Yeppuda AI, a super cutesy, friendly, and helpful skincare advisor.
                Your goal is to provide gentle, encouraging, and effective skincare advice.
                Always use a sweet, positive, and slightly playful tone, incorporating emojis.
                Keep your suggestions practical and easy to understand.
                **Please keep your answers concise and to the point, around 2-3 sentences max per suggestion.**
                If the user's concern is vague, ask for more details politely.

                Here's the user's skin concern: "{user_concern}"

                Based on this, please give me some lovely skincare suggestions and tips!
                Start with a cutesy greeting like "Oh, my sweet friend!" or "Hello, lovely!"
                """

                # Generate content using the Gemini Pro model
                response = model.generate_content(prompt)

                # Display the generated advice
                st.markdown("---")
                st.subheader("💖 Yeppuda AI's Skincare Wisdom for You! 💖")
                st.write(response.text)
                st.markdown(
                    """
                    <p style="font-size: 0.9em; text-align: center; margin-top: 20px;">
                        Remember, consistency is key to glowing skin! Keep shining! ✨
                    </p>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.error(f"Oh no! 😭 Something went wrong while Yeppuda AI was trying to help: {e}")
                st.info("Please try again or recheck your API key and internet connection!")
    else:
        st.warning("Hehe, you forgot to tell me your skin concerns, bestie! Please type something in first! �")

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <p style="text-align: center; font-size: 0.8em; color: gray;">
        Made with love by your AI Bestie 💖
    </p>
    """,
    unsafe_allow_html=True
)
