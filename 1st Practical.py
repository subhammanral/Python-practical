def factorial(n):
    if(n==0 or n<0):
        return 1
    else:
        return n*factorial(n-1)

def main():
    num1 = int(input('ENTER THE NUMBER: '))
    factor=factorial(num1)
    print('the factorial of the given number: ',factor)

if __name__ == '__main__':
    main()
        
