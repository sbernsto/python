#writeToFile.PY
# Date: 20 March 2015
# Author: S. A. Bernstorf
# Purpose: To create a variable list of time and write it to a file, 1 item per line


#open a file to write to
fh = open("/Users/bernssa1/Downloads/pythonTrajectory.txt","w")

#Create time variable
time = range(100)

#Loop through variable printing to file each time
for i in time:
    i = str(i)+ ", \n"
    fh.write(i)
    
fh.close()


