Commandos
+++++++++

Estos son los comandos que tiene programados el asistente virtual:

.. _YouTubeCommand:

Comando para YouTube
====================

Este comando abre la página de YouTube buscando el video que se ha especificado.

Para ejecutarlo, debe decir ``Sofia, pon en YoutTube <Palabras Clave>`` y en seguida las plabras clave con las que se quiere obtener resultados.

Ejemplo:

.. code::

    Sofia, pon en YouTube Carlos Vives Cumbiana

.. image:: /user/img/YouTubeCommand.png


.. _DateTimeCommand:

Comando para saber la hora
==========================

Este comando responde con la hora actual. Toma la hora del computador y la devuelve por voz.

Para ejecutarlo, debe decir ``Sofia, qué hora es``.

Ejemplo:

.. code::

    Sofia, qué hora es

.. image:: /user/img/DateTimeCommand.png


.. _WikipediaCommand:

Comando para buscar algo en Wikipedia
=====================================

Este comando abre la página de Wikipedia con el resultado de la búsqueda, según la o las palabras que se le han especificado.

Para ejecutarlo, debe decir ``Sofia, busca en Wikipedia <Palabras Clave>`` y en seguida las plabras clave con las que se quiere obtener resultados.

Ejemplo:

.. code::

    Sofia, busca en Wikipedia Bastardos Sin Gloria

.. image:: /user/img/WikipediaCommand.png


.. _GoogleCommand:

Comando para buscar algo o abrir google
=======================================

Este comando abre la página de Google y como opciona, muestra el resultado de la búsqueda, según la o las palabras que se le han especificado.
Si no ha incluido ningún parámetro de búsqueda, el asistente simpelmente abre la página principal de google.

Para ejecutarlo, debe decir ``Sofia, abre Google [Palabras Clave]`` y en seguida las plabras clave con las que se quiere obtener resultados.

Ejemplo 1:

.. code::

    Sofia, abre Google

Ejemplo 2:

.. code::

    Sofia, abre Google Trainspotting

.. image:: /user/img/GoogleCommand.png


.. _EMailCommand:

Comando para enviar correo electrónico
======================================

Este comando usa el gestor de correo electrónico que está configurado por defecto en el sistema y crea un uevo correo con los parámetros que se le ingresaron.
Los parámetros para incluir son **Dirección destino**, **Asunto** y **Mensaje**

Para ejecutarlo, debe decir ``Sofia, redacta correo electrónico a <Dirección Destino> con asunto <Asunto> y mensaje <Mensaje>``.

Ejemplo:

.. code::

    Sofia, redacta correo electrónico a john.cruz@ustadistancia.edu.co con asunto prueba de correo y mensaje probando el asistente virtual para redacción de correo electrónico

.. image:: /user/img/EMailCommand.png


.. _PictureCommand:

Comando para tomar una foto
===========================

Este comando accede a la cámara web que el equipo debe tener conectada, toma una foto y la guarda en la misma carpeta donde reside el programa bajo el nombre `picture.png`

.. danger::
    El asistente usará la primera cámara que encuentre conectada al equipo. En caso de no existir cámara, arrojará un error descriptivo.

Para ejecutarlo, debe decir ``Sofia, tómame una foto``.

Ejemplo:

.. code::

    Sofia, tómame una foto

.. image:: /user/img/YouTubeCommand.png


.. _HelpCommand:

Comando para obtener ayuda
==========================

Este comando responderá con una ayuda general de los comandos que tiene programados el asistente virtual.

Para ejecutarlo, debe decir ``Sofia, ayuda``.

Ejemplo:

.. code::

    Sofia, ayuda

.. image:: /user/img/HelpCommand.png


.. _ShutdownCommand:

Comando para salir
==================

Este comando terminará el programa del asistente virtual.

Para ejecutarlo, debe decir ``Sofia, apagar``.

Ejemplo:

.. code::

    Sofia, apagar

.. image:: /user/img/ShutdownCommand.png
