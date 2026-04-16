class Solution:
    def groupAnagrams(self, strs: List[str]):
        groups = {}
    
        for word in strs:
            key = ''.join(sorted(word))
        
            if key not in groups:
                groups[key] = []

            groups[key].append(word)

            group_list = list( groups.values())
            group_list.sort(key=len)

        return group_list