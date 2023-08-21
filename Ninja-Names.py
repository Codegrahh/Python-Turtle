letters={
 'A':['SHI'],
 'B':['ARI'],
 'C':['CHI'],
 'D':['DO'],
 'E':['RU'],
 'F':['MEI'],
 'G':['MA'],
 'H':['FU'],
 'I':['ZI'],
 'J':['KA'],
 'K':['ZU'],
 'L':['MI'],
 'M':['TE'],
 'N':['KU'],
 'O':['LI'],
 'P':['JI'],
 'Q':['RI'],
 'R':['KI'],
 'S':['ZE'],
 'T':['ME'],
 'U':['TA'],
 'V':['RIN'],
 'W':['TO'],
 'X':['KE'],
 'Y':['NO'],
 'Z':['MO']
}
#Taking User Input - Name
string=input("Enter Your name : ")
print("Your Ninja Name is : ",end="")
#loop for changing english letters -----> Ninja letters
for i in range(1):
 for word in range(len(string)):
  n=string[word].upper()        #Incase user given input in lowercase it will convert 
  if word==len(string)-1:
   print(letters[n][i])
  else:
   print(letters[n][i],end="")