import random

#alphabet, number and symbol for automatic passwod
lower = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
Upper = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
number = "0,1,2,3,4,5,6,7,8,9"
symbol = "!,,@,#,$,%,^,&,*,(,),_,-,+,=,?,/"


#formula for automatic password generator
total = lower + Upper + number + symbol

password = "" 

while len(password) < 8:
    password += random.choice(total)

#print
print(password)

