##############################################################################
Chapter Light Sensor
##############################################################################

In this chapter, we will learn the micro:bit built-in light sensor and photoresistor.

Project Built-in Light Sensor
********************************************

In this project, we use the micro:bit built-in light sensor to measure the brightness of light.

Component list
==============================

.. list-table:: 
   :width: 100%
   :align: center

   * -  Microbit x1
     -  USB cable x1
   * -  |Chapter03_00|
     -  |Chapter03_03|

.. |Chapter03_00| image:: ../_static/imgs/3_LED/Chapter03_00.png
.. |Chapter03_03| image:: ../_static/imgs/3_LED/Chapter03_03.png

Component knowledge
===============================

Light sensor
---------------------------------

Micro:bit detects the ambient light intensity through the LED matrix. In forward bias mode, the LED screen works as a display. In reverse bias mode, the LED screen works as a basic light sensor that can be used to detect ambient light.

.. image:: ../_static/imgs/15_Light_Sensor/Chapter15_00.png
    :align: center

Circuit
=============================

Connect micro:bit and PC via a micro USB cable.

Hardware connection

.. image:: ../_static/imgs/15_Light_Sensor/Chapter15_01.png
    :align: center

Block code 
===============================

Open MakeCode first. Import the .hex file. The path is as below:

( :ref:`How to import project <import_project>` )

+-----------+------------------------------------------------+-------------------------+
| File type | Path                                           | File name               |
+-----------+------------------------------------------------+-------------------------+
| HEX file  | ../Projects/BlockCode/15.1_LightIntensityMeter | LightIntensityMeter.hex |
+-----------+------------------------------------------------+-------------------------+

After importing successfully, the code is shown as below:

.. image:: ../_static/imgs/15_Light_Sensor/Chapter15_02.png
    :align: center

Check the connection of the circuit, verify it correct and download the code into the micro:bit. Open the serial port console, then you can see the reading light intensity. Cover the LED screen with your hand or increase the light shining on it, you can see the change in value, the range of values is 0-255, 0 is dark, 255 is the brightest, as shown below.

.. image:: ../_static/imgs/15_Light_Sensor/Chapter15_03.png
    :align: center

Reference
------------------------------

.. list-table:: 
   :width: 100%
   :align: center

   * -  Block
     -  Function 
   
   * -  |Chapter15_04|
     -  Detect the light level (how bright or dark it is) of the environment where you are. The light level 0 means darkness and 255 means bright light.

.. |Chapter15_04| image:: ../_static/imgs/15_Light_Sensor/Chapter15_04.png

Python code
==============================

Open the .py file with Mu. Code, the path is as below:

+-------------+-------------------------------------------------+------------------------+
| File type   | Path                                            | File name              |
+-------------+-------------------------------------------------+------------------------+
| Python file | ../Projects/PythonCode/15.1_LightIntensityMeter | LightIntensityMeter.py |
+-------------+-------------------------------------------------+------------------------+

After loading successfully, the code is shown as below:

.. image:: ../_static/imgs/15_Light_Sensor/Chapter15_05.png
    :align: center

Check the connection of the circuit, verify it correct, download the code into the micro:bit. Open the serial port console, then you can see the reading light intensity. Cover the LED screen with your hand or increase the light shining on it, you can see the change in value, the range of values is 0-255, 0 is dark, 255 is the brightest, as shown below.】

.. image:: ../_static/imgs/15_Light_Sensor/Chapter15_06.png
    :align: center

.. image:: ../_static/imgs/15_Light_Sensor/Chapter15_07.png
    :align: center

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Projects/PythonCode/15.1_LightIntensityMeter/LightIntensityMeter.py
    :linenos: 
    :language: python
    :lines: 1-4
    :dedent:

Reference
-----------------------

.. py:function:: display.read_light_level()	

    Use the display's LEDs in reverse-bias mode to sense the amount of light falling on the display, return an integer between 0 and 255 representing the light level. The larger the value, the brighter the light..

.. include:: 15.2_Light_Sensor.rst