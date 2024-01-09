pupilNames=["dana","anna","lucy","henry","susan"]
nameSearch=input("enter the pupils name:")
#constant mx
max=len(pupilNames)

# flag to identify if the name is found

for i in range(0,max):
    if nameSearch!=pupilNames[i]:
        if i==4:
            print("name not found")
    else: 
        if nameSearch==pupilNames[i]:
            print("record number=", pupilNames[i +1])



#  selection, to check if the flag is true then output if the name is found



 





