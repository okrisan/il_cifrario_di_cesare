import caesar_cipher
from hex_to_bin import*
from base64_decode import *
from caesar_breaker import *
from caesar_cipher import *
from morse_code import morse_code



def solve_level_1(text: str = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d") -> str:
    return hex_to_bin(text).decode('utf-8')

def solve_level_2(parte1: str | bytes = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE=", parte2: int = int("664813035583918006462745898431981286737635929725", 10)) -> str:
    numero_byte = (parte2.bit_length() + 7) // 8
    return f"{base64_decode(parte1).decode('utf-8')}{parte2.to_bytes(length=numero_byte, byteorder='big').decode('utf-8')}"

def solve_level_3(text: str | bytes = "NjY2YzYxNjc3YjZjMzQ3OTMzNzIzNTVmMzA2ZTVmNmMzNDc5MzM3MjM1N2Q=") -> str:
    result=base64_decode(text)
    result=result.decode('utf-8')
    result=hex_to_bin(result)
    result = result.decode('utf-8')
    return result

def solve_level_4(text: str | bytes = "Wm14aFozdGlOSE16WDNNeGVIUjVYMll3ZFhKZk1XNWpNM0IwTVRCdWZRPT0=") -> str:
    result = base64_decode(text)
    result=result.decode('utf-8')
    result = base64_decode(result).decode('utf-8')
    return result


def solve_level_5(text: str = "7d72337474346d5f73337479625f35647234776b6334627b67616c66") -> str:
    result = hex_to_bin(text)
    result = result.decode('utf-8')
    result = result[::-1]
    return result

def solve_level_6(text: str = "0066006c00610067007b007a003300720030005f00700034006400640031006e0067005f0033007600330072007900770068003300720033007d") -> str:
    result=text.replace("00","")
    result = hex_to_bin(result)
    result = result.decode('utf-8')
    return result

def solve_level_7(text: str = "4e6a5932597a59784e6a6333596a63304e6a67334d6a4d7a4d7a4d315a6a5a6a4d7a51334f544d7a4e7a49334d7a566d4e6a517a4d7a4d7a4e7a41335a413d3d") -> str:

    result = hex_to_bin(text)
    result = result.decode('utf-8')
    result = base64_decode(result)
    result = result.decode('utf-8')
    result = hex_to_bin(result)
    result = result.decode('utf-8')
    return result


def solve_level_8(text: str = "666c6167 | e20xeA== | 5f346e64 | X200dA== | 63685f33 | bmMwZA== | 316e6735 | fQ==") -> str:
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
    return result

def solve_level_9(text: str | bytes = "bXNobntqNDN6NHlfdDMzYXpfaTR6MzY0fQ==") -> str:
    result = base64_decode(text)
    result = result.decode('utf-8')
    result = brute_force(result)
    for element in result:
        if "flag" in element[1]:
            return element[1]
    

def solve_level_10(text: str | bytes = "pHSjnRW0lF9iW2AgIjXuHjXynP8jmtBpnDL5o2nrlQI=") -> str:
    result= encrypt(text, 16)
    result = base64_decode(result)
    result = result.decode('utf-8')
    result= result[::-1]
    #result = base64_decode(result)
    #for element in result:
    #    element = base64_decode(element)
    #    print(element)
    #result = result.decode('utf-8')
    #result=result.replace("\x","")
    return result

def solve_level_11(fileinput: str = "challenge_final_boss.txt") -> str:
    return morse_code(fileinput)

def main() -> None:
    print ("=== CTF Decoder ===")
    print(f"Level 1: {solve_level_1('666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d')}")
    print(f"Level 2: {solve_level_2('ZmxhZ3t3NDF0XzF0c19hbGxfYjE=', int('664813035583918006462745898431981286737635929725', 10))}")
    print(f"Level 3: {solve_level_3('NjY2YzYxNjc3YjZjMzQ3OTMzNzIzNTVmMzA2ZTVmNmMzNDc5MzM3MjM1N2Q=')}")
    print(f"Level 4: {solve_level_4('Wm14aFozdGlOSE16WDNNeGVIUjVYMll3ZFhKZk1XNWpNM0IwTVRCdWZRPT0=')}")
    print(f"Level 5: {solve_level_5('7d72337474346d5f73337479625f35647234776b6334627b67616c66')}")
    print(f"Level 6: {solve_level_6('0066006c00610067007b007a003300720030005f00700034006400640031006e0067005f0033007600330072007900770068003300720033007d')}")
    print(f"Level 7: {solve_level_7('4e6a5932597a59784e6a6333596a63304e6a67334d6a4d7a4d7a4d315a6a5a6a4d7a51334f544d7a4e7a49334d7a566d4e6a517a4d7a4d7a4e7a41335a413d3d')}")
    print(f"Level 8: {solve_level_8('666c6167 | e20xeA== | 5f346e64 | X200dA== | 63685f33 | bmMwZA== | 316e6735 | fQ==')}")
    print(f"Level 9: {solve_level_9('bXNobntqNDN6NHlfdDMzYXpfaTR6MzY0fQ==')}")
    print(f"Level 10: {solve_level_10('pHSjnRW0lF9iW2AgIjXuHjXynP8jmtBpnDL5o2nrlQI=')}")
    print(f"Level 11: {solve_level_11('challenge_final_boss.txt')}")


if __name__ == "__main__":    main()