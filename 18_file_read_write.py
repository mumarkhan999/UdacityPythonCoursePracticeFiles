#file handling

#both ways are same to open a file
#either use /  or \\ in the path
#bo = open("files/sample.txt","w")
#
#open( fileName , "w" for writing OR "r" for reading OR "a" for appending)



#writing
bo = open("files\\sample.txt","w")
bo.write("I am writing")
bo.close()

#reading
bo = open("files/sample.txt","r")
content = bo.read()
print(content)
bo.close()
