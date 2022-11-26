import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import os
from virtual_asistant_utils import *


class VirtualAssistant:

    running: bool = False
    name: str = "Sofía"
    language: str = "es-CO"
    r = sr.Recognizer()
    speaker = pyttsx3.init()

    def __init__(self, running: bool = False):
        self.running = running
        self.runAssitant()

    def runAssitant(self):
        self.parametrize()
        while self.running:
            helper, command = self.listenForCommand()
            if command is None:
                continue
            results = self.executeCommand(helper, command)
            self.sendResponse(results)

    def listenForCommand(self):
        command = None
        while True:
            command = self.getAudio()
            if command is None:
                return None, None
            if command.lower().startswith("apagar"):
                self.shutdown()
                return None, None
            if command.lower().startswith("ayuda"):
                self.help()
                return None, None
            for _command in COMMANDS:
                if command.lower().startswith(_command["command"].lower()):
                    helper = _command["helper"]
                    return helper, command
            self.sendResponse("No te entendí, por favor repítelo.")

    def executeCommand(self, helper, command):
        return helper().execute(command)

    def sendResponse(self, message):
        print("Response:", message)
        if message is not None:
            self.speaker.say(message)
            self.speaker.runAndWait()

    def shutdown(self):
        self.running = False
        self.sendResponse("Hasta pronto!")

    def help(self):
        commands = [item["command"] for item in COMMANDS]
        commands.append("Apagar")
        commands.append("Ayuda")
        self.sendResponse(
            "Estos son los comandos que tengo programados: " +
            ", ".join(commands) +
            "... Todos los comandos deben comenzar por mi nombre, " +
            self.name)

    def getAudio(self):
        with sr.Microphone() as source:
            print("Esperando comandos...")
            audio = self.r.listen(source)
        try:
            print("Reconociendo audio...")
            audio_string: str = self.r.recognize_google(
                audio, language=self.language)
            print("OK Reconocí esto: " + audio_string)
        except sr.UnknownValueError:
            return None
            # self.sendResponse("No entendí lo que dijiste.")
            # self.sendResponse("Podrías por favor repetir?")
        except sr.RequestError as e:
            print(
                "No pude procesar tu solicitud {0}".format(e))
            return None
        if audio_string.lower().startswith(self.name.lower()):
            return audio_string[len(self.name):].strip()
        else:
            return None

    def parametrize(self):
        voices = self.speaker.getProperty('voices')
        selected_voice = voices[0]
        if len(voices) > 2:
            for voice in voices:
                if str(voice.name).count("Spanish") > 0:
                    selected_voice = voice
        elif len(voices) == 2:
            selected_voice = voices[1]
        self.speaker.setProperty('voice', selected_voice.id)
        self.sendResponse(
            "Ajustando parámetros de audio.")
        self.r.energy_threshold = 1000
        self.r.dynamic_energy_threshold = True
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            self.sendResponse("OK. Dí " +
                              self.name + " ayuda, para información de uso... Esperando comandos.")
            return
        self.sendResponse(
            "No pude configurar ningún micrófono. Por favor asegúrate de tener uno conectado.")


def main():
    va = None
    try:
        va = VirtualAssistant(True)
    except KeyboardInterrupt:
        print("Terminando aplicación.")


if __name__ == '__main__':
    main()
