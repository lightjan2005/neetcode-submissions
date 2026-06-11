class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        
        dic = {}
        res = ""
        
        def get_value(key_char, rep_map):
            val = rep_map[key_char]
            while '%' in val:
                for k, v in rep_map.items():
                    val = val.replace(f'%{k}%', v)
            return val

        rep_map = {r[0]: r[1] for r in replacements}
        for key in rep_map:
            dic[key] = get_value(key, rep_map)

        parts = text.split('_')
        res_parts = []
        for p in parts:
            key = p.strip('%')
            res_parts.append(dic[key])
        
        return "_".join(res_parts)