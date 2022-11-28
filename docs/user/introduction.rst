Introducción
++++++++++++

En esta sección se dará un vistazo general al asistente virtual.

Funcionamiento
==============

Este asistente tiene habilidades de escucha, y ejecución de funciones específicas previamente programadas.

Funciona con reconocimiento de voz a través de un servicio de google, así que, se requiee conexión a internet para su correcto funcionamiento.
De lo contrario, el asistente no funcionará y arrojará errores de conexión.

Por defecto, el asistente se llama *'Sofía'*. Es por este nomebre por el que deben comenzar todos los comandos que se desea que el asistente ejecute.

.. note::
    En una versión posterior se planea tener la opción de personalizar el nombre del asistente.

Iniciando el asistente
======================

Para inicar el asistente, basta con abrir una ventana de terminal o command e ingresar el sisguiente comando:

.. code-block:: python

    python virtual_assistant.py

.. image:: /user/img/StartSofia.png

Una vez, el asistente esté corriendo, ajustará los parámetros de audio con el sonido ambiente del lugar y notificará cuando esté listo, con el mensaje ``OK. Esperando comandos...``

.. caution::

    El assitente usará el micrófono y salida de audio predeterminados por sistema. Estos se configuran en las preferencias de sistema de su sistema operativo.

.. caution::

    En cuanto a la cámara, el asistente siempre usará la primera cámara que esté por listado del sistema. Para mejor operación, asegúrese de tener conectada una sola cámara en su equipo.

Al iniciar, dará unas breves instrucciónes para obtener ayuda de los comandos y lo que puede hacer. En tal caso de querer escucharlo, puede decir ``Sofia, ayuda`` tal como se lo ha indicado, el asistente.

Comandos por voz
================

El sistente tratará de escuchar permanentemente su siguiente comando, que identificará cuando se le diga exactamente tal como se ha programado.
Para el detalle de cada uno de los comandos, púede referirise a las siguiente secciones:

#. :ref:`YouTubeCommand`
#. :ref:`DateTimeCommand`
#. :ref:`WikipediaCommand`
#. :ref:`GoogleCommand`
#. :ref:`EMailCommand`
#. :ref:`PictureCommand`
#. :ref:`HelpCommand`
#. :ref:`ShutdownCommand`
