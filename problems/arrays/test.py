

def findMiddle(s):
    m = len(s) // 2
    print(len(s), m)
    time = 4
    l = m
    r = m

    while time:
        l-=1
        r+=1
        time-=1

    left = s[:l]
    middle = s[l: r]
    right = s[r:]
    print(left)
    print(right[::-1])
    print(middle)



findMiddle("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")


    while l < r: # saba, l = a, r = a, charsToBeDeleted = 0
        if s[l] != s[r]:
            if s[l+1] == s[r] and charsToBeDeleted: # delete s[l]
                charsToBeDeleted -=1
                l+=1
            elif s[r-1] == s[l] and charsToBeDeleted: # delete s[r]
                charsToBeDeleted-=1
                r-=1
            else:
                return False
        r-=1
        l+=1
    
    return True
