#!/usr/bin/env python3

import sys

 
#Generic:                               Example:
#Cache Size: *** KB                         Cache Size: 1024 KB  (<- This means 1 MB)
#Block Size: *** bytes                      Block Size: 16 bytes
#Associativity: ***                         Associativity: 2
#Policy: RR or RND or LRU                   Policy: RR
#----- Calculated Values -----
#Total #Blocks: ***                         Total #Blocks: 64 KB (2^ 16)
#Tag Size: *** bits                         Tag Size: 13 bits
#Index Size: *** bits, Total Indices: ***   Index Size: 15 bits, Total Indices: 32 KB
#Overhead Memory Size: ***                  Overhead Memory Size: 114,688 bytes (or 112 KB)
#Implementation Memory Size: ***            Implementation Memory Size: 1,163,264 bytes (or 1136 KB)
#----- Results -----
#Cache Hit Rate: *** %                      Cache Hit Rate: 96.2 %
#CPI:  ***                                  CPI: 1.5 cycles/instruction 

def Assosicativity():
    return
    

def RR():
    return
    


def traceWork():

    #FIRST DETERMINE EXECUTEABLE INFORMATION
    #Input paramaters from our exec file 
    #1. –f <trace file name> [ name of text file with the trace ]
    #2. –s <cache size in KB> [ 1 KB to 8 MB ]
    #3. –b <block size> [ 4 bytes to 64 bytes ]
    #4. –a <associativity> [ 1, 2, 4, 8, 16 ]
    #5. –r <replacement policy> [ RR or RND or LRU for bonus points] 
    #Exmaple of a exec command (the )
    #Sim.exe –f trace1.txt –s 1024 –b 16 –a 2 –r RR 

    #trace through the command line input as a String
    # where we see each of those params
    #get the appropriate values
    print("This doesn't do anything yet!")
    filename = sys.argv[1]

    openFile = open(filename, "r")

    lines = openFile.readlines()
    numBytesRead = 0
    addressOfInstruction = ""
    dataReadIngore = ""
    i = 0

    while i < len(lines):
        line = lines[i].split()
        print(line)
        if lines[i] == "\n":
            print("empty line")
            i += 1
            continue
        if line[0] == "EIP":
            numBytesRead = line[1][1:2]
            print(numBytesRead)
            addressOfInstruction = line[2]
            print(addressOfInstruction)
            dataReadIgnore = line[3:]
            print(dataReadIgnore)
        if line[0] == "dstM:":
            print("do some other stuff")
        i += 1
    
    openFile.close()

    #SECOND
    #TRACE FILE WORK
    #2 examples of Trace lines

    #EIP (04): 7c809767 83 60 34 00 and dword [eax+0x34],0x0
    #dstM: 00000000 -------- srcM: 00000000 -------- 

    #EIP (07): 7c80976b 8b 84 88 10 0e 00 00 mov eax,[eax+ecx*4+0xe10]
    #dstM: 7ffdf034 00000000 srcM: 7ffdfe2c 901e8b00

    #First line is instruction fetch line contains the data length (number of bytes read), the address (a 32-bit hexadecimal number) and data
    #(the machine code of the instruction). 
    #you care about the length and the address


    #second line the data access line shows addresses for destination memory “dstM” (i.e. the write address) and source memory
    #“srcM” (i.e. the read address) and the data read. There is NO indication of the length of data read and thus you should ASSUME all data accesses are 4 bytes. 
    #For the data line, the length is given as 4
    #bytes and you need the dst/src addresses. Additionally, if the src/dst address is zero, then ignore it – that means
    #there was no data access. 
    #If the dstM address is all 0's from the start, ignore it
    #if the srcM is all 0000000, ignore it

    #For each instruction, assign a CPI of 2 for the fetch.
    #IF that instruction has either a source or destination dataaccess, add 2 CPI * number of reads required.
    #If it has both, the add 2 CPI * number of reads for source and 2CPI * number of reads for destination.
    # Number of reads is determined by data bus size and cache block size. 
    #If cache block is 16 bytes and data bus is 4 bytes (32 bits), then 4 reads are required resulting in 4 * 2 = 8 CPI. 
    #If a read wraps around, then the 2nd cache row accessed is independent of the first. It may be a hit/miss on its own. 



    return


#Main function
#where all our functions calls will be done
def main():
    print("Starting project \n")
    for i in sys.argv:
        print(i, '\n')
        sys.stdout.write(i)
    print(sys.argv[0])

if __name__ == "__main__":
    main()
    traceWork()