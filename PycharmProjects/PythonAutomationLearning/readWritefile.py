file=open('test.txt')
#Toreadthecontent
#print(file.read(8))
#print(file.readline())
 #print(file.readline())
#line=file.readline()
#while line!='':
 #   print(line)
    #line=file.readline()#
# print(file.readlines())

for line in file.readlines():
    print(line)
file.close()