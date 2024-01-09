class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ''' req: 
            - fn takes 2 strs
            - return true if anagrams
            - anagram: can create word by rearranging letters
        '''
        count = defaultdict(int)

        for char in s:
            count[char] += 1
        
        for char in t:
            count[char] -= 1

        for val in count.values():
            if val != 0:
                return False
        
        return True
        

# create counters for strs
# iterate through s and increment count for each char
# iterate through t and decrement count for each char
# check if any char has non-zero freq --> not anagrams
