from typing import Any, List, Union

import speech_recognition as sr
from flask import Blueprint, request

CENTER = "centre"

audio_bp = Blueprint("audio", __name__, url_prefix="/audio")

recognizer = (
    sr.Recognizer()
)  # using the recognizer class from the speech_recognition module (google speech recognition)


def get_text_from_audio(temp_filename) -> str:
    """Function to get text from audio file."""
    audio_file = sr.AudioFile(temp_filename)

    try:
        with audio_file as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Failed to recognize the audio"


def text_to_command(text: str) -> Union[List[str], List[Any], None]:
    """Function to convert text to command.
    Supported commands:
        - top left
        - top center
        - top right
        - center left
        - center
        - center right
        - bottom left
        - bottom center
        - bottom right

    :param text: text, as transcribed from the audio
    :return: command as form of list of string
    """
    text = text.lower()
    if " " in text:
        commands = text.split(" ")
        if len(commands) >= 2:
            if commands[0] in ["top", CENTER, "bottom"]:
                if commands[1] in ["left", CENTER, "right"]:
                    return commands[:2]
    else:
        commands = [text]
        if commands[0] == CENTER:
            return [CENTER]
    return []


def commands_to_coordinate(commands: List[str]):
    """Based on the command(s) given, return the coordinate(s) of the command(s).

    :param commands: list of string, containing the command(s)
    """
    if len(commands) == 1:
        if commands[0] == CENTER:
            return [1, 1]
    elif len(commands) == 2:
        if commands[0] == "top":
            if commands[1] == "left":
                return [0, 0]
            elif commands[1] == CENTER:
                return [0, 1]
            elif commands[1] == "right":
                return [0, 2]
        elif commands[0] == CENTER:
            if commands[1] == "left":
                return [1, 0]
            elif commands[1] == "right":
                return [1, 2]
        elif commands[0] == "bottom":
            if commands[1] == "left":
                return [2, 0]
            elif commands[1] == CENTER:
                return [2, 1]
            elif commands[1] == "right":
                return [2, 2]
    else:
        return []


@audio_bp.route("/process_audio", methods=["POST"])
def process_audio():
    temp_filename = "audio.wav"
    request.files["audio"].save(temp_filename)

    text = get_text_from_audio(temp_filename)
    # text = "top left"
    print()
    print(text)

    commands = text_to_command(text)

    print(commands)
    if commands:
        coordinates = commands_to_coordinate(commands)
        print(coordinates)
        if coordinates:
            pass
        else:
            # send error message
            return "Invalid command. Please try again.", 400
    else:
        # send error message
        return "Invalid command. Please try again.", 400

    return {"command": commands, "coordinates": coordinates}
