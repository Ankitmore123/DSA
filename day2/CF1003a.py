n = int(input())
arr = list(map(int, input().split()))
freq= {}
max_freq =0 
for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]]+=1
    else:
        freq[arr[i]] =1
    if freq[arr[i]]>max_freq:
        max_freq = freq[arr[i]]
print(max_freq)