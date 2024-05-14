#ListusingIntegers

# L1=[1,2,3,4,5]
# print(L1[0])#1
# print(L1[1])#2
# print(L1[-1])
#ListusingStrings
# L2=["Maha","Laxmi","Sai","Shree","Prabu"]
# print(L2[2])#Sai
# print(L2[3])#Shree
# print(L2[-1])#Prabu
# print(L2[1:4])#'Laxmi','Sai],'Shree']

#ListusingIntegersandStrings

L3=[6,7,"Meenakshi","Rithanya",9.5]
# print(L3[1])#7
# print(L3[3])#Rithanya
# print(L3[2])#Meenakshi
# print(L3[-1])#9.5
L3.insert(4,"Maha")
print(L3)
L3.append("End")
print(L3)
L3[2]="MEENAKSHI"
print(L3)
del L3[5]
print(L3)

#Tuple Concepts
L1=(6,7,"Meenakshi","Rithanya",9.5)
L1[2]="MEENAKSHI"
print(L1)