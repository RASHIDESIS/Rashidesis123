name  ="sudanir fua"
phone ="12345678910"
email ="1"

if(len(name)==0 or len(phone)==0 or len(email)==0):
    print("failed")
else:
    if(len(name)<2 or len(name)>6):
        print("the name must be between 2 and 6")
    elif(len(phone)!=11):
        print("the phone number must be 11")
    else:
        print ("success")

print("mushfiq"*10 )