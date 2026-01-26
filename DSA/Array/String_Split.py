
def solution(s1,s2):
    word1=s1.split()
    word2=s2.split()

    def is_continued(source_word,target_word):
        for s_word in source_word:
            found=False
            for t_word in target_word:
                if s_word in t_word:
                    found =True
                    break
            if not found:
                return False
        return True
    s1_in_s2=is_continued(word1,word2)
    s2_in_s1=is_continued(word2,word1)  

    if s1_in_s2 and s2_in_s1:
        return s1 if len(s1) <= len(s2) else s2
    elif s1_in_s2:
        return s1
    elif s2_in_s1:
        return s2
    else:
        return "NONE"

s1="hey diksha hello"
s2="hey sameeddiksha hello"
print(solution(s1,s2))