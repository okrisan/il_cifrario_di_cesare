from caesar_cipher import *

def caesar_bruteforce(text:str)-> str | list[str]:
    lista=[]
    result=""
    for i in range(1,26,1):
        result=encrypt(text,int(i))
        lista.append(result)
        if "flag" in result:
            return result

    return lista