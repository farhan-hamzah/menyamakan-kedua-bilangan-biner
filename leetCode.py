start = int(input())
goal = int(input())
i = 1
b = 1
result = 0
result2 = 0
while start > 0:
    if start%2 != 0:
        result = result + i
    start //= 2
    i *= 10
while goal > 0:
    if goal%2 != 0:
        result2 = result2 + b
    goal //= 2
    b *= 10
steps = 0
while result != result2:
    if result % 10 != result2 % 10:
        steps += 1
    result //= 10
    result2 //= 10
print(steps)