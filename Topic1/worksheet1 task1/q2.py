pupilNames=["dana","anna","lucy","henry","susan"]
nameSearch=input("enter the pupils name:")
#constant mx
max=len(pupilNames)

# flag to identify if the name is found
nameFound=False
i=-1#
x=1

while nameFound==False:                                                      #for i in range(0,max):
     if nameSearch==pupilNames[i+x]:
         nameFound=True
     x=x+1
     if max==i+x:
      print("name not found")
     
      
if nameFound==True:
    print("record number =", i + x)
else: 
    print("name not found")

#  selection, to check if the flag is true then output if the name is found


