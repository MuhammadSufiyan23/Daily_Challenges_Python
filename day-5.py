# DAY-5 CHALLENGE

num = int(input("Enter a number: "))

total = 0
numbers = []  

for i in range(1, num + 1):
    total += i
    numbers.append(str(i)) 

print("Result Is: 👇\n")
print(f"Sum: {total} ({' + '.join(numbers)} = {total})")
