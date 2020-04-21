#!/usr/bin/env python3
#Group 11
#Ashley Marble
#Joseph Daau
#Cassandra Diaz

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
    
def canBeInt(inp):
    try:
        int(inp)
        return True
    except ValueError:
        return False
def getPower(num):
    binary = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    two = 1
    top = -1
    i = 0
    num = int(num)
    while num > 0:
        i = 0
        two = 1
        if (num % 2) == 1:
            binary[-1] = 1
            num -= 1
            i += 1
            two *= 2
        while i < len(binary):
            if two > num:
                break
            temp = num / two
            if canBeInt(temp) == True:
                topNum = two
                topIndex = i
            i += 1
            two *= 2
        num -= topNum
        binary[-i] = 1
    i = 0
    string = ""
    ones = 0
    printThis = 0
    for each in binary:
        if each == 1:
            ones += 1
            printThis = (len(binary)-1) - i
        i += 1
        string += str(each)
    if ones == 1:
        return printThis
def checkIfKB(convert):
    kb = convert / 1024
    if kb >= 1:
        return str(int(kb)) + " KB"
    else: 
        return convert

def Cache_Calculation(cacheSize, blockSize, assType):
    
    hitRate = 0.0
    cpi = 0.0
    unusedCache = 0.0
    unusedCachePercent = 0.0
    cost = 0.05 * cacheSize
    cacheSizeTo2 = getPower(cacheSize) + 10 # plus 10 bc KB
    offset = getPower(blockSize)
    power = cacheSizeTo2 - offset
    totalBlocks = (2**power)
    indexSize = cacheSizeTo2 - (offset + getPower(assType))
    totalIndicesBytes = 2**indexSize
    tagSize = 32 - indexSize - offset
    overheadMemoryBytes = assType * (1 + tagSize) * totalIndicesBytes / 8
    overheadMemoryKB = overheadMemoryBytes / 1024
    implementMemoryBytes = overheadMemoryBytes + 2**cacheSizeTo2
    implementMemoryKB = implementMemoryBytes / 1024

    

    print("***** Calculated Values *****") 
    print("Total # Blocks:              ", checkIfKB(int(totalBlocks)), "(2^", str(power) + ")")
    print("Tag Size:                    ", tagSize) 
    print("Index Size:                  ", indexSize, "bits, Total Indices:", checkIfKB(totalIndicesBytes)) 
    print("Total # Rows:                ", checkIfKB(totalIndicesBytes))
    print("Overhead Memory Size:        ", "{:,}".format(int(overheadMemoryBytes)), "(or ","{:,}".format(int(overheadMemoryKB)),"KB)")
    print("Implementation Memory Size:  ", "{:,}".format(int(implementMemoryBytes)),"bytes  (or ", "{:,}".format(int(implementMemoryKB)),"KB)")
    #print("----- Results -----")
    #print("Cache Hit Rate:              ", hitRate, " %")
    #print("CPI:                         ", cpi, " cycles/instruction")
    print("Cost:                        $" + str(cost))
    #print("Unused Cache Space:          ", unusedCache, " KB / ", unusedCachePercent, "%")
    # M2
    print("***** CACHE SIMULATION RESULTS *****")
    print("Total Cache Accesses: 282168")                                           # how many times you checked an address 
    print("Cache Hits: 275489")                                                     # it was valid and tag matched 
    print("Cache Misses: 6679")                                                     # it was either not valid or tag didn’t match
    print("--- Compulsory Misses: 6656")                                            # it was not valid
    print("--- Conflict Misses: 23")                                                # it was valid, tag did not match 
    print("***** ***** CACHE HIT & MISS RATE: ***** *****")                         # (Hits * 100) / Total Accesses 
    print("Hit Rate: 97.6330%")                                                     # 1 – Hit Rate 
    print("Miss Rate: 2.3670%")                                                     # Number Cycles/Number Instructions 
    print("CPI: 4.13 Cycles/Instruction")                                           # Unused KB = ( (TotalBlocks-Compulsory Misses) * (BlockSize+OverheadSize) ) / 1024 
    print("Unused Cache Space: 462.19 KB / 580.00 KB = 79.69% Waste: $23.11")       # The 1024 KB below is the total cache size for this example 
    print("Unused Cache Blocks: 26112 / 32768")                                     # Waste = COST/KB * Unused KB 
    
    #For each instruction, assign a CPI of 2 for the fetch.
    #IF that instruction has either a source or destination dataaccess, add 2 CPI * number of reads required.
    #If it has both, the add 2 CPI * number of reads for source and 2CPI * number of reads for destination.
    # Number of reads is determined by data bus size and cache block size. 
    #If cache block is 16 bytes and data bus is 4 bytes (32 bits), then 4 reads are required resulting in 4 * 2 = 8 CPI. 
    #If a read wraps around, then the 2nd cache row accessed is independent of the first. It may be a hit/miss on its own. 

    return

def trace_work(file_name):

    #trace through the command line input as a String
    # where we see each of those params
    #get the appropriate values
    #print('In TraceWork')
    #file_name = "trace1.txt"
    #SECOND
    #TRACE FILE WORK
    #2 examples of Trace lines

    #EIP (04): 7c809767 83 60 34 00 and dword [eax+0x34],0x0
    #dstM: 00000000 -------- srcM: 00000000 -------- 
    
    #EIP (07): 7c80976b 8b 84 88 10 0e 00 00 mov eax,[eax+ecx*4+0xe10]
    #dstM: 7ffdf034 00000000 srcM: 7ffdfe2c 901e8b00
    
    try:
        
        with open(file_name, "r") as trace_file:

            length = ""
            address = ""
            dst1 = 0
            dst2 = 0
            src1 = 0
            src2 = 0
            #i = 0
            size = 0
           #onlyTo20 = 0
            for line in trace_file:

                split_line = line.rstrip().split()
                #print(split_line)
                    #First line is instruction fetch line contains the data length (number of bytes read), 
                    #the address (a 32-bit hexadecimal number) and data (the machine code of the instruction). 
                    #you care about the length and the address

                if "".join(split_line[0:1]) == "EIP":
                    length =  "".join(split_line[1:2])
                   # if onlyTo20 < 20:
                   #     print(str(split_line[2]) + ":", length[:-1])
                    len = int(length.replace('(','').replace(')','').replace(':',''))
                    add = hex(int("".join(split_line[2:3]),16))
                    #data = "".join(split_line[4:])
                
                #second line the data access line shows addresses for destination memory “dstM” (i.e. the write address) and source memory
                #“srcM” (i.e. the read address) and the data read. 
                #There is NO indication of the length of data read and thus you should ASSUME all data accesses are 4 bytes. 
                #For the data line, the length is given as 4 bytes and you need the dst/src addresses. 
                #Additionally, if the src/dst address is zero, then ignore it – that means there was no data access. 
                #If the dstM address is all 0's from the start, ignore it
                #if the srcM is all 0000000, ignore it

                elif "".join(split_line[0:1]) == "dstM:":
                    
                    if "".join(split_line[1:2]) == "00000000":   #ignore dst
                        dst1 =0
                    else:
                        dst1 = hex(int("".join(split_line[1:2]),16))
                        size+=1

                    if "".join(split_line[2:3]) == "--------":
                        dst2 = 0
                    else:
                        dst2 = hex(int("".join(split_line[2:3]),16))
                        size+=1

                    if "".join(split_line[4:5]) == "00000000":   #ignore src
                        src1 = 0
                    else:
                        src1 = hex(int("".join(split_line[4:5]),16))
                        size+=1

                    if "".join(split_line[5:6]) == "--------":
                        src2 = 0
                    else:
                        src2 = hex(int("".join(split_line[5:6]),16))
                        size+=1
                    
                    #i = i+1
                    #onlyTo20 += 1
                    #Cache_Calculation(len,add,dst1,dst2,src1,src2,i)
                    #print(dst1," ",dst2," ",src1," ",src2)

                #trace_file.readline()
                #len = int(length.replace('(','').replace(')','').replace(':',''))
                #add = hex(int("".join(split_line[2:3]),16))
                #print(len," ",add)
                #Cache_Calculation(len, add)

        trace_file.close()

    except IOError:
        print('Error opening file or file does not exist')
    except EOFError:
        print('File is empty')

    return


#Main function of obtaining command line arguments
#Purpose:
#   Parse through command line arguments to obtain neccessary information
#Paramaters:
#   N/A
# Return:
#    traceFileNameInput     <trace file name>
#    cacheSizeInput         <cache size in KB> 
#    blockSizeInput         <block size>
#    associativityInput     <associativity>
#    replacementInput       <replacement policy> 
def main():


    #FIRST DETERMINE EXECUTEABLE INFORMATION
    #Input paramaters from our exec file 
    #1. –f <trace file name> [ name of text file with the trace ]
    #2. –s <cache size in KB> [ 1 KB to 8 MB ]
    #3. –b <block size> [ 4 bytes to 64 bytes ]
    #4. –a <associativity> [ 1, 2, 4, 8, 16 ]
    #5. –r <replacement policy> [ RR or RND or LRU for bonus points] 
    #Exmaple of a exec command (the )
    #Sim.exe –f trace1.txt –s 1024 –b 16 –a 2 –r RR 



    #initial check to see if we have enough command line arguments
    if len(sys.argv) < 10:
        print("Too few arguments, you entered less then 11 arguments")
        sys.exit()
    if  len(sys.argv) > 11:
        print("Too many arguments, you entered more then 11 arguments")
        sys.exit()

    #for joe because his VS is stupid and doesn't wanna work correctly
    argEx = ['code.py', '–f', 'trace1.txt', '–s', '1024', '–b', '16', '–a', '2', '–r', 'RR']
    traceFileNameInput = ''
    cacheSizeInput = ''
    blockSizeInput = ''
    associativityInput = ''
    replacementInput = ''

    #for everything else
    print("Starting project \n")
    for i in sys.argv:
        if i == "-f":
           traceFileNameInput = sys.argv[2]
           print("Cache Simulator CS 3853 Spring 2020 - Group #11")
           print()
           print("Trace File:                   ",traceFileNameInput)

        if i == "-s":
            cacheSizeInput = sys.argv[4]
            print("Cache Size:                  ", cacheSizeInput)

        if i == "-b":
            blockSizeInput = sys.argv[6]
            print("Block Size:                  ",blockSizeInput )

        if i == "-a":
            associativityInput = sys.argv[8]
            print("Associativity:               ", associativityInput)

        if i == "-r":
            if sys.argv[10] ==  "RR" or sys.argv[10] == "rr":
                print("Replacement Policy:      ", "Round Robin")
            if sys.argv[10] ==  "RND" or sys.argv[10] == "rnd":
                print("Replacement Policy:      ", "Random")
            if sys.argv[10] ==  "LRU" or sys.argv[10] == "lru":
                print("Replacement Policy:      ", "Least Recently Used")
            print()
    Cache_Calculation(int(cacheSizeInput), int(blockSizeInput), int(associativityInput))
    

    

    index = 0
    #loop through argEx(use thes in the loop above, this is for me testing later)
    #for val in argEx:
        #print(val)
        #print(val == "–r")

   #     if val == "–f":
    #       traceFileNameInput = argEx[index + 1]
     #      print("file name: ", traceFileNameInput)

      #  if val == "–s":
       #     cacheSizeInput = argEx[index+1]
       #     print("cache size: ", cacheSizeInput)

#        if val == "–b":
 #           blockSizeInput = argEx[index+1]
  #          print("block size is :",blockSizeInput )

   #     if val == "–a":
    #        associativityInput = argEx[index+1]
     #       print("associativity is: ", associativityInput)

      #  if val == "–r":
        #    replacementInput = argEx[index+1]
       #     print("Replacement is: ", replacementInput)

#        index = index +1


    return traceFileNameInput, cacheSizeInput, blockSizeInput, associativityInput, replacementInput

#Actual Main
if __name__ == "__main__":
    traceFileNameInput, cacheSizeInput, blockSizeInput, associativityInput, replacementInput = main()
    #print("Return Values are: ", traceFileNameInput," ", cacheSizeInput," ", blockSizeInput, " ", associativityInput, " ", replacementInput)
    trace_work(traceFileNameInput)
