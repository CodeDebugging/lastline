import os
import sys

retval = 1
print ("File truncation tool version 1, 09 JAN 2018")
if (len(sys.argv) < 1):
    print ("Usage: delete <filename>")
    print ("This program will trunacte the file from the character 0x1A")
    print ("Returns 0 in case of 0x!a removed or EOL found, 1 if any other condition is found")
    sys.exit(retval);      

# 26 (0x1A) is SUB character sometimes appearing after last EOL in text files
chartofind = 26

try:
    #with io.open(filename, 'r', encoding='utf-8', errors='replace') as logfile:
    #file = open(sys.argv[1], "rb")
    # open for binary read and modify, but not create when not exists
    file = open(sys.argv[1], "a+b")

except Exception as exception:
    #type, value, traceback = sys.exc_info()
    #print('Error opening %s: %s %s' % (value.filename, value.strerror, type))       
    #sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]
    #print('Error opening %s: %s %s' % (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]))
    print ("Could not open file!")               
    sys.exit(retval)
else:
    print ("File name: ",sys.argv[1])
    statinfo = os.stat(sys.argv[1])
    print ("File size: ", statinfo.st_size)
        
    #seek to the end of file
    file.seek(0, os.SEEK_END)
    # get the file size
    # last position is size - 1 
    pos = file.tell() - 1
        
    #y = 0;
    while pos > 0:
        file.seek(pos, os.SEEK_SET)
        #y = y + 1
        #if (y == 10):
        #    break  
        ch = file.read(1)         
        x = len(ch)
        if (x > 0): 
            # debung output
            print(ord(ch))
            #sys.stdout.write(str(ch)+"\n")  
            if (ord(ch) == 10):
            # normal end of file is 0Xd 0a
                print("End of line found at end of file !")
                retval = 0 
                break               
            if (ord(ch) == chartofind):
                print("Found arrow character 0x1A !")    
                print("Truncating anything from here")  
                file.seek(pos, os.SEEK_SET)
                retval = 0
                #file.truncate()   
                break
        else:
            #something went wrong
            retval = 1
            break    
        pos -= 1    
                       
    file.close()
    print ("Completed !")
    sys.exit(retval)
        

