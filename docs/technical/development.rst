Desarrollo del asistente virtual
++++++++++++++++++++++++++++++++

Como se ha comentado en otras partes, el asistente virtual está hecho con lenguaje de programación Python.
Está dividido en dos archivos:
* Archivo principal: En donde se encuentra la función de entrada de ejecución 'main' y la clase VirtualAssistant, que tiene la lógica del asistente virtual
* Archivo de utilidades: En donde se encuentran las clases auxiliares que ejecutan cada uno de los comandos.



.. _MainClass:

Clase principal (virtual_assistant.py)
======================================

Esta clase contiene la lógica de la aplicación y está subdividida en varios métodos.

Tiene propiedades modificables como ``name`` para almacenar el nombre del asistente y ``languaje`` para definir el lenguaje natural del aistente.
Otras propiedades definidas son de uso interno y no se deben modificar.

A continuación se explica en detalle cada uno de los métodos utilizados:



.. _initMethod:

Método __init__
---------------

Este método inicializa las propiedades de la clase que requieren ser inicializadas, ajusta parámetros de audio con :ref:`parametrize <parametrizeMethod>` y llama al método :ref:`runAssistant <runAssistantMethod>`.

.. code:: python

    def __init__(self, running: bool = False):
        self.running = running
        self.runAssitant()



.. _runAssistantMethod:

Método runAssistant
-------------------

Este método ejecuta el algoritmo que corre permanentemente la aplicación en un loop infinito que se rompera tan pronto se dé el comando de :ref:`apagar <shutdowncommand>`.
Dentro del loop, usa consecutivamente los métodos :ref:`listenForCommand <listenForCommandMethod>`, :ref:`executeCommand <executeCommandMethod>` y :ref:`sendResponse <sendResponseMethod>`.

.. code:: python

    def runAssitant(self):
        self.parametrize()
        while self.running:
            helper, command = self.listenForCommand()
            if command is None:
                continue
            results = self.executeCommand(helper, command)
            self.sendResponse(results)



.. _listenForCommandMethod:

Método listenForCommand
-----------------------

Este método tiene un loop infinito que permanentemente hace capturas de audio convertidas en texto, a través del método :ref:`getAudio <getAudioMethod>`, compara con el banco de instrucciones que tiene programadas y si coincide con alguna, devuelve una referencias del método que ejecuta dicha instrucción.
En caso contrario, devuelve un mensaje de error.

.. code:: python

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



.. _executeCommandMethod:

Método executeCommand
---------------------

Este método se encarga de ejecutar la clase utilitaria referenciada en :ref:`listenForCommand <listenForCommandMethod>`, con el comando detectado previamente en el mismo método.

.. code:: python

    def executeCommand(self, helper, command):
        return helper().execute(command)



.. _sendResponseMethod:

Método sendResponse
-------------------

Este método se encarga de recibir una cadena que usa para convertirla a audio y reproducirlo a través del parlante predefinido en el sistema operativo.

.. note::

    Usa la librería ``pyttsx3`` para la converisón de texto a audio y reproducir ese audio.

.. code:: python

    def sendResponse(self, message):
        print("Response:", message)
        if message is not None:
            self.speaker.say(message)
            self.speaker.runAndWait()



.. _getAudioMethod:

Método getAudio
---------------

Este método abre el micrófono para obtener audio que pueda detectar como instrucciones, las convierte a texto y verifica si la instrucción comienza por el nombre del asistente.
De no ser así, entiende que no es una instrucción que se impartió, por lo tanto desecha el audio y devuelve ``None``.
Si encuentra algún error en medio del reconocimiento, muestra el error y devuelve ``None``, para que el programa sigua su curso normal.

.. note::

    Usa la librería ``speech_recognition`` para la detección de audio y conversión de ese audio a texto.
    Para esto último se predifinió el uso de Google *Speech Recognition API*, usando los servicios en línea de reconociimento de voz de Google.

.. code:: python

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



.. _shutdownMethod:

Método shutdown
---------------

Este método termina la aplicación, poniendo la variable interna ``running`` en estado ``False``.

.. code:: python

    def shutdown(self):
        self.running = False
        self.sendResponse("Hasta pronto!")



.. _helpMethod:

Método help
-----------

Este método simplemente arma una frase con los comandos que tiene programados y los dice haciendo uso del método :ref:`sendResponse <sendResponseMethod>`.

.. code:: python

    def help(self):
        commands = [item["command"] for item in COMMANDS]
        commands.append("Apagar")
        commands.append("Ayuda")
        self.sendResponse(
            "Estos son los comandos que tengo programados: " +
            ", ".join(commands) +
            "... Todos los comandos deben comenzar por mi nombre, " +
            self.name)



.. _parametrizeMethod:

Método parametrize
------------------

Este método ajusta algunas propiedades iniciales, así:

Busca la segunda voz en español que tiene el sistema instalado y la selecciona para ser usada a la largo del programa.
La segunda voz es la voz de mujer de la versión en español.
Si no encuentra una voz en español, entonces trata de usar la segunda voz instalada en el sistema, que es la voz de mujer del lenguaje instlado.
Si no la encuentra, usa la primera voz encontrada, se de hombre o de mujer.

Ajusta niveles de toma de audio tales como ruido ambiente, umbrales de los registros de voz, entre otros.

.. code:: python

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




.. _HelperClasses:

Clases de Ayuda (virtual_assistant_utils.py)
===============================================

.. note::
    Todas las clases de ayuda '*helpers*' usan la librería ``parse``, la cual ayuda en la separación del comando y los parámetros a ejecutar para cada comando.



.. _YoutubeHelperClass:

Clase _YoutubeHelper
--------------------

Esta clase detecta las palabras que se han dicho como parámetros del comando y abre una página de YouTube con la búsqueda usando dichos parámtros y usando el navegador predefinido en el sistema operativo.

.. code:: python

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



.. _TimeHelperClass:

Clase TimeHelper
----------------

Esta clase simplemente arma una frase usando la hora actual del reloj interno del computador y la devuelve en una cadena (*string*).
Se puede adecuar fácilmente para que incluya el año y el mes y devuelva la fecha completamente junto a la hora.
Solo basta con quitar el comentario y en las dos líneas y comentar la línea inmediatamente posterior.

.. code:: python

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



.. _WikipediaHelperClass:

Clase WikipediaHelper
---------------------

Esta clase detecta las palabras que se han dicho como parámetros del comando y abre una página de Wikipedia con la búsqueda, usando dichos parámtros y usando el navegador predefinido en el sistema operativo.
Por defecto Wikipedia envía directamente al resultado en caso de encontrar un solo, de lo contrario muestra la página de desambiguación.

.. code:: python

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



.. _GoogleHelperClass:

Clase GoogleHelper
------------------

Esta clase detecta las palabras que se han dicho como parámetros del comando y abre una página de Google con la búsqueda, usando dichos parámtros y usando el navegador predefinido en el sistema operativo.
En caso de no haber mencionado ningún parámetro, solamente abre la página principal de Google, para iniciar un búsqueda.

.. code:: python

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



.. _MailHelperClass:

Clase MailHelper
----------------

Esta clase detecta las palabras que se han dicho como parámetros y usa la aplicación que se tiene por defecto como gestor de correos para redactar un nuevo correo con el destinatario, asunto y mensaje proporcionados en el comando.

.. code:: python

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



.. _PictureHelperClass:

Clase PictureHelper
-------------------

Esta clase usa la primera webcam que se tiene conectada al sistema, trata de tomar una foto y la guarda en la carpeta del programa bajo el nombre ``picture.png``.

.. code:: python

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



