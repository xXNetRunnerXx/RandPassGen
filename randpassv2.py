'''
Generate random pass 
validate the password then salt the password.
Pass the salted password to another function
to hash it with an encryption. 
'''
import os
import random
import hashlib
import re

def rpass():
    passlen = int(input("enter the length of password"))
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    
    pass_gen =  "".join(random.sample(s,passlen,))
    #a = int(passlen)
    #j = passlen(input)
    
    validator = 0
    while True:
        if (len(pass_gen)<8):
            validator = -1
            break
        elif not re.search("[a-z]", pass_gen):
            validator = -1
            break
        elif not re.search("[A-Z]", pass_gen):
            validator = -1
            break
        elif not re.search("[0-9]", pass_gen):
            validator = -1
            break
        elif not re.search("[_@$]", pass_gen):
            validator = -1
            break
        elif re.search("\s", pass_gen):
            validator = -1
            break
        else:
            validator = 0
            print("Valid Password")
            break
    if validator ==-1:
        print("Not Valid pass")     

    else: 
        return pass_gen 


salt = os.urandom(32)
passinput = rpass().encode()

hasher = hashlib.pbkdf2_hmac('sha256', passinput, salt, 10000)

hex_hash = hasher.hex()
print(hex_hash)

byte_hash = hasher.fromhex(hasher.hex())
print(byte_hash)


