class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        '''req:
            - fn takes in 2 int arrs
            - return list len of 2
                - ans[0] --> distinct ints in nums1 not in nums2
                - ans[1] --> distinct ints in nums2 not in nums1
            
            >>> nums1 = [1,2,3], nums2 = [2,4,6]
            [[1,3],[4,6]]

            >>> nums1 = [1,2,3], nums2 = [1,1,2]
            [[3], []]
        '''
        # make sets of nums1 and nums2
        # create 2 arr vars
        # iterate through each arr and check if elem is in opp set
        # if no, append to expected list and add to set
        # return arrs in list
        s1 = set(nums1)
        s2 = set(nums2)
        result1 = []
        result2 = []

        for i in range(len(nums1)):
            if nums1[i] not in s2:
                result1.append(nums1[i])
                s2.add(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in s1:
                result2.append(nums2[i])
                s1.add(nums2[i])
        return [result1, result2]
