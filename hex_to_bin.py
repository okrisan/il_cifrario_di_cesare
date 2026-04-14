def hex_to_bin(hex_string: str) -> bytes:
    hex_list=hex_string.replace(","," ").replace("0x","")
    result=bytes.fromhex(hex_list)


    return result



if __name__=="__main__":
    string=input("Enter a string: ")
    print(hex_to_bin(string))