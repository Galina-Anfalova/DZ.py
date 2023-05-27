arr = [-10, 2, -9, 22, 31, -4, 2, 0, 12, -1, -3]
min = int(input())
max = int(input())
for i in range(len(arr)):
    if min <= arr[i] <= max:
        print(i)