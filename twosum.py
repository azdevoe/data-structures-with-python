def tp(arr,target):
    left=0
    right=len(arr)-1
    while right>left:
        sup=arr[left]+arr[right]
        if sup== target:
            return [left,right]
        elif sup>target:
            right-1