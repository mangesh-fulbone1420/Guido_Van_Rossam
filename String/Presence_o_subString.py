
str="python programming language"

def presence_of_subString(str,subString):
    if subString in str:
        return "The Substring is present in the String"
    else:
        return "The SubString is Not Present in the String"
    
print(presence_of_subString(str ,"powerful language"))    