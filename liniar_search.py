#Linear Search program

def linear_search(list,target):
    for i in range(len(list)):
        if list[i]==target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index",index)
    else:
        print("Target not found")

n=[11,2,33,4,5,6,7,8]
result= linear_search(n,8)
verify(result)





