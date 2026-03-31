def encrypt(text: str, key: int) -> str:
    result=""
    for c in text:
        if not c.isalpha():
            result += c
            continue
        ascii_code = ord(c)
        match ascii_code:
            case (a) if a<=90 :
                result += chr((ascii_code-65+key)%26+65)
            case (a) if a>=97:
                result += chr((ascii_code - 97 + key) % 26 + 97)

    return result






def main():
    key = input("inserire la chiave da utilizzare (positiva per cryptare, negativa per decryptare): ")
    while not key.strip("-").isnumeric():
        print("chiave non valida, deve essere un numero\n")
        key = input("inserire la chiave da utilizzare (positiva per cryptare, negativa per decryptare): ")
    key = int(key)
    text = input("inserisci il testo da cryptare/decryptare: ")
    result_text= encrypt(text, key)
    print(result_text)


main()