t = int(input())           # test cases — always int()
for _ in range(t):
    n = int(input())        # single number — int()
    arr = list(map(int, input().split()))   # array on one line
    freq= {}
    for num in arr:
        freq[num] = freq.get(num,0) +1
        
    for i,num in enumerate(arr):
        if freq[num] == 1:
            print(i+1)
            break