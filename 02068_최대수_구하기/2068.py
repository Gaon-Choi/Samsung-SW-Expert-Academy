n = int(input())

result = []

for _ in range(n):
    result.append(max(list(map(int, input().split()))))
    
for idx, elem in enumerate(result):
    print("#{idx} {total}".format(idx = idx + 1, total = elem))