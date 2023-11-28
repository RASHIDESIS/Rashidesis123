                        #SCIENCE:

Bangla_1 = 35                       #Full marks = 100
Bangla_2 = 69                       #Full marks = 100
Eng_1 = 50                          #Full marks = 100         
Eng_2 = 70                          #Full marks = 100
General_Math = 10                   #Full marks = 100
Highermath_subjective = 5           #Full marks = 75
Highermath_practical = 2            #Full marks = 25   
Biology_subjective = 0              #Full marks = 75  
Biology_Practical = 21              #Full marks = 25   
Physics_Subjective = 69             #Full marks = 75 
Physics_Practical = 22              #Full marks = 25
Chemistry_Subjective = 64           #Full marks = 75           
Chemistry_Practical = 24            #Full marks = 25 
Islamic_Religion = 50               #Full marks = 100  
Social_science = 60                 #Full marks = 100   
ICT = 99                            #Full marks = 100 

Bangla = ( (Bangla_1 + Bangla_2)/2 )
English = ( (Eng_1 + Eng_2)/2 )
Higher_Math = (Highermath_practical + Highermath_subjective)
Biology = (Biology_subjective + Biology_Practical)
Physics = (Physics_Subjective + Physics_Practical)
Chemistry = ( Chemistry_Subjective + Chemistry_Practical)

print("SUBJECT             SCORE    GRADE POINT         GRADES")

if (Bangla>80 and Bangla<100):
     print("Bangla         ",Bangla_1,Bangla_2,Bangla," Grade point = 5.00, Grade = A+"),
elif(Bangla<0 or Bangla>100):
        print("Bangla        ",Bangla_1, Bangla_2,  Bangla," Grade point = Invalid, Grade = Invalid")
else:
    if(Bangla>=70 and Bangla<=79):
        print("Bangla         " ,Bangla_1, Bangla_2, Bangla, "  Grade point = 4.00, Grade = A ")
    elif(Bangla>=60 and Bangla<=69):
        print("Bangla         " ,Bangla_1,  Bangla_2 , Bangla ,"  Grade point = 3.50, Grade = A- ")
    elif(Bangla>=50 and Bangla<=59):
        print("Bangla         ", Bangla_1, Bangla_2,  Bangla, "  Grade point = 3.00, Grade = B ")
    elif(Bangla>=40 and Bangla<=49):
        print("Bangla         " ,Bangla_1,  Bangla_2, Bangla, "  Grade point = 2.00, Grade = C ")
    elif(Bangla>=33 and Bangla<=39):
        print("Bangla         " ,Bangla_1, Bangla_2, Bangla, "  Grade point = 1.00, Grade = D ")
    else:
        print("Bangla         " ,Bangla_1, Bangla_2 ,Bangla, "  Grade point = 0.00, Grade = F ")

if (English>80 and English<100):
     print("English         ",Eng_1,Eng_2,English," Grade point = 5, Grade = A+"),
elif(English<0 or English>100):
        print("English        ",Eng_1, Eng_2, English,"  Grade point = Invalid, Grade = Invalid")
else:
    if(English>=70 and English<=79):
        print("English        " ,Eng_1  ,Eng_2, English, "  Grade point = 4.00, Grade = A ")
    elif(English>=60 and English<=69):
        print("English        " ,Eng_1,  Eng_2 , English ,"  Grade point = 3.50, Grade = A- ")
    elif(English>=50 and English<=59):
        print("English        ", Eng_1, Eng_2,  English, "  Grade point = 3.00, Grade = B ")
    elif(English>=40 and English<=49):
        print("English       " ,Eng_1,  Eng_2, English, "  Grade point = 2.00, Grade = C ")
    elif(English>=33 and English<=39):
        print("English       " ,Eng_1, Eng_2, English, "  Grade point = 1.00, Grade = D ")
    else:
        print("English       " ,Eng_1, Eng_2 ,English, "  Grade point = 0.00, Grade = F ")


if(General_Math> 80 and General_Math<100):
     print("General_Math         ",General_Math,"    Grade point = 5.00, Grade = A+")
elif(General_Math<0 or General_Math>100):
     print("General_Math         ",General_Math, "    Grade point = Invalid, Grade = Invalid")    
else:
    if(General_Math>70 and General_Math<79):
        print("General_Math         ",General_Math,"    Grade point = 4.00, Grade = A")
    elif(General_Math>60 and General_Math<69):
        print("General_Math         ",General_Math,"    Grade point = 3.50, Grade = A-")
    elif(General_Math>50 and General_Math<59):
        print("General_Math         ",General_Math,"    Grade point = 3.00, Grade = B")
    elif(General_Math>40 and General_Math<49):
        print("General_Math         ",General_Math,"    Grade point = 2.00, Grade = C")
    elif(General_Math>33 and General_Math<39):
        print("General_Math         ",General_Math,"    Grade point = 1.00, Grade = D")
    else:
        print("General_Math         ",General_Math,"    Grade point = 0.00, Grade = F")    


if(Higher_Math> 80 and Higher_Math<100):
     print("Higher_Math          ",Higher_Math,"    Grade point = 5.00, Grade = A+")
elif(Higher_Math<0 or Higher_Math>100):
     print("Higher_Math        ",Higher_Math, "    Grade point = Invalid, Grade = Invalid")    
else:
    if(Higher_Math>70 and Higher_Math<79):
        print("Higher_Math          ",Higher_Math,"    Grade point = 4.00, Grade = A")
    elif(Higher_Math>60 and Higher_Math<69):
        print("Higher_Math          ",Higher_Math,"    Grade point = 3.50, Grade = A-")
    elif(Higher_Math>50 and Higher_Math<59):
        print("Higher_Math          ",Higher_Math,"    Grade point = 3.00, Grade = B")
    elif(Higher_Math>40 and Higher_Math<49):
        print("Higher_Math          ",Higher_Math,"    Grade point = 2.00, Grade = C")
    elif(Higher_Math>33 and Higher_Math<39):
        print("Higher_Math          ",Higher_Math,"    Grade point = 1.00, Grade = D")
    else:
        print("Higher_Math           ",Higher_Math,"    Grade point = 0.00, Grade = F")    


if(Biology> 80 and Biology<100):
     print("Biology              ",Biology,"    Grade point = 5.00, Grade = A+")
elif(Biology<0 or Biology>100):
     print("Biology            ",Biology, "    Grade point = Invalid, Grade = Invalid")    
else:
    if(Biology>70 and Biology<79):
        print("Biology              ",Biology,"    Grade point = 4.00, Grade = A")
    elif(Biology>60 and Biology<69):
        print("Biology              ",Biology,"    Grade point = 3.50, Grade = A-")
    elif(Biology>50 and Biology<59):
        print("Biology              ",Biology,"    Grade point = 3.00, Grade = B")
    elif(Biology>40 and Biology<49):
        print("Biology              ",Biology,"    Grade point = 2.00, Grade = C")
    elif(Biology>33 and Biology<39):
        print("Biology              ",Biology,"    Grade point = 1.00, Grade = D")
    else: 
        print("Biology              ",Biology,"    Grade point = 0.00, Grade = F")    

if(Physics> 80 and Physics<100):
     print("Physics              ",Physics,"    Grade point = 5.00, Grade = A+")
elif(Physics<0 or Physics>100):
     print("Physics             ",Physics, "    Grade point = Invalid, Grade = Invalid")    
else:
    if(Physics>70 and Physics <79):
        print("Physics              ",Physics,"    Grade point = 4.00, Grade = A")
    elif(Physics>60 and Physics<69):
        print("Physics              ",Physics,"    Grade point = 3.50, Grade = A-")
    elif(Physics>50 and Physics<59):
        print("Physics              ",Physics,"    Grade point = 3.00, Grade = B")
    elif(Physics>40 and Physics<49):
        print("Physics              ",Physics,"    Grade point = 2.00, Grade = C")
    elif(Physics>33 and Physics<39):
        print("Physics              ",Physics,"    Grade point = 1.00, Grade = D")
    else:
        print("Physics              ",Physics,"    Grade point = 0.00, Grade = F")  

if(Chemistry> 80 and Chemistry<100):
     print("Chemistry            ",Chemistry,"    Grade point = 5.00, Grade = A+")
elif(Chemistry<0 or Chemistry>100):
     print("Chemistry           ",Chemistry, "    Grade point = Invalid, Grade = Invalid")    
else:
    if(Chemistry>70 and Chemistry<79):
        print("Chemistry            ",Chemistry,"    Grade point = 4.00, Grade = A")
    elif(Chemistry>60 and Chemistry<69):
        print("Chemistry            ",Chemistry,"    Grade point = 3.50, Grade = A-")
    elif(Chemistry>50 and Chemistry<59):
        print("Chemistry            ",Chemistry,"    Grade point = 3.00, Grade = B")
    elif(Chemistry>40 and Chemistry<49):
        print("Chemistry            ",Chemistry,"    Grade point = 2.00, Grade = C")
    elif(Chemistry>33 and Chemistry<39):
        print("Chemistry            ",Chemistry,"    Grade point = 1.00, Grade = D")
    else:
        print("Chemistrty           ",Chemistry,"    Grade point = 0.00, Grade = F")  

if(Islamic_Religion> 80 and Islamic_Religion<100):
     print("Islamic_Religion     ",Islamic_Religion,"    Grade point = 5.00, Grade = A+")
elif(Islamic_Religion<0 or Islamic_Religion>100):
     print("Islamic_Religion    ",Islamic_Religion, "    Grade point = Invalid, Grade = Invalid")    
else:
    if(Islamic_Religion>70 and Islamic_Religion<79):
        print("Islamic_Religion     ",Islamic_Religion,"    Grade point = 4.00, Grade = A")
    elif(Islamic_Religion>60 and Islamic_Religion<69):
        print("Islamic_Religion     ",Islamic_Religion,"    Grade point = 3.50, Grade = A-")
    elif(Islamic_Religion>50 and Islamic_Religion<59):
        print("Islamic_Religion     ",Islamic_Religion,"    Grade point = 3.00, Grade = B")
    elif(Islamic_Religion>40 and Islamic_Religion<49):
        print("Islamic_Religion     ",Islamic_Religion,"    Grade point = 2.00, Grade = C")
    elif(Islamic_Religion>33 and Islamic_Religion<39):
        print("Islamic_Religion      ",Islamic_Religion,"    Grade point = 1.00, Grade = D")
    else:
        print("Islamic_Religion     ",Islamic_Religion,"    Grade point = 0.00, Grade = F")         

if(Social_science> 80 and Social_science<100):
     print("Social_science       ",Social_science,"    Grade point = 5.00, Grade = A+")
elif(Social_science<0 or Social_science>100):
     print("Social_science      ",Social_science, "    Grade point = Invalid, Grade = Invalid")    
else:
    if(Social_science>70 and Social_science<79):
        print("Social_science       ",Social_science,"    Grade point = 4.00, Grade = A")
    elif(Social_science>60 and Social_science<69):
        print("Social_science       ",Social_science,"    Grade point = 3.50, Grade = A-")
    elif(Social_science>50 and Social_science<59):
        print("Social_science       ",Social_science,"    Grade point = 3.00, Grade = B")
    elif(Social_science>40 and Social_science<49):
        print("Social_science       ",Social_science,"    Grade point = 2.00, Grade = C")
    elif(Social_science>33 and Social_science<39):
        print("Social_science       ",Social_science,"    Grade point = 1.00, Grade = D")
    else:
        print("Social_science       ",Social_science,"    Grade point = 0.00, Grade = F")  


if(ICT> 80 and ICT<100):
     print("        ICT          ",ICT,"    Grade point = 5.00, Grade = A+")
elif(ICT<0 or ICT>100):
     print("        ICT         ",ICT, "    Grade point = Invalid, Grade = Invalid")    
else:
    if(ICT>70 and ICT <79):
        print("ICT                  ",ICT,"    Grade point = 4.00, Grade = A")
    elif(ICT>60 and ICT<69):
        print("ICT                  ",ICT,"    Grade point = 3.50, Grade = A-")
    elif(ICT>50 and ICT<59):
        print("ICT                  ",ICT,"    Grade point = 3.00, Grade = B")
    elif(ICT>40 and ICT<49):
        print("ICT                  ",ICT,"    Grade point = 2.00, Grade = C")
    elif(ICT>33 and ICT<39):
        print("ICT                  ",ICT,"    Grade point = 1.00, Grade = D")
    else:
        print("ICT                  ",ICT,"    Grade point = 0.00, Grade = F")  
       