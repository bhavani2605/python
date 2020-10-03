#Reverse number s
print('******Basics steps to understand Reverse Number********')

print('''Assume n = 123.
Multiply n with 10 i.e. n = n * 10 = 1230.
Add the first digit to the resultant number i.e. 1230 + 1 = 1231.
Subtract (first digit) * 10k from the resultant number where k is the number of digits in the original number (in this case, k = 3).
1231 – 1000 = 231 is the left shift number of the original number.''')



# find no of digits entered

def NoOfDigits(n):
    cnt=0
    while n>0:
        cnt+=1
        n//=10
    return cnt

#print the left shift numbers 

def Reverse(num):
    digit= NoOfDigits(num)
    powTen= pow(10,digit-1)
    #print('powTen',powTen)
    for i in range(digit -1):
        firstDigit =num// powTen
        #print('firstdigit',firstDigit)
        left =(num*10+firstDigit-(firstDigit*powTen*10))
        print(left,end=" ")
        num = left
    

num1 = int(input('Please enter the first number: '))
Reverse(num1)
