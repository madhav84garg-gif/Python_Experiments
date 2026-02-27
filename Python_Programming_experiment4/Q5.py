##Q5) Check whether number is palindrome
num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if rev == num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")