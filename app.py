import streamlit as st
import google.generativeai as genai

# Set API key (Replace with your actual key)
genai.configure(api_key="AIzaSyAVJJlXyTJaOm2fJhtUme0pHtNcUgcp7iw")

# Function to get response from Gemini
def get_gemini_response(prompt):
    model = genai.GenerativeModel("Gemini 1.5 Pro")
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("NutriGen AI - Nutrition Assistant")
st.write("Get detailed nutritional info using Google Gemini AI")

food_item = st.text_input("Enter a food item:", "")

if st.button("Get Nutrition Info"):
    if food_item:
        prompt = f"Give me detailed nutritional info (calories, protein, carbs, fats) for {food_item}."
        response = get_gemini_response(prompt)
        st.write(response)
    else:
        st.warning("Please enter a food item!")
        
