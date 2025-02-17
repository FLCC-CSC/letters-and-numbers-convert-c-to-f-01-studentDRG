# FILE NAME - convertCF01.py

# NAME - 
# DATE - 
# DESCRIPTION - 

def main():
    convertCF()

def convertCF():
    temp = float(input('Enter a temperature in Celsius: '))
    newTemp = temp * 9 / 5 + 32
    print()
    print(temp, 'degrees Celsius is', newTemp, 'degrees Fahrenheit.')

main()
