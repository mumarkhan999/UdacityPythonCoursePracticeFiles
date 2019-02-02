#before running this code make "b.txt" file and "a.txt" file
#in files folder as it will be deleted in this code


#renaming or removing a file
#os.rename ( oldName , newName)
#os.remove( fileName )


import os
os.rename("files/a.txt" , "files/aaa.txt")
os.remove("files/b.txt")
