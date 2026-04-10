from hex_to_bin import hex_to_bin
from binary_to_text import binary_to_text
from base64_decode import base64_decode
from caesar_bruteforce import caesar_bruteforce


def morse_code(fileinput):
    morse_to_char = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7',
        '---..': '8', '----.': '9', "--..--":","
    }

    with open(fileinput) as f:
        text=f.read().split(" ")
    result=""
    for c in text:
        #print(c)
        result+=morse_to_char.get(c).lower()
    #print(result)

    result= hex_to_bin(result)

    #print(result)
    result=result.decode('utf-8')
    #print(result)
    result=binary_to_text(result)
    #print(result)
    result=base64_decode(result)
    #print(result)
    result=result.decode('utf-8')
    return caesar_bruteforce(result)


def main():    print(f"Level 11: {morse_code("morse_code.txt")}")

if __name__ == "__main__": main()

