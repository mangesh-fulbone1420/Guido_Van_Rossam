class Solution:
    def largestNum(self, arr):
        ans = float('-inf')
        for i in arr:
            if i < ans:
                ans =i
            else:
                continue
        return ans
arr =[1,8,7,56,90,45,23]
obj=Solution()
res=obj.largestNum(arr)
print("Largest Number in the Array is : ",res)



