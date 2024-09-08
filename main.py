import streamlit as st
import whisper
from pydub import AudioSegment
import os
from audio_recorder_streamlit import audio_recorder

# Load the Whisper model
model = whisper.load_model("small")

# Function to save recorded audio
def save_audio(audio_data, file_name):
    file_path = f"audio_files/{file_name}"
    
    # Ensure the directory exists
    if not os.path.exists("audio_files"):
        os.makedirs("audio_files")
        
    with open(file_path, "wb") as f:
        f.write(audio_data)
    return file_path

# Streamlit UI
st.title("Whisper AI Transcription (Indonesian)")
st.write("Klik tombol di bawah untuk mulai merekam audio:")

# Record audio
audio_data = audio_recorder()

if audio_data:
    # Save and process audio file
    audio_path = save_audio(audio_data, "recorded_audio.wav")

    # Convert audio to wav format if needed
    if audio_path.endswith(".mp3") or audio_path.endswith(".m4a"):
        sound = AudioSegment.from_file(audio_path)
        audio_path = audio_path.replace(os.path.splitext(audio_path)[1], ".wav")
        sound.export(audio_path, format="wav")

    # Run Whisper model with forced Indonesian language
    st.write("Transkripsi audio...")
    result = model.transcribe(audio_path)
    st.write("Transkripsi:")
    st.text(result["text"])
