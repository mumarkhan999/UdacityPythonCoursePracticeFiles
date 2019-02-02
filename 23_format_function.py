#using format function
#n1 = 2
#n2 = 3
#n3 = 4
#both are same
#print(  "{}{}{} " .format(n1,n2,n3) )  OR print(  "{0}{1}{2} " .format(n1,n2,n3) )
#in {} we write indices corresponding to the values written in .format() function
#e.g  if .format(n1,n2,n3) is like this then idices will be
#0 index is for n1
#1 index is for n2
#3 index is for n3

#print( "{3}{2}{1}".format(n1,n2,n3))
#will display n3 first then n2 then n1

#we can also use {} like this
#"   {  index : number_of_spaces }   "


for i in range(1,11):
    print("{0:5}{1:5}{2:5}".format(i,i*i,i*i*i))
