from time import time
start_time=time()

def binary_search(arr,low,high,key):

    if not low<high:
        return-1
            
    mid = (high+low) // 2

    if arr[mid]==key:
        return mid

    elif arr[mid]<key:
        return binary_search(arr,mid+1,high,key)

    else:
        return binary_search(arr,low,mid,key)
        
       
print("create arr:")

arr = list(map(int,input().split()))
arr=sorted(arr)
print(arr)       

key = int(input("which numer are you looking for:"))
result=binary_search(arr,0,len(arr)-1,key)

if result != -1:
   print("index of {}:{}".format(key,result))
else:   
   print("key is not present in array") 
end_time=time()
elapsed=end_time-start_time
print(elapsed)
