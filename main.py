num = 50
print("Bin of", num, "=", bin(num)[2:])
count = 0
while num > 0:
    count += 1
    num = num >> 1
print(count)