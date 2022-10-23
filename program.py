from typing import Type


upper = "library ieee;\nuse ieee.std_logic_1164.all;\nuse ieee.numeric_std.all;\nuse work.archer_pkg.all;\nentity rom is\n\tport (\n\t\taddr : in std_logic_vector (ADDRLEN-1 downto 0);\n\t\tdataout : out std_logic_vector (XLEN-1 downto 0)\n\t);\nend rom;\narchitecture rtl of rom is\n\ttype memory is array (0 to 2**(ADDRLEN)-1) of std_logic_vector (7 downto 0);\nbegin\n\tprocess (addr) is\n\t\tvariable rom_array : memory := ("
lower = "\n\t\tothers => (others=>'0'));\n\t\tvariable word_addr : std_logic_vector (ADDRLEN-1 downto 0) := (others=>'0');\n\tbegin\n\t\tword_addr := addr(ADDRLEN-1 downto 2) & \"00\";\n\t\tdataout <= rom_array(to_integer(unsigned(word_addr))+3) & rom_array(to_integer(unsigned(word_addr))+2) & rom_array(to_integer(unsigned(word_addr))+1) & rom_array(to_integer(unsigned(word_addr)));\n\tend process;\nend architecture;"
#upper and lower are the necessary VHDL code before and after the program hex code

def generateVHD(filename):
    myHex = open(filename,'r')
    lineCount = 0
    myString = ""
    for line in myHex:
        lineCount +=1
        if lineCount > 256:
                raise TypeError ("ERROR: Program is too large -- ROM cannot be initialized")
        else:
            for i in range(6,-2,-2):
                myString = myString + "X\""+ line[i:i+2]+ "\","
        myString = myString + "\n\t\t"
    myVHD = open(filename[:-4]+".vhd",'w')
    myVHD.write(upper + "\n\t\t")
    myVHD.write(myString)
    myVHD.write("\n\t\t")
    myVHD.write(lower)
    myVHD.close()
    myHex.close()

generateVHD("myHexFile.txt")
#in the above, replace "myHexFile.txt" with appropriate text file

#the program cannot be over 2^13 bits = 8192 bits
#each line in the hexadecimal file is an 8 digit hex value, thus each line is 8*4 = 32 bits long
#thus, a maximum of 8192 bits corresponds to 8192 bits /32 bits per line = 256 lines
