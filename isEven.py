def isEven(num):
    numstr =str(num)
    arr=[0,2,4,6,8]
    if int(numstr[len(numstr)-1]) in arr:
        return True
    return False

print(isEven(30))