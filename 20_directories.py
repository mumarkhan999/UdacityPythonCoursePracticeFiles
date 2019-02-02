#making directories
#changing path of directories
#getting path of directories


#os.mkdir()
#is to make directory
#os.getcwd()
#is to get the path of directory where it is created
#os.chdir(  new_path  )
#is to change the path of directory which is to be formed


#os.mkdir()
#can also take path of the directory which is going to be formed
#like
#os.mkdir(  'C:\\Users\\USER\\Desktop\\PythonPrac\\dir'  )


#os.rmdir(  directory_name )
#to remove directory


#os.rename(  old_name , new_name)
#to rename directory
#this method is also used for files

import os
#this line will create directory at the location of
#of your code file
#os.mkdir("hahahaha")
#so first change the directory
print(os.getcwd())
os.chdir("dir")
print(os.getcwd())
os.mkdir("hahahaha")

input("enter something to delete hahahaha directory\n")

print(os.rmdir("hahahaha"))


