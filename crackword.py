#Things todo: 

#Made by Raheem Idowu for a science fair in Birralee International School in April 2016.
#Shared under any license. Use your "sense"! ;D

#Imports. Need time and sound. Remember to plug your batteries in! :D
import time
import winsound
import sys

#Set up variables.
aof = 0 #Comb counter
passwordfound = False #Has to be False. Becomes true when password found
timeout = False #Has to be False. Becomes true when the time is out
list = ["q","w","e","r","t","y","u","i","o","p","å","a","s","d","f","g","h","j","k","l","ø","æ","å","z","x","c","v","b","n","m","1","2","3","4","5","6","7","8","9","0"," "]
whitelist = ["password","123456","1234567","1234","qwerty","12345"]
maxtime = 1000000000000000 #In seconds. Time failsafe. Will make timeout true if this amount of seconds passes.
timeofend = False #The time that the password gets cracked. Its time.time() so watch out.
maxlength = 8 #Change this to add a mex password length failsafe
hasnumbers = False


#Gotta print stuff
print("Made by the to be master programmer Rahoom for the Birralee International School Science fair.")
print("Only numbers and letters. Read my report or talk to me if you have questions. Please do not use special signs like @ # %")

#input and time start
print("Write your password:")
inputpassword = input() #
password = inputpassword.lower() #Computer isn't strong enough to do caps but cheating is allowed.
PASSLEN = len(password) #For the maxlength failsafe
timeofstart = time.time() #Get the start of time

for whitepassword in whitelist:
	if password == whitepassword:
		print("This password is on the popular password whitelist. You really need to change it!!!!!! ")
		sys.exit()


if PASSLEN >= maxlength: #Length failsafe
        timeout = True #timeout triggered

#Classic brute force. Could be remade to be better and more effiecent.

for a in list:
        if passwordfound or timeout: #If done skip
                break
        #print(a)
        aof = aof + 1 #Add a comb to our counter
        if (time.time() - timeofstart) > maxtime: #Check for maxtime failsafe
                timeout = True #timeout triggered
                break
        if a == password:
                timeofend = time.time()
                passwordfound = True


if not passwordfound or not timeout:
         for a in list:
                if passwordfound or timeout:
                        break
                for b in list:
                        if passwordfound or timeout:
                                break
                        if (time.time() - timeofstart) > maxtime:
                                timeout = True
                                break
                        #print(a+b)
                        aof = aof + 1
                        if a+b == password:
                                timeofend = time.time()
                                passwordfound = True
        
if not passwordfound or not timeout:
        for a in list:
                if passwordfound or timeout:
                        break
                for b in list:
                        if passwordfound or timeout:
                                break
                        for c in list:
                                if passwordfound or timeout:
                                        break
                                if (time.time() - timeofstart) > maxtime:
                                        timeout = True
                                        break
                                #print(a+b+c)
                                aof = aof + 1
                                if a+b+c == password:
                                        timeofend = time.time()
                                        passwordfound = True

if not passwordfound  or not timeout:
        for a in list:
                if passwordfound or timeout:
                        break
                for b in list:
                        if passwordfound or timeout:
                                break
                        for c in list:
                                if passwordfound or timeout:
                                        break
                                for d in list:
                                        if (time.time() - timeofstart) > maxtime:
                                                timeout = True
                                                break
                                        #print(a+b+c+d)
                                        aof = aof + 1
                                        if a+b+c+d == password:
                                                timeofend = time.time()
                                                passwordfound = True

if not passwordfound  or not timeout:
        for a in list:
                if passwordfound or timeout:
                        break
                for b in list:
                        if passwordfound or timeout:
                                break
                        for c in list:
                                if passwordfound or timeout:
                                        break
                                for d in list:
                                        if passwordfound or timeout:
                                                break
                                        for e in list:
                                                if (time.time() - timeofstart) > maxtime:
                                                        timeout = True
                                                        break
                                                #print(a+b+c+d+e)
                                                aof = aof + 1
                                                if a+b+c+d+e == password:
                                                        timeofend = time.time()
                                                        passwordfound = True

if not passwordfound  or not timeout:
        for a in list:
                if passwordfound or timeout:
                        break
                for b in list:
                        if passwordfound or timeout:
                                break
                        for c in list:
                                if passwordfound or timeout:
                                        break
                                for d in list:
                                        if passwordfound or timeout:
                                                break
                                        for e in list:
                                                if passwordfound or timeout:
                                                        break
                                                for f in list:
                                                        if (time.time() - timeofstart) > maxtime:
                                                                timeout = True
                                                                break
                                                        #print(a+b+c+d+e+f)
                                                        aof = aof + 1
                                                        if a+b+c+d+e+f == password:
                                                                timeofend = time.time()
                                                                passwordfound = True

if not passwordfound  or not timeout:
        for a in list:
                if passwordfound or timeout:
                        break
                for b in list:
                        if passwordfound or timeout:
                                break
                        for c in list:
                                if passwordfound or timeout:
                                        break
                                for d in list:
                                        if passwordfound or timeout:
                                                break
                                        for e in list:
                                                if passwordfound or timeout:
                                                        break
                                                for f in list:
                                                        if passwordfound or timeout:
                                                                break
                                                        for g in list:
                                                                if (time.time() - timeofstart) > maxtime:
                                                                        timeout = True
                                                                        break
                                                                #print(a+b+c+d+e+f+g)
                                                                aof = aof + 1
                                                                if a+b+c+d+e+f+g == password:
                                                                        timeofend = time.time()
                                                                        passwordfound = True
        

        
        
			

        


#Get time and find a correct mesaurement!
if timeofend:
        Timetaken = timeofend - timeofstart
else:
        Timetaken = time.time() - timeofstart
inmilis = Timetaken * 100
inminis = Timetaken / 60
	
if Timetaken > 1:
        displayedtime = Timetaken
        unit = "seconds"      
if Timetaken < 1:
        displayedtime = inmilis
        unit = "miliseconds"
if Timetaken > 60:
        displayedtime = inminis
        unit = "minutes"

#Play sound
winsound.Beep(1000, 1000)

#Check for exception(time over or too long password
if timeout:
        print("Time out or password too long! Good password.")
        time.sleep(300)

#Feed back.
if passwordfound:
       		print("It took this average computer ", displayedtime , " ", unit, " to crack your password after trying", aof, "combinations."  )
       		print("To make your password stronger:\n")
        	for i in password:
          		if i in ["1","2","3","4","5","6","7","8","9","0"]:
          			hasnumbers = True
       		if not hasnumbers:
          		print ("You can add numbers to increase variation.\n")
          		
        	if PASSLEN < 7:
          		print("I recommend that you change your password to at least 7 letters long.")
          	

else:
	print("Damn it. Didn't get the password. Do not use symbols that are not standard. Debug stuff: ", aof, " ", Timetaken)

#just to make you accually be able to see the output.
time.sleep(300)


#226 lines of code. DAMN SON
