
class Solution:
    def count(self , s):
        camel_count =0
        for i in s:
            if ord(i) >= 65 and ord(i) <= 90:
                camel_count += 1
            else:
                continue
        return camel_count 
    
s="shree ganesh"
obj=Solution()
res = Solution.count(obj,s)
print("Count of Camelcase Characters is : ",res)    
    

    
                