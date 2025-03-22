



Project Relay & Motor
************************************

In this project, we will control a relay to drive a motor.

Component list
===================================

+----------------------------+-----------------------------+
| Microbit x1                | Expansion board x1          |
|                            |                             |
| |Chapter03_00|             | |Chapter03_01|              |
+----------------------------+-----------------------------+
| Breakboard x1              | USB cable x1                |
|                            |                             |
| |Chapter03_02|             | |Chapter03_03|              |
+----------------------------+-----------------------------+
|NPN(8050)transistor x 1     | Motor x1                    |
|                            |                             |
| |Chapter21_06|             | |Chapter21_07|              |
+----------------------------+-----------------------------+
| Relay x1                   | LED x1                      |
|                            |                             |
| |Chapter21_08|             | |Chapter21_09|              |
+-----------------+----------+---------+-------------------+
| Diode x1        | 1kΩ x1             | 220Ω x1           |
|                 |                    |                   |
| |Chapter21_02|  |  |Chapter21_00|    |  |Chapter21_01|   |
+-----------------+--------------------+-------------------+
| Jumper  M/M x4  | Jumper  F/M x5     | Jumper  F/F x1    |
|                 |                    |                   |
| |Chapter21_03|  |  |Chapter21_04|    |  |Chapter21_05|   |
+-----------------+--------------------+-------------------+

.. |Chapter21_00| image:: ../_static/imgs/21_Motor/Chapter21_00.png
.. |Chapter21_01| image:: ../_static/imgs/21_Motor/Chapter21_01.png
.. |Chapter21_02| image:: ../_static/imgs/21_Motor/Chapter21_02.png
.. |Chapter21_03| image:: ../_static/imgs/21_Motor/Chapter21_03.png
.. |Chapter21_04| image:: ../_static/imgs/21_Motor/Chapter21_04.png
.. |Chapter21_05| image:: ../_static/imgs/21_Motor/Chapter21_05.png
.. |Chapter21_06| image:: ../_static/imgs/21_Motor/Chapter21_06.png
.. |Chapter21_07| image:: ../_static/imgs/21_Motor/Chapter21_07.png
.. |Chapter21_08| image:: ../_static/imgs/21_Motor/Chapter21_08.png
.. |Chapter21_09| image:: ../_static/imgs/21_Motor/Chapter21_09.png
.. |Chapter03_00| image:: ../_static/imgs/3_LED/Chapter03_00.png
.. |Chapter03_01| image:: ../_static/imgs/3_LED/Chapter03_01.png
.. |Chapter03_02| image:: ../_static/imgs/3_LED/Chapter03_02.png
.. |Chapter03_03| image:: ../_static/imgs/3_LED/Chapter03_03.png

Component knowledge
===============================

DC Motor
-------------------------------

DC Motor is a device that converts electrical energy into mechanical energy. DC Motors consist of two major parts, a Stator and the Rotor. The stationary part of a DC Motor is the Stator and the part that Rotates is the Rotor. The Stator is usually part of the outer case of motor (if it is simply a pair of permanent magnets), and it has terminals to connect to the power if it is made up of electromagnet coils. Most Hobby DC Motors only use Permanent Magnets for the Stator Field. The Rotor is usually the shaft of motor with 3 or more electromagnets connected to a commutator where the brushes (via the terminals 1 & 2 below) supply electrical power, which can drive other mechanical devices. The diagram below shows a small DC Motor with two terminal pins.

.. image:: ../_static/imgs/21_Motor/Chapter21_10.png
    :align: center

When a DC Motor is connected to a power supply, it will rotate in one direction. If you reverse the polarity of the power supply, the DC Motor will rotate in opposite direction. This is important to note.

.. image:: ../_static/imgs/21_Motor/Chapter21_11.png
    :align: center

Relay
------------------------

Relays are a type of Switch that open and close circuits electromechanically or electronically. Relays control one electrical circuit by opening and closing contacts in another circuit using an electromagnet to initiate the Switch action. When the electromagnet is energized (powered), it will attract internal contacts completing a circuit, which act as a Switch. Many times Relays are used to allow a low powered circuit (and a small low amperage switch) to safely turn ON a larger more powerful circuit. They are commonly found in automobiles, especially from the ignition to the starter motor.

The following is a basic diagram of a common relay and the image and circuit symbol diagram of the 5V relay used in this project:

.. list-table:: 
   :width: 100%
   :align: center

   * -  Diagram
     -  Feature
     -  Symbol 
   
   * -  |Chapter21_12|
     -  |Chapter21_13|
     -  |Chapter21_14|

.. |Chapter21_12| image:: ../_static/imgs/21_Motor/Chapter21_12.png
.. |Chapter21_13| image:: ../_static/imgs/21_Motor/Chapter21_13.png
.. |Chapter21_14| image:: ../_static/imgs/21_Motor/Chapter21_14.png

Pin 5 and pin 6 are internally connected to each other. When the coil pin3 and pin 4 are connected to a 5V power supply, pin 1 will be disconnected from pins 5 & 6 and pin 2 will be connected to pins 5 & 6. Pin 1 is called Closed End and pin 2 is called the Open End.

Inductor
---------------------

The symbol of Inductance is "L" and the unit of inductance is the "Henry" (H). Here is an example of how this can be encountered: 1H=1000mH, 1mH=1000μH.

An Inductor is a passive device that stores energy in its Magnetic Field and returns energy to the circuit whenever required. An Inductor is formed by a Cylindrical Core with many Turns of conducting wire (usually copper wire). Inductors will hinder the changing current passing through it. When the current passing through the Inductor increases, it will attempt to hinder the increasing movement of current; and when the current passing through the inductor decreases, it will attempt to hinder the decreasing movement of current. So the current passing through an Inductor is not transient.

.. image:: ../_static/imgs/21_Motor/Chapter21_15.png
    :align: center

The circuit for a Relay is as follows: The coil of Relay can be equivalent to an Inductor, when a Transistor is present in this coil circuit it can disconnect the power to the relay, the current in the Relay’s coil does not stop immediately, which affects the power supply adversely. To remedy this, diodes in parallel are placed on both ends of the Relay coil pins in opposite polar direction. Having the current pass through the diodes will avoid any adverse effect on the power supply.

.. image:: ../_static/imgs/21_Motor/Chapter21_16.png
    :align: center

Circuit
========================

.. list-table:: 
   :width: 100%
   :align: center

   * -  Schematic diagram
   * -  |Chapter21_17|
   * -  Hardware connection
   * -  |Chapter21_18|

.. |Chapter21_17| image:: ../_static/imgs/21_Motor/Chapter21_17.png
.. |Chapter21_18| image:: ../_static/imgs/21_Motor/Chapter21_18.png

Block code 
========================

Open MakeCode first. Import the .hex file. The path is as below:

( :ref:`How to import project <import_project>` )

+-----------+----------------------------------+-----------+
| File type | Path                             | File name |
+-----------+----------------------------------+-----------+
| HEX file  | ../Projects/BlockCode/21.1_Relay | Relay.hex |
+-----------+----------------------------------+-----------+

After importing successfully, the code is shown as below:

.. image:: ../_static/imgs/21_Motor/Chapter21_19.png
    :align: center

Check the connection of the circuit, verify it correct, and download the code into micro:bit. Press button A, then the motor starts to rotate. Release the button, then the motor stops.

It is to determine whether the button A is pressed. If pressed, P0 outputs a high level, the relay is turned on, and the motor is running; if it is not pressed, P0 outputs a low level, and the motor does not run.

.. image:: ../_static/imgs/21_Motor/Chapter21_20.png
    :align: center

Python code
==============================

Open the .py file with Mu. Code, the path is as below:

+-------------+-----------------------------------+-----------+
| File type   | Path                              | File name |
+-------------+-----------------------------------+-----------+
| Python file | ../Projects/PythonCode/21.1_Relay | Relay.py  |
+-------------+-----------------------------------+-----------+

After loading successfully, the code is shown as below:

.. image:: ../_static/imgs/21_Motor/Chapter21_21.png
    :align: center

Check the connection of the circuit, verify it correct, and download the code into micro:bit. Press button A, then the motor starts to rotate. Release the button, then the motor stops.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Projects/PythonCode/21.1_Relay/Relay.py
    :linenos: 
    :language: python
    :lines: 1-6
    :dedent:

If A is pressed, P0 outputs a high level, the relay is turned on, and the motor is running. If it is not pressed, P0 outputs a low level, and the motor does not run.

.. literalinclude:: ../../../freenove_Kit/Projects/PythonCode/21.1_Relay/Relay.py
    :linenos: 
    :language: python
    :lines: 3-6
    :dedent:
