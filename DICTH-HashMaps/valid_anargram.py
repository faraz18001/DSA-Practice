def valid_anargram(s1,s2):
    if len(s1)!=len(s2):
        return False

    map_s={}
    for char in s1:
        if char not in map_s:
            map_s[char]=1
        else:
            map_s[char]=+1

    map_s2={}
    for char in s2:
        if char not in map_s2:
            map_s2[char]=1
        else:
            map_s2[char]=+1
        
    if map_s==map_s2:
        return True

    else:
        return False


res=valid_anargram("anagram","nagaram")
print(res)