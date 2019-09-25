from roman_converter import Converter

def main():
    while True:
        number = int(input("Digiete um número: "))
        conv = Converter(number)
        roman_number = conv.convert()
        print(roman_number)

if __name__=='__main__':
    main()