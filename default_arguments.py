#DEFAULT ARGUMENTS = A default value for certain parameters 
# default is used when that argument is omitted 
# make your functions more flexible,reduces


import time
def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")
count(10)        
