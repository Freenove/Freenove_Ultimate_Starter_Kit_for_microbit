



Project Potentiometer & Motor
*******************************************

In this project, a rotary potentiometer is used to control a motor.

Component list
=============================

+----------------------------+-----------------------------+
| Microbit x1                | Expansion board x1          |
|                            |                             |
| |Chapter03_00|             | |Chapter03_01|              |
+----------------------------+-----------------------------+
| Breakboard x1              | USB cable x1                |
|                            |                             |
| |Chapter03_02|             | |Chapter03_03|              |
+----------------------------+-----------------------------+
|F/M x9   M/M x3             | Motor x1                    |
|                            |                             |
| |Chapter21_22|             | |Chapter21_07|              |
+----------------------------+-----------------------------+
| Rotary potentionmeter x1   | L293D x1                    |
|                            |                             |
| |Chapter21_08|             | |Chapter21_23|              |
+----------------------------+-----------------------------+

.. |Chapter21_22| image:: ../_static/imgs/21_Motor/Chapter21_22.png
.. |Chapter21_23| image:: ../_static/imgs/21_Motor/Chapter21_23.png
.. |Chapter21_07| image:: ../_static/imgs/21_Motor/Chapter21_07.png
.. |Chapter21_08| image:: ../_static/imgs/21_Motor/Chapter21_08.png
.. |Chapter03_00| image:: ../_static/imgs/3_LED/Chapter03_00.png
.. |Chapter03_01| image:: ../_static/imgs/3_LED/Chapter03_01.png
.. |Chapter03_02| image:: ../_static/imgs/3_LED/Chapter03_02.png
.. |Chapter03_03| image:: ../_static/imgs/3_LED/Chapter03_03.png

Component knowledge
=============================

L293D
---------------------------

L293D is an IC Chip (Integrated Circuit Chip) with a 4-channel motor drive. You can drive a Unidirectional DC Motor with 4 ports or a Bi-Directional DC Motor with 2 ports or a Stepper Motor (Stepper Motors are covered later in this Tutorial).

.. image:: ../_static/imgs/21_Motor/Chapter21_24.png
    :align: center

Port description of L293D module is as follows:

.. image:: ../_static/imgs/21_Motor/Chapter21_25.png
    :align: center

For more details, please see datasheet.

When using the L293D to drive a DC Motor, there are usually two connection options.

The following connection option uses one channel of the L239D, which can control motor speed through the PWM, However the motor then can only rotate in one direction.

.. image:: ../_static/imgs/21_Motor/Chapter21_26.png
    :align: center

The following connection uses two channels of the L239D: one channel outputs the PWM wave, and the other channel connects to GND. Therefore, you can control the speed of the motor. When these two channel signals are exchanged, not only controls the speed of motor, but also can control the speed of the motor.

.. image:: ../_static/imgs/21_Motor/Chapter21_27.png
    :align: center

In practical use the motor is usually connected to channel 1 and by outputting different levels to in1 and in2 to control the rotational direction of the motor, and output to the PWM wave to Enable1 port to control the motor’s rotational speed. If the motor is connected to channel 3 and 4 by outputting different levels to in3 and in4 to control the motor's rotation direction, and output to the PWM wave to Enable2 pin to control the motor’s rotational speed.

Circuit
========================

.. list-table:: 
   :width: 100%
   :align: center

   * -  Schematic diagram
   * -  |Chapter21_28|
   * -  Hardware connection
   * -  |Chapter21_29|

.. |Chapter21_28| image:: ../_static/imgs/21_Motor/Chapter21_28.png
.. |Chapter21_29| image:: ../_static/imgs/21_Motor/Chapter21_29.png

Block code 
=========================

Open MakeCode first. Import the .hex file. The path is as below:

( :ref:`How to import project <import_project>` )

+-----------+----------------------------------+-----------+
| File type | Path                             | File name |
+-----------+----------------------------------+-----------+
| HEX file  | ../Projects/BlockCode/21.2_Motor | Motor.hex |
+-----------+----------------------------------+-----------+

After importing successfully, the code is shown as below:

.. image:: ../_static/imgs/21_Motor/Chapter21_30.png
    :align: center

Check the connection of the circuit and verify it correct. Download the code into the micro:bit and rotate the potentiometer. When the potentiometer is in the middle position, the motor stops rotating. When the potentiometer gets away from middle position, the motor speed increases. The potentiometer moves to the limit and the motor speed reaches its maximum value. When the potentiometer is on a different side, the rotating direction of motor is different. 

Read the analog value of the P0 pin of the potentiometer. When the analog value is less than 411, the motor rotates forward. When the analog value is greater than 612, the motor reverses. When the analog value is between 411 and 612, the motor does not rotate.

.. image:: ../_static/imgs/21_Motor/Chapter21_31.png
    :align: center

Set P2 to low level. P1 outputs PWM signal with an interval of 20ms and duty cycle changes with the change of potentiometer variable, then motor rotates forward.

.. image:: ../_static/imgs/21_Motor/Chapter21_32.png
    :align: center

Set P1 to low level, P2 output PWM signal with an interval of 20ms, duty cycle changes with the change of potentiometer variable, then motor rotates in a reverse direction.

.. image:: ../_static/imgs/21_Motor/Chapter21_33.png
    :align: center

When P1, P2 pin output high level, motor does not rotate.

.. image:: ../_static/imgs/21_Motor/Chapter21_34.png
    :align: center

Reference
--------------------------

.. list-table:: 
   :width: 100%
   :align: center

   * -  Block
     -  Function 
   
   * -  |Chapter21_35|
     -  Write an analog signal (0 through 1023) to the pin you set.
  
   * -  |Chapter21_36|
     -  Configure the period of Pulse Width Modulation (PWM) 
        
        on the specified analog pin. 
      
        Before you call this function, 
        
        you should set the specified pin as analog.

.. |Chapter21_35| image:: ../_static/imgs/21_Motor/Chapter21_35.png
.. |Chapter21_36| image:: ../_static/imgs/21_Motor/Chapter21_36.png

Python code
-----------------------------

Open the .py file with Mu. Code, the path is as below:

+-------------+-----------------------------------+-----------+
| File type   | Path                              | File name |
+-------------+-----------------------------------+-----------+
| Python file | ../Projects/PythonCode/21.2_Motor | Motor.py  |
+-------------+-----------------------------------+-----------+

After loading successfully, the code is shown as below:

.. image:: ../_static/imgs/21_Motor/Chapter21_37.png
    :align: center

Check the connection of the circuit and verify it correct. Download the code into the micro:bit and rotate the potentiometer. When the potentiometer is in the middle position, the motor stops rotating. When the potentiometer gets away from middle position, the motor speed increases. The potentiometer moves to the limit and the motor speed reaches its maximum value. When the potentiometer is on a different side, the rotating direction of motor is different. 

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Projects/PythonCode/21.2_Motor/Motor.py
    :linenos: 
    :language: python
    :lines: 1-14
    :dedent:

Read the analog value of the P0 pin of the potentiometer. When the analog value is less than 411, the motor rotates forward. When the analog value is greater than 612, the motor reverses. When the analog value is between 411 and 612, the motor does not rotate.

.. code-block:: python

    potentiometer=pin0.read_analog()
    if potentiometer<=411:
        
    elif potentiometer>=612:
        
    else:

Set P2 to low level. P1 outputs PWM signal with an interval of 20ms, duty cycle changes with potentiometer variable, then motor rotates forward.

.. literalinclude:: ../../../freenove_Kit/Projects/PythonCode/21.2_Motor/Motor.py
    :linenos: 
    :language: python
    :lines: 5-7
    :dedent:

Set P1 to low level. P2 outputs PWM signal with an interval of 20ms, duty cycle changes with the change of potentiometer variable, then motor rotates in a reverse direction.

.. literalinclude:: ../../../freenove_Kit/Projects/PythonCode/21.2_Motor/Motor.py
    :linenos: 
    :language: python
    :lines: 9-11
    :dedent:

When P1, P2 pins output high level, motor does not rotate.

.. literalinclude:: ../../../freenove_Kit/Projects/PythonCode/21.2_Motor/Motor.py
    :linenos: 
    :language: python
    :lines: 13-14
    :dedent:

Reference
-------------------------

.. py:function:: pin.set_analog_period(int)	

    sets the interval; of the PWM output of the pin in milliseconds

    see https://en.wikipedia.org/wiki/Pulse-width_modulation

.. py:function:: pin.write_analog(value)	

    value is between 0 and 1023