arr=[]
numbers = input('Enter the numbers:')
arr=[int(i) for i in numbers.split()]
j=0
for i in range(len(arr)):
    if i < len(arr) - 2 and arr[i] == arr[i + 1]:
            continue
    arr[j] = arr[i]
    j += 1
for i in range(len(arr)-1):
    print(arr[i],end=' ')