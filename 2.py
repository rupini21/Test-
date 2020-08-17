
def printMax(arr, n, k):
    max=0
    for i in range(n - k + 1):
        max = arr[i]
        for j in range(1, k):
            if arr[i + j] > max:
                max = arr[i + j]
        print(str(max) + " ", end="")
if __name__ == "__main__":
    arr = [1, 2, 3,1, 4, 5,2,3, 6]
    n = len(arr)
    k = 3
    printMax(arr, n, k)

#######################################################
print()
print()
print()
######################################################

from collections import deque
def printMax(arr, n, k):
    Qi = deque()
    for i in range(k):
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    for i in range(k, n):
        print(str(arr[Qi[0]]) + " ", end="")
        while Qi and Qi[0] <= i - k:
            Qi.popleft()

        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()

        Qi.append(i)
    print(str(arr[Qi[0]]))
if __name__ == "__main__":
    arr = [8,5,10,7,9,4,15,12,90,13]
    k = 4
    printMax(arr, len(arr), k)
