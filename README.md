# CPU Instruction-Memory Initialization

I have written a Python program that allows the user to initialize their processor instruction memory to a certain program of their choosing.

The Python program takes as input the hexadecimal dump text file of the desired assembly program, and generates a VHDL file (.vhd) of instruction memory initialized with this program.

The maximum allowed size of the assembly program is 1 kilobyte (8192 bits) to safely fit inside instruction memory. This could be changed manually depending on user preference and instruction memory capacity.

This allows users to quickly and efficiently change the default program loaded into the processor at bootup.
