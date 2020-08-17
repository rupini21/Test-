
def smallestSublist(A, k):
    windowSum = 0
    length = float('inf')
    left = 0

    for right in range(len(A)):
        windowSum += A[right]
        while windowSum > k and left <= right:
            length = min(length, right - left + 1)
            windowSum -= A[left]
            left = left + 1
    return length
if __name__ == '__main__':
        A = [2,3,1,5,6,3,7,9,14,10,2,5]
        k = 35
        length = smallestSublist(A, k)

        if length != float('inf'):
            print("Smallest sublist length is", length)
        else:
            print("No sublist exists")

#############################################################

def lengthOfSmallestSubsequence(K, N):
    pq = []
    for i in N:
        pq.append(i)
    pq.sort()
    sum = 0
    count = 0
    while (len(pq) > 0 and sum < K):
        sum += pq[-1]
        del pq[-1]
        count += 1
    if (sum < K):
        return -1
    return count
N = [1,2,2,2,3,4,5,4,7,6,5,12]
K = 70
print(lengthOfSmallestSubsequence(K, N))



































