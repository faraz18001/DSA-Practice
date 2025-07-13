"""def t_sum(arr: list, target: int):
    map = {}
    for i in range(len(arr)):
        compliment = target - arr[i]
        if compliment in map:
            # Return the indices of the current element and its complement
            return [map[compliment], i]
        else:
            # Store the current element in the map
            map[arr[i]] = i"""


"""Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."""

"""
first+second=Target
compliment=second=target-first

map={0:2


}
#1st iteration i=0
compliment=9-2=7
is 7 in the map
nope
add the value and its index to the map
2nd iteraton i=1
compliment=9-7=2
is 2 inside the map? 
yes it is inside the map 

then return the ith value on you are currently standing  which is
basically nums[1]=7 and the compliment's value which is basically 2

these two add up to make the target of 9
arr[1]+arr[0]=9
target is found.



"""




def two_sum(arr:list,target:int):
    map={}
    for i in range(len(arr)):
        compliment=target-arr[i]
        if compliment in map:
            return [map[compliment],i]

        else:
            map[i]=arr[i]