from time import time
start_time=time()

def binary_search(arr, aranan):

    first = 0
    mid = 0
    end = len(arr)

    while ( end >= first ):

        mid = ( first+ end) // 2

        if aranan == arr[mid]:
            return mid

        if aranan > arr[mid]:
            first = mid+1

        if aranan < arr[mid]: 
            end = mid-1   
        
    return-1


print("arr:")
arr=list(map(int,input().split()))

arr=sorted(arr)
print(arr)
aranan=int(input("aranan: "))

print("Index of {}: {}".format(aranan, binary_search(arr, aranan)))

end_time=time()
elapsed=end_time-start_time
print(elapsed)
