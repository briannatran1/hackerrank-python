class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        '''req:
            - fn takes 2 positive int arrs and an int
            - return an int arr

            >>> spells = [3,1,2], potions = [8,5,8], success = 16
            [2, 0, 2]
        '''
        # initialize empty res arr
        # sort potions arr in ascending order so we can apply binary search
        # iterate through spells arr
        # for each spell, we need to find the min potion needed to achieve success
        # do binary search to find the min threshold idx
        # calculate num of successful pairs
        result = []
        potions.sort()

        for spell in spells:
            min_potion_strength = success / spell 
            left, right = 0, len(potions)
            
            while left < right:
                mid = (left + right) // 2 
                
                if potions[mid] < min_potion_strength: 
                    left = mid + 1
                else:
                    right = mid 

            pair_count = len(potions) - left 
            result.append(pair_count)

        return result

"""

[1, 2, 2, 2, 5] target = 2


bisect.bisect_left(arr, target) -> num where u can insert target and maintain sorted order


"""
