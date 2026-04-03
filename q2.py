def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    while adjacent_duplicates_kontrol(s):
        sonuc = ""
        for i in range(len(s)):

            if i < len(s)-1 and s[i] == s[i+1]:
  
                sonuc += s[i+2:]
                break
            else:
                sonuc += s[i]

        s = sonuc
    return s
def adjacent_duplicates_kontrol(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False
