#29. Median of Three
i = 0
arr = [0] * 3
#Put number in array
while (i < 3):
    arr[i] = int(input())
    i += 1
#Arrange number in array
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
#Print Median
print(arr[1])