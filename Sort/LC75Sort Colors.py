def sortColors(nums):
    zero_color, one_color, two_color = 0, 0, 0
    #calculate the number of 0,1,2
    for val in nums:
        if val == 0:
            zero_color += 1
        elif val == 1:
            one_color += 1
        elif val == 2:
            two_color += 1
    #create a new string, put the number into correct location
    for i in range(0, zero_color):
        nums[i] = 0
    for i in range(zero_color, zero_color+one_color):
        nums[i] = 1
    for i in range(zero_color+one_color, zero_color+one_color+two_color):
        nums[i] = 2

a = sortColors([0,2,1,1,2,0])
print(a)
