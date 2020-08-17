def minPlatforms(arrival, departure):
    count = 0
    platforms = 0
    i = j = 0
    while i < len(arrival):
        if arrival[i] < departure[j]:
            count = count + 1
            platforms = max(platforms, count)
            i = i + 1
        else:
            count = count - 1
            j = j + 1
    return platforms


if __name__ == '__main__':
    arrival = [9.00, 9.40, 9.50, 11.00, 15.00, 18.00]
    departure = [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]
    arrival.sort()
    departure.sort()
    print("Minimum platforms needed is", minPlatforms(arrival, departure))


#########################################################################
#another code

def findPlatform(arr, dep, n):
    arr.sort()
    dep.sort()
    plat_needed = 1
    result = 1
    i = 0
    j = 0
    while (i < n and j < n):
      if (arr[i] <= dep[j]):
            plat_needed += 1
            i += 1
      elif (arr[i] > dep[j]):
            plat_needed -= 1
            j += 1
            if (plat_needed > result):
               result = plat_needed
    return result
arr = [9.00, 9.40]
dep = [9.10, 12.00]
n = len(arr)

print("Minimum Number of Platforms Required = ", findPlatform(arr, dep, n))

