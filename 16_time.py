#using time
import time

#generating time frame of current time
t = time.time()
#converting into local time
#it will give the description
t = time.localtime(t)
#this can also be used like that for current time
#time.localtime()
print(t)


#more readable form
#getting string of the current time
print("\n"*5)
print(time.asctime())
#it can also be used for other time
#time.asctime(t)


#displaying current time in better readable form
t.asctime(t.localtime(t.time()))
#both are same
t.asctime(t.localtime())

#delaying time
sleepTime = 3
time.sleep(sleepTime)
print("You have slept for ",sleepTime)




