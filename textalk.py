import streamlit as st
from gtts import gTTS
from io import BytesIO
import os

def main():
    st.title('Text to speech')
    text = st.text_area("Enter your text here...")
    if st.button('Generate speech'):
        if text:
            tts = gTTS(text=text, lang='en')
            temp_file = 'temp_audio.mp3'
            tts.save(temp_file)
            with open(temp_file, 'rb') as f:
                audio_bytes = BytesIO(f.read())
            st.audio(audio_bytes, format='audio/mp3')
            os.remove(temp_file)
        else:
            st.error("Please enter text")

if __name__ == '__main__':
    main()      