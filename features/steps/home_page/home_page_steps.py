from behave import step
from pages.home.home_page import HomePage
from utils.api.voice_service.voice_service import VoiceService
import config as cfg
from interactions.voice_interactions.voice_interactions import recognize_speech_from_audio_file


@step("The user is on the home page")
def search_for_phone_icon(context):
    result = HomePage(context.driver).search_for_phone_icon()
    assert result is True, "Phone icon not found on the home page."


@step("The user enters {temperature} in the temperature text box")
def user_change_the_temperature(context, temperature):
    HomePage(context).user_change_the_temperature()


@step("The temperature should be updated to {temperature}")
def validate_temperature_on_home_page(context, temperature):
    result = HomePage(context.driver).get_text_from_temperature_widget()
    assert result == temperature, "Expected temperature to be {temperature}, but got {result}"


@step("Sending the API request to get the audio file")
def get_audio_file(context):
    context.audio_file_path = VoiceService().save_audio_file(cfg.BASE_URL, context.access_token)


@step("The audio file should contain the {temperature}")
def convert_audio_to_text(context, temperature):
    audio_files_path = "interactions/voice_interactions/audio_files/car_temperature.wav"
    text_from_audio_file = recognize_speech_from_audio_file(audio_files_path)
    assert temperature in text_from_audio_file, \
        f"Temperature {temperature} not found in the audio text. The text is '{text_from_audio_file}'"
