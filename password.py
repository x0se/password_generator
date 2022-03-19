import random 

chars = "abcdefghijklmnoprstuvyxyzABCDEFGHIJKLMNOPRSTUVYZ0123456789!$@#&/([]}{=?.-"

for i in range(100):
    first = "".join((random.choice(chars) for i in range(7)))
    second = "".join((random.choice(chars) for i in range(7)))
    third = "".join((random.choice(chars) for i in range(7)))

    result = first + "" + second + "" + third 

    output = open("password.txt", "a")
    output.write(result + "\n")