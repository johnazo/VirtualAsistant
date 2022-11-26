import webbrowser
from datetime import datetime
import cv2 as cv
import parse


class YoutubeHelper:
    format_string = "Pon en YouTube {}"

    def execute(self, command: str = None):
        if command is None:
            return None
        parsed_command = parse.parse(self.format_string, command)
        if parsed_command is None:
            return None
        search_url = "https://www.youtube.com/results?search_query=" + \
            "+".join(parsed_command[0].split())
        webbrowser.open(search_url, new=0, autoraise=True)
        return "Poniendo en YouTube " + parsed_command[0]


class TimeHelper:
    format_string = "Qué hora es"

    months = ("Enero", "Febrero", "Marzo", "Abril",
              "Mayo", "Junio", "Julio", "Agosto",
              "Septiembre", "Octubre", "Noviembre", "Diciembre")

    def execute(self, command):
        now = datetime.now()
        second = now.second
        minute = now.minute
        hour = now.hour
        day = now.day
        month = now.month
        year = now.year
        ampm = now.strftime("%p")
        hour_expression1 = "Es la " if hour == 1 else "Son las "
        # format_string = (hour_expression1 + "{} y {} {} del {} de {} de {}").format(
        #     hour, minute, ampm, day, self.months[now.month-1], year)
        format_string = (hour_expression1 + "{} y {} {}").format(
            hour, minute, ampm)
        return format_string


class WikipediaHelper:
    format_string = "Busca en Wikipedia {}"

    def execute(self, command):
        if command is None:
            return None
        parsed_command = parse.parse(self.format_string, command)
        if parsed_command is None:
            return None
        search_url = "https://en.wikipedia.org/wiki/Special:Search?search=" + \
            "+".join(parsed_command[0].split())
        webbrowser.open(search_url, new=0, autoraise=True)
        return "Buscando en Wikipedia " + parsed_command[0]


class GoogleHelper:
    format_string = "Abre Google {}"

    def execute(self, command):
        if command is None:
            return None
        parsed_command = parse.parse(self.format_string, command)
        url = "https://www.google.com/search?q="
        if parsed_command is not None:
            url = url + "+".join(parsed_command[0].split())
            message_string = "Buscando en Google " + parsed_command[0]
        else:
            message_string = "Abriendo Google"
        webbrowser.open(url, new=0, autoraise=True)
        return message_string


class MailHelper:
    format_string = "Redacta correo electrónico a {} con asunto {} y mensaje {}"

    def execute(self, command=None):
        if command is None:
            return None
        parsed_command: str = parse.parse(self.format_string, command)
        if parsed_command is None:
            return None
        mail_address = parsed_command[0].replace(
            " arroba ", "@").replace(" ", "")
        mail_link = "mailto:{}?subject={}&body={}".format(
            mail_address, parsed_command[1], parsed_command[2])
        webbrowser.open(mail_link, new=0, autoraise=True)
        return "Redactando correo."


class PictureHelper:
    format_string = "Tómame una foto"
    camera_port = 0

    def execute(self, command):
        camera = cv.VideoCapture(self.camera_port)
        result, image = camera.read()

        if result:
            cv.imwrite("picture.png", image)
        else:
            return "No se detectó imagen. Por favor intente de nuevo"
        return "Foto Tomada y guardada."


COMMANDS = [
    {"command": "Pon en YouTube",
        "helper": YoutubeHelper},
    {"command": "Qué hora es",
        "helper": TimeHelper},
    {"command": "Busca en Wikipedia",
        "helper": WikipediaHelper},
    {"command": "Abre Google",
        "helper": GoogleHelper},
    {"command": "Redacta correo electrónico",
        "helper": MailHelper},
    {"command": "Tómame una foto",
        "helper": PictureHelper}
]
