#!/usr/bin/env python3
#Group 11
#Ashley Marble
#Joseph Daau
#Cassandra Diaz

import sys
import array as arr  

#For our simulation, reading memory requires 3 clock
#cycles while reading the cache requires only 1.

#For each instruction, assign a CPI of 2 for the fetch.
#IF that instruction has either a source or destination dataaccess, add 2 CPI * number of reads required.
#If it has both, the add 2 CPI * number of reads for source and 2CPI * number of reads for destination.
# Number of reads is determined by data bus size and cache block size. 
#If cache block is 16 bytes and data bus is 4 bytes (32 bits), then 4 reads are required resulting in 4 * 2 = 8 CPI. 
#If a read wraps around, then the 2nd cache row accessed is independent of the first. It may be a hit/miss on its own. 

#NEW!!
#GLOBAL CLOCK OF TOTAL CYCLES WE WILL INCREMENT
clockCycle = 0
#if its a miss increment this clock as well
cycleMissed = 0
#cache
cache = [[0]*1]*1
#Global for calculation 
cacheSize = 0 
blockSize = 0 
associativity = 0
replacement = ""
TotalBlocks = 0
Overhead = 0
impKB = 0
cost = 0
index = 0


#NEW FUNCTION TO DO!!! 
#function: AssosicativityReplace
#purpose:
#           replace in our cache array system basedon associativity type
#param:
#           replaceType                             what kind of replacement we are doing
#return     
#           nothing its pretty much a void function
def AssosicativityReplace(replaceType, value):
    #check what replacement type we have [RR(round robin, LRU(least recently used)] only need to impliment 2 and i'm unsure of RND
    global index
    if replaceType == "RR":
        
        #replace
        cache[index][value] = value
        #keep track from top to bottom which index you are replacing
        if index == len(cache):
            index = 0
        else :
            index+=1
        #set up next variable you will be checking(this might need to be a global)
    

    #if replaceType == "LRU":
        #look for least recently used cache
        
        #replace    


    return
    

#NEW FUNCTION TO DO!!! 
#function: CacheWork
#purpose:
#       Take parts of the instrecution we read in and do cache work
#       Processes both the EIP and dstM line we read in
#Paramaters:
#       indexSize                   size of our index in bits 
#       numericAddress              Current address we are at we wish to read from(EID)   
#       dstMWriteAddress            next avaiable write memory(dstm)   
#       srcMReadAddress             next vaiable point of read memory(srcM)
#       instFetchTF                 1 if there was a instruction to fetch ie the read line was EIP
#                                   0 if there wasn't a line to fetch ir: dstM line
#       assocType                   How we wish to replace
#       instLenREDO                 had to keep track of previous instruction's instLen for dstM and srcM(thought not sure if needed)
#return:
#       instLenREDO                 0 -> both valid lines, no need to keep track of in the next iteration
#                                   >0   -> need to keep track of for next iteration    
def CacheWork(indexSize, numericAddress, dstMWriteAddress, srcMReadAddress, assocType, instLenREDO):

    addressAmu = 0 
    valid = 0 
    invalid = 0 
    tagMiss = 0
    #given a 32 bit bus, we can only access 4 bytes of instruction at a time
    #if the instLen is > 4, we will have to do that instruction multiple times

    #NOT SURE IF NEEDED
    #if there is a empty dstM line, keep the instLen as a return value to be used in the 
    #next iteration of this code 
    
    #Based of the numericAddress, get the tag and index values
    last = numericAddress[5:10:]
    last  = "".join(last[1::])
    index = hex(int(last,16))

    if len(last) ==  3 :
        index = hex(int(last+"0",16))
    #print(numericAddress)
    #print(index)

    #loop by how many times we have to read 
    if int(assocType) > 4:
        i = int(assocType) / 4
    else:
        i = int(assocType)
    
    for x in range(int(i)):
        #check if the index exists in the the first associativity
        print("In loop: ",x) #for compile purpouses until code is made
        #WARNING, THIS PART MIGHT NEED TO BE EDITED LATER
        
        #if the index exists but the tag is different, check the other assoc table part to see if it exists
        #if it doesn't exist its a miss
        #a miss increments clock:(3 cycles * number of memory reads to populate cache block) 
        # number of reads == CEILING ( block size / 4 )
        #increment both clockCycle and cycleMissed

        #IF THERE IS A NEED TO REPLACE
        #(every associativity has the same index but diff tags, and we want to add 1 more which is larger then our associative range
        #ie: we have 4 9BC indexs and want to add a 5th in a 4 associativty, we need to now replace)
        #call AssosicativityReplace

        #if its a hit, increment clock by one
        #increment clockCycle
    
        #if there is a instruction we grabbed (EIP line), add 2 to clockCycle
    
        #else if not EIP Line, increment clockCycle by 1 because we are calculatnig a effective address
        #these last two parts might be done at the same time cause of the fact we are reading both lines in



    return addressAmu, valid, invalid, tagMiss #instLenREDO because iDK its purpose





#NEW FUNCTION TO DO!
#function: CreateCache
#purpose:
#       create a 2d array of our cache based off of associativity
#Paramaters:
#       associativity               associtivty type
#       rows                        full length of rows(memory/block size) <-if this incorporates the memory/block size/associtivty
#                                   skip the second comment
#Return:
#       2d array [index][# of tags]
def CreateCache(associativity, row):  

    #create 2d array[number of rows/associativity][associtivity]
    rows, cols = (int(row / associativity), associativity) 
    cols+=1
    cache = [[0]*cols]*rows

    #print(cache)
    return cache





#function: canBeInt
#purpose:
#    check if value passed in is a int
#param:
#       inp           any value we wish to check
#return:
#       true          value is a int
#       false         value is not a int
def canBeInt(inp):
    try:
        int(inp)
        return True
    except ValueError:
        return False


#function:  getPower
#purpose:
#       get the power of 2 value of the number passed in
#param:
#       num             number we wish to find the power of
#return:
#       printThis       power of the number in 2
#
#Side note: Overcomplicated *Ashely :3
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



#function: checkIfKB
#purpose: 
#           Checks to see if the value passed in is a KB
#param:
#           convert             number we wish to check
#Return:
#       str(int(kb)) + " KB"    size in KB if something is Larger then a KB
#       convert                 value isn't larger thena  kilobyte              
def checkIfKB(convert):
    kb = convert / 1024
    if kb >= 1:
        return str(int(kb)) + " KB"
    else: 
        return convert


#function: Cache_Calculation
#purpose:
#       calculate the return values to stdout
#param:
#    cacheSize          size of the cache in MB
#    blockSize          size of our blocks in bytes
#    assType            associativity type
def Cache_Calculation(cacheSize, blockSize, assType):
    
    global cost
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

    #Global For M2
    global TotalBlocks
    global Overhead
    global impKB
    TotalBlocks = int(totalBlocks)
    Overhead = tagSize+1
    impKB = implementMemoryBytes / 1024
    
    #milestone 1 Printout
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
    
    return
#function: cacheCalc2
#purpose:
#       calculate the return values to stdout
#param:
#    addressAmu         How many times an adress  was accessed
#    valid              How many times it was valid and tag matched
#    invalid            How many times it was not valid
#    tagMiss            Tag did not match
#    intructionAmu      The times the dst and src were 0 (instrucctions read)
def cacheCalc2(addressAmu, valid, invalid, tagMiss, intructionAmu):

    #NEW!!
    #MILESTONE 2
                                      
    global clockCycle
    global TotalBlocks
    global blockSize
    global Overhead
    global cost

    print("***** Cache Simulation Results *****")                                   
    # how many times you checked an address
    print("Total Cache Accesses: ", addressAmu)                                     
    # it was valid and tag matched
    print("Cache Hits: ", valid)                                                    
    # it was either not valid or tag didn’t match
    print("Cache Misses: ", invalid+tagMiss)                                                
    # it was not valid
    print("--- Compulsory Misses: ", invalid)                                           
    # it was valid, tag did not match 
    print("--- Conflict Misses: ", tagMiss)                                
    print("***** ***** CACHE MISS RATE: ***** *****")
    #(Hits * 100) / Total Accesses
    hit = (valid *100) / addressAmu
    print("Hit Rate: % 2.4f"% hit,"%")                                                    
    # 1 – Hit Rate
    miss = 100 - hit
    print("Miss Rate: % 2.4f"% miss,"%")
    #if clockCycle == 0:
    #    clockCycle = 41.3
    print("CPI: ",clockCycle / intructionAmu," Cycles/Instruction")                                          # Number Cycles/Number Instructions 
    #TotalBlocks = 32768 
    #Overhead = 17
    #impKB = 580
    #cost = 29
    unusedKB = ( (int(TotalBlocks)-invalid) * (((int(blockSize)*8)+int(Overhead)) / 8) ) / 1024
    # The 1024 KB below is the total cache size for this example
    # Waste = COST/KB * Unused KB 
    percentage = (unusedKB / impKB)*100
    print("Unused Cache Space: %.2f"% unusedKB," KB / %.2f"% impKB," KB = %.2f"%percentage,"%"," Waste: $%.2f"% round((cost/impKB *float(unusedKB)),2) )
    print("Unused Cache Blocks: ",(int(TotalBlocks)-invalid)," / ", TotalBlocks)  



    return

def trace_work(file_name, associativityInput):

    #trace through the command line input as a String
    # where we see each of those params

    #EIP (04): 7c809767 83 60 34 00 and dword [eax+0x34],0x0
    #dstM: 00000000 -------- srcM: 00000000 -------- 
    
    #EIP (07): 7c80976b 8b 84 88 10 0e 00 00 mov eax,[eax+ecx*4+0xe10]
    #dstM: 7ffdf034 00000000 srcM: 7ffdfe2c 901e8b00
    
    try:
        
        with open(file_name, "r") as trace_file:

            length = ""
            address = ""
            dst1 = 0
            src1 = 0
            checker = 0
            instLenREDO = 0
            # will change to 0 when there are actual numb being returned
            intructionAmu = 1
            addressAmu = 1 
            valid = 1
            invalid = 1 
            tagMiss = 1

            for line in trace_file:

                split_line = line.rstrip().split()
                    #First line is instruction fetch line contains the data length (number of bytes read), 
                    #the address (a 32-bit hexadecimal number) and data (the machine code of the instruction). 
                    #you care about the length and the address

                if "".join(split_line[0:1]) == "EIP":
                    length =  "".join(split_line[1:2])
                    len = int(length.replace('(','').replace(')','').replace(':',''))
                    add = hex(int("".join(split_line[2:3]),16))
                
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

                    if "".join(split_line[4:5]) == "00000000":   #ignore src
                        src1 = 0
                    else:
                        src1 = hex(int("".join(split_line[4:5]),16))

                    if dst1 == 0:
                        instLenREDO = len
                        checker = 1
                        intructionAmu += 1
                    #NEW!!!!
                    #ONCE WE FINISH READING THE SECOND LINE, WE NOW CALL CACHEWORK 
                    add, val, inval, tagM = CacheWork(len, add, dst1, src1, associativityInput, instLenREDO)
                    addressAmu+= add 
                    valid += val 
                    invalid += inval 
                    tagMiss += tagM
                    #instLenREDO = 0
                    checker = 0


        #close the file once we have fully went through it
        trace_file.close()
        cacheCalc2(addressAmu, valid, invalid, tagMiss, intructionAmu)
        #cacheCalc2(int(282168), int(275489), int(6656), int(23), int(10))

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


    #reutrn values that will be used in other functions
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


    #printout our cache calculations
    Cache_Calculation(int(cacheSizeInput), int(blockSizeInput), int(associativityInput))
    


    return traceFileNameInput, cacheSizeInput, blockSizeInput, associativityInput, replacementInput

#Actual Main
if __name__ == "__main__":
    traceFileName, cacheSize, blockSize, associativity, replacement = main()

    #create our cache based off of associativity
    rows = int(cacheSize) / int(blockSize) / int(associativity)
    cache = CreateCache(int(associativity), int(rows))
    trace_work(traceFileName, associativity)
