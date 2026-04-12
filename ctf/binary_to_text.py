from caesar_cipher import main


def binary_to_text(binary_string: str) -> str:
    result=""
    bytevalue=0
    for i in range(0,len(binary_string),8):
        bytevalue=int(binary_string[i:i+8],2)
        result+=chr(bytevalue)
    return result


def main() -> None:
    bin=input("Enter a binary string: ")
    print(binary_to_text(bin))
if __name__ == "__main__": main()