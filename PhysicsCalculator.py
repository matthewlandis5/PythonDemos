#Incomplete calculator for the AP Physics kinematic equations 

from decimal import Decimal
import math

Ufvel=int(input("Have Final Velocity? (yes=1 or no=0) "))
Uivel=int(input("Have Initial Velocity? "))
Udis=int(input("Have Distance? "))
Uacc=int(input("Have Acceleration? "))
Utime=int(input("Have Time? "))
print("")



if(Ufvel==1):fvel=Decimal(input("Final Velocity: "))
else:fvel=Decimal(-58217913)
if(Uivel==1):ivel=Decimal(input("Initial Velocity: "))
else:ivel=Decimal(-58217913)
if(Udis==1):dis=Decimal(input("Distance: "))
else:dis=Decimal(-58217913)
if(Uacc==1):acc=Decimal(input("Acceleration: "))
else:acc=Decimal(-58217913)
if(Utime==1):time=Decimal(input("Time: "))
else:time=Decimal(-58217913)

print("")

if(Ufvel+Uivel+Uacc+Utime==3):
  if(Ufvel==0):
    fvel=acc*time+ivel 
    Ufvel=1
  elif(Uivel==0):
    ivel=fvel-(acc*time)
    Uivel=1
  elif(Uacc==0):
    acc=(fvel-ivel)/time
    Uacc=1
  elif(Utime==0):
    time=(fvel-ivel)/acc 
    Utime=1

if(Udis+Uivel+Ufvel+Utime==3):
  if(Udis==0):
    dis=(ivel+fvel)*time/2
    Udis=1
  elif(Uivel==0):
    ivel=(2*dis/time)-fvel
    Uivel=1
  elif(Ufvel==0):
    fvel=(2*dis/time)-ivel
    Ufvel=1
  elif(Utime==0):
    time=(dis*2)/(ivel+fvel)
    Utime=1

if(Ufvel+Uivel+Uacc+Udis==3):
  if(Ufvel==0):
    fVel=math.sqrt(abs((ivel**2)+(2*acc*dis)))
    Ufvel=1
  elif(Uivel==0):
    iVel=math.sqrt((fvel**2)-(2*acc*dis))
    Uivel=1
  elif(Uacc==0):
    acc=((fvel**2)-(ivel**2))/(2*dis)
    Uacc=1
  elif(Udis==0):
    dis=((fvel**2)-(ivel**2))/(2*acc)
    Udis=1

if(Udis+Uivel+Utime+Uacc==3):
  if(Udis==0):
    dis=(ivel*time)+(acc*(time**2)/2)
    Udis=1
  if(Uivel==0):
    ivel=(dis-(acc*(time**2)/2))/time
    Uivel=1
  if(Uacc==0):
    acc=(dis-(ivel*time))*2/(time**2)
  if(Utime==0):
    print("I dont wanna solve for time using the last formula")

print("")
print("*Answers:* ")
if(fvel!=-58217913):print("Final Velocity: "+str(fvel))
if(ivel!=-58217913):print("Initial Velocity: "+str(ivel))
if(dis!=-58217913):print("Distance: "+str(dis))
if(acc!=-58217913):print("Acceleration: "+str(acc))
if(time!=-58217913):print("Time: "+str(time))
