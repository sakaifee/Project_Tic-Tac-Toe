h1=['_','_','_'];h2=['_','_','_'];h3=['_','_','_']
v1=['_','_','_'];v2=['_','_','_'];v3=['_','_','_']
d1=['_','_','_'];d2=['_','_','_']

H=[h1,h2,h3];V=[v1,v2,v3]
L=[h1,h2,h3,v1,v2,v3,d1,d2];Ls=[0,0,0,0,0,0,0,0]

R=[];C=[]

names={'p1':'player1','p2':'player2','p':'player','c':'computer'}
choice=['X','O']
signs={}

import random
def printgrid():                                                                           #used to display the game grid
 print(1,'-',2,'-',3)
 print(h1[0],'|',h1[1],'|',h1[2],1)
 print('--+---+--','|')
 print(h2[0],'|',h2[1],'|',h2[2],2)
 print('--+---+--','|')
 print(h3[0],'|',h3[1],'|',h3[2],3)

printgrid()
GM=int(input('select game mode:-  1)Player1 vs Player 2)Player vs Computer'))              #switching game mode
while GM not in (1,2):
  GM=int(input('enter 1 or 2  1)Player1 vs Player 2)Player vs Computer  '))  
if GM==1:                                                                                      
  s=str(input('Player1, choose your symbol out of X and O and enter it'))                  #choosing symbols
  while s not in choice:
   s=str(input('please enter one out of X and O only, be careful about the case'))
  signs['p1']=s
  signs['p2']=choice[1-choice.index(s)]
  ap='p1'
elif GM==2:
  s=str(input('choose your symbol out of X and O and enter it'))                            #choosing symbols
  while s not in choice:                                                    
   s=str(input('please enter one out of X and O only. be careful about the case'))
  signs['p']=s
  signs['c']=choice[1-choice.index(s)]
  ap=str(input('who do you want to play first?? enter p for player enter c for computer'))   #deciding the 1st active player
  while ap not in ('p','c'):
    ap=str(input('who do you want to play first?? enter p for player enter c for computer'))


 
  
def Lanalyse():                                                 #used to analyse status of all lines
 i=0
 while i<=7:
  l=L[i]
  if l.count('_')==3:
   Ls[i]=0
  elif l.count('_')==2:
   if l.count(signs[ap])==0:
    Ls[i]=1
   elif l.count(signs[ap])==1:
    Ls[i]=2
  elif l.count('_')==1:
   if l.count(signs[ap])==0:
    Ls[i]=3
   elif l.count(signs[ap])==1:
    Ls[i]=4
   elif l.count(signs[ap])==2:
    Ls[i]=5
  elif l.count('_')==0:
   if l.count(signs[ap])==1 or l.count(signs[ap])==2:
    Ls[i]=6
   else:
    Ls[i]=7     
  i+=1


printgrid()
Gstatus='continue'
while Gstatus=='continue':
 print('its',names[ap]+"'s",'turn')
 
 if  GM==2 and ap=='p' or GM==1:                       #input method for player(s)
  inpstat='retry'
  while inpstat=='retry': 
   r=int(input('enter row number'))
   while r not in range(1,4):
     print('Invalid input')
     r=int(input('please enter row number between 1 and 3'))
   c=int(input('enter column number'))
   while c not in range(1,4):
     print('Invalid input')
     c=int(input('please enter column number between 1 and 3'))
   if (H[r-1])[c-1]!='_':
     print('This place is already occupied,you cant overwrite it')
     inpstat='retry'
   else:
     inpstat='done'
 elif GM==2 and ap=='c':                                #input method for computer(s)
  Lanalyse()
  if 5 in Ls:
    wind=Ls.index(5)
    if wind in range(0,3):
     r=wind+1
     c=(L[wind]).index('_')+1
    elif wind in range(3,6):
     c=wind-2
     r=(L[wind]).index('_')+1
    elif wind==6:
     r=d1.index('_')+1
     c=r
    elif wind==7:
     c=d2.index('_')+1
     r=4-c
  else:
   ri=0   
   while ri<=2:
    ei=0
    while ei<=2:
     if (H[ri])[ei]=='_':
      R.append(ri+1)
      C.append(ei+1)
      ei+=1
     else:
      ei+=1  
    ri+=1      
   ind=random.randint(0,len(R)-1)
   r=R[ind]
   c=C[ind]
   R.clear();C.clear()
  

 Hg=H[r-1];Hg[c-1]=signs[ap];
 Vg=V[c-1];Vg[r-1]=signs[ap];
 if r*c==9 or r*c==1:
   d1[r-1]=signs[ap]
 elif r*c==3:
   d2[c-1]=signs[ap]
 elif r*c==4:
   d1[1]=signs[ap]
   d2[1]=signs[ap]
 
    
 printgrid()
 Lanalyse()    
 
 if 7 in Ls:
   print(names[ap],'wins')
   Gstatus='complete'
 elif 0 not in Ls and 1 not in Ls and 2 not in Ls and 3 not in Ls and 5 not in Ls:
   print('this game is a tie')
   Gstatus='complete'
 elif 0 in Ls or 1 in Ls or 2 in Ls or 3 in Ls or 5 in Ls:
   if GM==1: 
    if ap=='p1':
      ap='p2'
    elif ap=='p2':
      ap='p1'
   elif GM==2:
    if ap=='p':
      ap='c'
    elif ap=='c':
      ap='p'  
   Gstatus='continue'   

if Gstatus=='complete':
 print('THANKS FOR PLAYING')  


