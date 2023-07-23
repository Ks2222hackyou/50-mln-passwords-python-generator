import random,keyboard, time

keys = ["1","2","3","5","6","7","8","9","0","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]

min_nums = 3
max_nums = 16

file = open("passwords.txt","w")



print(time.strftime("%H:%M:%S"))
for pas in range(50000000):
    
    pasw = ""

    
    for i in range(random.randint(min_nums,max_nums)):
        key = random.choice(keys)
        pasw = pasw + key
    

    
    file.write((f"{pasw}\n"))

print(time.strftime("%H:%M:%S"))