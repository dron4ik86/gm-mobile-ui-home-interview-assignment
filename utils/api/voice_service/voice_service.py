from utils.api.request_headers import build_requests_headers
import requests
from logging_config import log


class VoiceService:
    """
    This class handles operations related to the voice service.
    """
    def __init__(self):
        self.voice = "/Voice"

    def save_audio_file(self, base_url, access_token):
        """
        This method sends a GET request to download an audio file.
        Open a file in binary write mode to save the audio file.
        Write the content of the response to the file in chunks
        stream=True, parameter ensures that the response content is downloaded in chunks, which is useful for large files
        """
        log.info(f"save_audio_file")
        file_path = "interactions/voice_interactions/audio_files/car_temperature.wav"
        request_headers = build_requests_headers(access_token)
        response = requests.get(f"{base_url}{self.voice}", headers=request_headers, stream=True)
        log.info(f"Voice Response: {response}")
        if response.status_code == 200:
            with open(file_path, 'wb') as audio_file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        audio_file.write(chunk)

        return file_path
