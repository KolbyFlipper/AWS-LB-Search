import zlib
import gzip
import tkinter, tkinter.filedialog
import os

#workflow: 
#run py unzip.py in cmd, select target directory with gzipped files, input info it needs
#open the output file it tells you
#save whatever is in your output file somewhere else (or rename it) -> goto step 1

#tkinter just makes it easier to run repeatedly, you can also hardcode a folder path as "directory"
directory = tkinter.filedialog.askdirectory() 

lookingFor = input('What would you like to search for? ("status" for status code, "string" for string)\n')

if (lookingFor != 'status' and lookingFor != 'string'):
    print("Invalid input- remember not to add any spaces!")
    exit()

fOut = open("fullOutputFile.txt", 'wb')    #full file as txt
fOut1 = open("statusCodeOutput.txt",'w')   #status code search results
fOut2 = open("stringSearchOutput.txt",'w') #string search results

for file in os.scandir(directory):
    inFile = gzip.GzipFile(file,'rb')
    inputTxt = inFile.read()
    fOut.write(inputTxt)

inFile.close()
fOut.close()
#have to close and reopen the file or Python thinks it's bytes instead of text
trim = open("fullOutputFile.txt", 'r')

if(lookingFor == 'status'):
    searchCode = input("What status code are you looking for?\n")
    print("Result will be in file named statusCodeOutput")
    
    for line in trim:
        data = line.split(" ")
        #print("elb status code: " +data[8] + " target status code " + data[9])
        if(data[8] == str(searchCode)): #elb status code
            fOut1.write(line)
        if (data[9] == str(searchCode)):#target status code
            fOut1.write(line) 
    #if you want them split by elb/target status code, change "fOut1" in the above line to fOut2
    #elb results will be in statusCodeOutput, target results will be in searchStringOutput 
    
if(lookingFor == 'string'):
    searchString = input("What string are you looking for?\n")
    print("Result will be in a file named searchStringOutput")
    for line in trim:
        if(str(searchString) in line): #if you're looking for a string
            fOut2.write(line)

fOut1.close()
trim.close()


