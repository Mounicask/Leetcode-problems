Binary Search :


nums = [1,4,5,7,11,28,33,41,56]
target = 33
low = 0
high = len(nums) -1
val = ''
while low<=high:
    mid = (low +high ) //2
    if nums[mid] == target:
        val=mid+1
        break
    elif nums[mid]<target:
        low =mid +1
    else:
        high= mid -1
if val == '':
    print("Value doesn't exist")