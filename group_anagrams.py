class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ''' req:
            - fn takes arr of strs
            - return arr of arrs with anagrams grouped together in each subarr
        '''
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())

# create dict of lists
# iterate through each word in strs
# sorted word will be used as a key and append original word to said key
# convert into list and return
