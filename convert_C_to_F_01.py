# FILE NAME - convertCF01.py
# DRG - Rerun for points 2025-02-18-2351
# NAME - 
# DATE - 
# DESCRIPTION - 



def main():
    convertCF()

def convertCF():
    temp = float(input('Enter a temperature in Celsius: '))
    newTemp = temp * 9 / 5 + 32
    print()
    print(temp, 'degreeeees Celsius is', newTemp, 'degrees Fahrenheit.')

main()



