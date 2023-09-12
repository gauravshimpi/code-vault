"""
@Author: Gaurav Shimpi
@Date: 12th Sept, 2023
"""


def is_anagram(s: str, t: str) -> bool:
    """
    finds if string t is the valid anagram of string s or not
    str:param t: string with all lower cases.
    str:param s: string with all lower cases.
    bool:return: true if it's valid anagram else not
    """
    char_counter = {}
    for ch in s:
        char_counter[ch] = char_counter.get(ch,0) + 1
    for ch in t:
        if ch not in char_counter:
            return False
        if char_counter[ch] <= 0:
            return False
        char_counter[ch] -= 1
        return True



if __name__ == '__main__':
    string1 = input("Enter string 1: ")
    string2 = input("Enter string 2: ")
    result = is_anagram(string1, string2)
    print(result)
