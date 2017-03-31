def isAnagram(s1, s2):
    list1 = []
    list2 = []
    for i in s1:
        list1.append(i)
    for i in s2:
        list2.append(i)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

word1 = input("Please enter a word:")
word2 = input("Please enter another word for comparison:")
if isAnagram(word1, word2):
    print("is an anagram")
else:
    print("is not an anagram")