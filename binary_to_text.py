from caesar_cipher import main


def binary_to_text(binary_string):
    result=""
    bytevalue=0
    for i in range(0,len(binary_string),8):
        bytevalue=int(binary_string[i:i+8],2)
        result+=chr(bytevalue)
    return result


def main():
    bin="0110001100110011011011000111010101100100010010000111010001000100010100010101010101010110010501０００１０１０００１０１０１０１１００１００１０１００１１００１１００１０１０１０００１０００１１０００１１０００００１１００１₀₀₁₀₁₀₁₀₀₁₁₀₁₀₀₀₁₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₁₀₁₀₀₀₁₀₀₁₁₀₁₀₁₀₁₀₁₀₁₀₁₀₁₁₀₁₀₀₀₁₀₀₁₁₀₁₀₁₀₁₂"
    print(binary_to_text(bin))
if __name__ == "__main__": main()