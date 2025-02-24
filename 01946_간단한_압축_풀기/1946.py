t = int(input())

result = []

for _ in range(t):
    n = int(input())
    
    word = ""
    for _ in range(n):
        alphabet, num = input().split()
        num = int(num)
        word += alphabet * num
    
    result.append(word)
    
for step, elem in enumerate(result):
    print("#", step + 1, sep = "")
    
    for idx, c in enumerate(elem):
        print(c, end="")
        if (idx + 1) % 10 == 0:
            print()
    
    print()