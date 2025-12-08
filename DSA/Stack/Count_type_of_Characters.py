class Solution:
    def count(self, s):
        upper_case = 0
        lower_case = 0
        numeric = 0
        special_char = 0
        for i in s:
            if ord(i) >= 65 and ord(i) <= 90:
                upper_case += 1
            elif ord(i) >= 97 and ord(i) <= 122:
                lower_case += 1
            elif ord(i) >= 48 and ord(i) <= 57:
                numeric += 1
            else:
                special_char += 1
        return (upper_case, lower_case, numeric, special_char)

s = '#GeeKs01fOr@gEEks07'
obj = Solution()
result = obj.count(s)
print("Uppercase characters:", result[0])
print("Lowercase characters:", result[1])
print("Numeric characters:", result[2])
print("Special characters:", result[3])