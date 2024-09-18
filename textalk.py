import streamlit as st
from TTS.api import TTS
import soundfile as sf

tts = TTS(model_name='tts_models/en/ljspeech/tacotron2-DDC', progress_bar=True)
st.title('Text Talk')
st.write('Write your text here...')

text_input = st.text_area('Enter your text', value = 'Your text')
if st.button('Speak...'):
    if text_input.strip():
        with st.spinner('Generating audio...'):
            output_file = 'output.wav'
            TTS.tts_with_file(text_input, output_file)
            data, samplerate = sf.read(output_file)
            st.audio(output_file)
            st.success('Speech generated...')
    else:
        st.warning('Please enter text...')