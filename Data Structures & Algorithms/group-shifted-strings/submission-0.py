class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for string in strings:
            
            ch = string[0]
            normalized = []
            
            for c in string:
                shifted = chr((ord(c)-ord(ch)) % 26 + ord('a'))
                normalized.append(shifted)

            key = "".join(normalized)

            groups[key].append(string)
        
        return list(groups.values())

