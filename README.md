# Whisper-AI-for-Bahasa-Indonesia
Implementing Whisper model for transcription Indonesia Language

# Streamlit APP
Here the link for testing streamlit app
```
https://whisper-zein.streamlit.app/
```
# Instalation
1. Clone or download this repository
2. Unzip the file
3. Build docker container
```
docker buildx build -t whisper-streamlit-app .
```
4. Run docker container
```
docker run -p 8501:8501 whisper-streamlit-app
```