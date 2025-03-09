# DAY-6 CHALLENGE

def is_binary_palindrome(n: int) -> bool:
    binary = bin(n)[2:]  
    return binary == binary[::-1]  


num = int(input("Enter a number: "))


binary_rep = bin(num)[2:]
if is_binary_palindrome(num):
    print(f"Input: {num}")
    print(f"Binary: {binary_rep}")
    print("It's a Palindrome ✅")
else:
    print(f"Input: {num}")
    print(f"Binary: {binary_rep}")
    print("It's Not a Palindrome ❌")
