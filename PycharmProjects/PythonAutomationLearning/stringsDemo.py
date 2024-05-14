#stringsDemo

str="RahulShettyAcademy.Com"
str1="ConsultingFirm"
str2="RahulShetty"
str3=" great "

print(str[1])#a
print(str[0:5])#Rahul
print(str+str1)#RahulShettyAcademy.comConsultingFirm
print(str2 in str)#True
var=str.split(".")
print(var)#['RahulShettyAcademy','Com']
print(var[0])#RahulShettyAcademy
print(str3.strip())#great andthecursorwillbeattheendofthestringandNOGAP
print(str3.lstrip())#toremovetheleftwhitespace
print(str3.rstrip())#toremovetherightwhitespace

