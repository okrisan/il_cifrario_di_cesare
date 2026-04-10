def encrypt(text: str, key: int) -> str:
    result=""
    for c in text:
       # if not c.isalpha():
        #     result += c
        #     continue
        ascii_code = ord(c)
        match ascii_code:
            case (a) if 65<=a<=90 :
                result += chr((ascii_code-65+key)%26+65)
            case (a) if 97<=a<=122 :
                result += chr((ascii_code - 97 + key) % 26 + 97)
            case _:
                result += c


    return result






def main() -> None:
    key = input("inserire la chiave da utilizzare (positiva per cryptare, negativa per decryptare): ")
    while not key.strip("-").isnumeric():
        print("chiave non valida, deve essere un numero\n")
        key = input("inserire la chiave da utilizzare (positiva per cryptare, negativa per decryptare): ")
    key = int(key)
    text = input("inserisci il testo da cryptare/decryptare: ")
    result_text= encrypt(text, key)
    print(result_text)

if __name__ == "__main__":
    main()