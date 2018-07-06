class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = {}
        existed=  []
        result = []
        for item in strs:
            key = ''.join(sorted(item))
            if key not in table:
                table[key] = [item]
                existed.append(key)
            else:
                table[key].append(item)
        for key in existed:
            result.append(table[key])
        return result
