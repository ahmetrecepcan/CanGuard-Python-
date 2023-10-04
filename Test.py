import random

CodeBOX = {"Numbers" : ["1","2","3","4","5","6","7","8","9","0"], "Letters" : ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","w","y","z"], "Markings" : ["&","+"]}

Code= ""
HeadTails= ["N","L","M"]
try:
    for index in range(1,7,1):
        if random.choice(HeadTails) == "N":
            Code += random.choice(CodeBOX["Numbers"])
        elif random.choice(HeadTails) == "L":
            Code += random.choice(CodeBOX["Letters"])
        else:
            Code += random.choice(CodeBOX["Markings"])
except e:
    print("Python Says: Something is wrong..."+str(e))
finally:
    with open("CanGuard_Code.txt","a+") as file:
        file.writelines("Your CanGuard Code : {}\n".format(str(Code.upper())))
    print("Your CanGuard Code is written in a file called CanGuard_Code.txt.")

##https://github.com/ahmetrecepcan