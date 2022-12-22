import random

randomChars = ["a", "b", "c", "d", "e", "f","g","h","i","j","k"
               "l","m","n","o","p","q","r","s","t","u","v","w","x","y",
               "z",",",".","<",">","?","/",";",":","[","]","{","}","|",
               "1","2","3","4","5","6","7","8","9","0","!","@","#",
               "$","%","^","&","*","(",")"]

password = ""

for char in range(random.randint(8,15)):
    num = random.randint(0,59)
    password = password + randomChars[num]

print(password)
    
    




