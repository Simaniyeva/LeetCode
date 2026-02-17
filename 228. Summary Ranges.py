class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        for num in nums:
            if not ranges or num > ranges[-1][1] + 1:
                ranges.append([num, num])
            else:
                    ranges[-1][1] = num
        return [str(interval[0]) + '->' + str(interval[1]) if interval[0] != interval[1] else str(interval[0]) for interval in ranges]
            