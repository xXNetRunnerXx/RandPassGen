import random

def rpass(passlen, s, e, p):
    passlen = int(input("enter the length of password"))
    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    e = "_%&$@"
    p =  "".join(random.sample(s,e, passlen ))

    if passlen < 7:
        print (p)
    else: 
        print (p)

