class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedlist=sorted(nums1 + nums2)
        n=len(sortedlist)
        if n%2 != 0:
            return float(sortedlist[n//2])
        else:
            return (sortedlist[n//2]+sortedlist[(n//2)-1])/2
