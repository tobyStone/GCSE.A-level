print("opening")
def writeToFile():
   
    myFile = open("TextFile1.txt", "a")
    
    for each in range(1, 8):
        record = "This is record number {0} in the file \n".format(each)
        print(record)
        myFile.write(record)
    myFile.close()

writeToFile()
