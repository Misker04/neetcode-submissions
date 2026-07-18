class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            out[key].append(s)
        return list(out.values())
        