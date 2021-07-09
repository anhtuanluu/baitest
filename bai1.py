def find_smallest_missing(arr):
    n = len(arr)
    aux = [0] * (n+1)
    for i in range(n):
        if(arr[i] > 0 and arr[i] <= n):
            aux[arr[i]-1] = 1
    for i,v in enumerate(aux):
        if not v:
            return i+1
    
if __name__ == '__main__':
    print(find_smallest_missing([1, 2, 3, 4, 6, 5]))
    print(find_smallest_missing([-8, -7, -6]))
    print(find_smallest_missing([4, 3, 1, -1]))
    print(find_smallest_missing([2, 1, 5, 4]))