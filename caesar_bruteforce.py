from caesar_cipher import *

def caesar_bruteforce(text:str):
    list=[]
    result=""
    for i in range(1,26,1):
        result=encrypt(text,int(i))
        list.append(result)
        if "flag" in result:
            return result

    return list