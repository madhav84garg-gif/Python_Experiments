##Q8) Convert lowercase to uppercase
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch >= 'a' and ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch

print("Uppercase String:", result)