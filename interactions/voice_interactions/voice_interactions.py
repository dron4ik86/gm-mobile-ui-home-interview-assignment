import speech_recognition as sr

recognizer = sr.Recognizer()


def recognize_speech_from_audio_file(audio_files_path):
    """
    Recognizes and transcribes speech from an audio file using the Google Web Speech API.
    """
    with sr.AudioFile(audio_files_path) as source:
        audio_data = recognizer.record(source)  # Listen to the audio
        try:
            text = recognizer.recognize_google(audio_data)  # Recognize the speech using Google Web Speech API
            return text
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
