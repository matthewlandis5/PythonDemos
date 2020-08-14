#

#@title Captures the Top Three Chars at each Position
!pip install --upgrade --quiet gspread
from google.colab import auth
auth.authenticate_user()

import gspread
from oauth2client.client import GoogleCredentials
gc = gspread.authorize(GoogleCredentials.get_application_default())
worksheet = gc.open('codes').sheet1
rows = worksheet.get_all_values()
#accesses the Google sheet with the codes and copies them to a var


for CHARLOCATION in range (0,14):
  possibleChar ='BFHJKLMNPRTVWX456790'
  first='a'
  firstC=-1
  second='a'
  secoudC=-1
  third='a'
  thirdC=-1
  List=[]
  hashMap={'1':-1}
  count=1


  #creates necessary vars


  for i in range(1,len(rows)):
    if(rows[i][2]=='Yes'):
      List.append(rows[i][0])
  #print(List)
    #adds the codes marked as valid to my new var


  for element in range(0, len(possibleChar)): 
      hashMap[possibleChar[element]]=0
  #print(hashMap)
    #makes a dict (called a hashmap in other languages) to hold the count for each character


  for i in range(len(List)):
    if(len(List[i])==14):
      hold=List[i][CHARLOCATION]
      if hold in {'8','U','S','G','O'}:
        if hold=='8':
          hashMap['B']=1+hashMap['B']
        elif hold=='U':
          hashMap['V']=1+hashMap['V']
        elif hold=='S':
          hashMap['5']=1+hashMap['5']
        elif hold=='G':
          hashMap['6']=1+hashMap['6']
        elif hold=='O':
          hashMap['0']=1+hashMap['0']
      elif hold in {'B','F','H','J','K','L','M','N','P','R','T','V','W','X','4','5','6','7','9','0'}:
        hashMap[hold]=1+hashMap[hold]
      #print('adding '+str(hold)+'  count of '+str(count))
      count+=1
  #print(hashMap)
    #rolls through the valid codes and counts the number of occurances for each character (taking into account the possible alternative characters)


  for element in range(0, len(possibleChar)): 
      temp=hashMap[possibleChar[element]]
      if(temp>firstC):
        firstC,secondC=temp,firstC
        first,second=possibleChar[element],first
      elif(temp>secondC):
        secondC,thirdC=temp,secondC
        second,third=possibleChar[element],second
      elif(temp>thirdC):
        thirdC=temp
        third=possibleChar[element]
  print(' ')
  print('The first most common at position '+str(CHARLOCATION)+': '+str(first)+' with: '+str(firstC))
  print('The second most common at position '+str(CHARLOCATION)+': '+str(second)+' with: '+str(secondC))
  print('The third most common at position '+str(CHARLOCATION)+': '+str(third)+' with: '+str(thirdC))
  #calculates the first and second most common characters found in the ten positions
