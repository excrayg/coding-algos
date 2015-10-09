
def is_match(str_to_match, pattern):
    if str_to_match == "":
        return True
    
    if pattern == "":
        return False
        
    if len(pattern) > 1 and pattern[1] == "*":
        trial1 = is_match(str_to_match, pattern[2:])
        if not trial1:
            while pattern[0] == "." or str_to_match[0] == pattern[0]:
                return is_match(str_to_match[1:], pattern)
        else:
            return trial1
    else:
        if pattern[0] == "." or str_to_match[0] == pattern[0]:
            return is_match(str_to_match[1:], pattern[1:])
        else:
            return False
            
print(is_match("aa",  "a")) 
print(is_match("aa",  "aa"))
print(is_match("aaa", "aa")) 
print(is_match("aa",  "a*"))
print(is_match("aa",  ".*"))
print(is_match("ab",  ".*"))
print(is_match("aab", "c*a*b"))