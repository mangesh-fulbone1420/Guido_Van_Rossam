
s = input("Enter The String : ")

words = s.split()

print("Given String is :", words)

for i in range(len(words)):
    words[i] = words[i].lower()

print("Lowercased words:", words)
words.sort()
print("Alphabetically sorted words:", words)

for i in words:
    print(i) 

