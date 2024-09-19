import streamlit as st
import gtts as gTTS
from io import BytesIO

def main():
    st.title('Text to speech')
    text = st.text_area("Enter your text here...")
    if st.button('Generate speech'):
        if text:
            tts = gTTS(text=text, lang='en')
            audio_bytes = BytesIO
            tts.writ_to_fp(audio_bytes)
            audio_bytes.seek(0)
            st.audio(audio_bytes, format='audio/mp3')
        else:
            st.error("Please enter text")           