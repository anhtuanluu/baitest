def find_smallest_missing(arr):
    index = 1
    while True:
        if index not in arr:
            return index
        index += 1
 
if __name__ == '__main__':
    print(find_smallest_missing([3, 4, -1, 1]))
    print(find_smallest_missing([-8, -7, -6]))