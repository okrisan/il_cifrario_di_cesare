from hex_to_bin import*
from base64_decode import *
from caesar_bruteforce import *
def solve_level_1(text:str):
    print(f"Level 1: {hex_to_bin(text)}")

def solve_level_2(parte1, parte2):
    numero_byte = (parte2.bit_length() + 7) // 8
    print(f"Level 2: {base64_decode(parte1)}{parte2.to_bytes(length=numero_byte, byteorder='big').decode('utf-8')}")

def solve_level_3(text):
    result=base64_decode(text)
    result=result.decode('utf-8')
    result=hex_to_bin(result)
    result = result.decode('utf-8')
    print(f"Level 3: {result}")

def solve_level_4(text):
    result = base64_decode(text)
    result=result.decode('utf-8')
    result = base64_decode(result)
    print(f"Level 4: {result}")


def solve_level_5(text):
    result = hex_to_bin(text)
    result = result.decode('utf-8')
    result = result[::-1]
    print(f"Level 5: {result}")

def solve_level_6(text):
    result=text.replace("00","")
    result = hex_to_bin(result)
    result = result.decode('utf-8')
    print(f"Level 6: {result}")

def solve_level_7(text):

    result = hex_to_bin(text)
    result = result.decode('utf-8')
    result = base64_decode(result)
    result = result.decode('utf-8')
    result = hex_to_bin(result)
    result = result.decode('utf-8')
    print(f"Level 7: {result}")


def solve_level_8(text):
    list = text.split("|")
    result=""
    for part in list:
        if "=" in part:
            part = base64_decode(part)
            part = part.decode('utf-8')
            result+=part
        else:
            part =hex_to_bin(part)
            part = part.decode('utf-8')
            result+=part
    print(f"Level 8: {result}")

def solve_level_9(text):
    result = base64_decode(text)
    result = result.decode('utf-8')
    result = caesar_bruteforce(result)
    print(result)

def solve_level_10(text):
    result = base64_decode(text)

    #result = result.decode('utf-8')
    #result=result.replace("\x","")
    print(result)


solve_level_10("pHSjnRW0lF9iW2AgIjXuHjXynP8jmtBpnDL5o2nrlQI===")