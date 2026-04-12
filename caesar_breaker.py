from caesar_cipher import *

def brute_force(ciphertext:str)-> list[tuple[int, str]]:
    lista=[]
    result=""
    for i in range(0,26):
        result=encrypt(ciphertext,-i)
        lista.append((i, result))
        #if "flag" in result:
        #   return result

    return lista


def main():
    text=input("inserisci il testo cifrato: ")
    result=brute_force(text)
    for element in result:
        print(f"Chiave: {element[0]} -> {element[1]}")
        
if __name__ == "__main__":  
    main()