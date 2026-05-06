import speech_recognition as sr
import streamlit as st

st.title("Voice-to-Text Converter with Multiple Accents")

# Dropdown to select language/accent
language = st.selectbox(
    "Select language/accent",
    ["English (US)", "English (UK)", "English (India)", "Spanish", "French","Telugu"]
)

# Map to Google Speech Recognition language codes
lang_codes = {
    "English (US)": "en-US",
    "English (UK)": "en-GB",
    "English (India)": "en-IN",
    "Spanish": "es-ES",
    "French": "fr-FR",
    "Telugu": "te-IN"

}

selected_code = lang_codes[language]

# Initialize recognizer
r = sr.Recognizer()

# Option to use microphone or typed input
mode = st.radio("Choose input mode:", ["Speak", "Type"])

if mode == "Speak":
    st.write("Press 'Record' and speak into your microphone.")
    if st.button("Record"):
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = r.listen(source)
            st.write("Processing...")
        try:
            # Recognize speech with selected language/accent
            text = r.recognize_google(audio, language=selected_code)
            st.success(f"You said: {text}")
        except sr.UnknownValueError:
            st.error("Sorry, could not understand audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")

elif mode == "Type":
    user_input = st.text_input("Type something here:")
    if user_input:
        st.success(f"You typed: {user_input}")