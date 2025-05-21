class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        nums1 = []
        nums2 = []
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            nums1.append(ord(s[i]))
            nums2.append(ord(t[i]))
        nums1.sort()
        nums2.sort()
        for i in range(len(s)):
            if(nums1[i] != nums2[i]):
                return False
        return True