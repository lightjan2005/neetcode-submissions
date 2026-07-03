class Solution:
    def compress(self, chars: List[str]) -> int:
        s_idx = 0
        l = 0

        while l < len(chars):
            r = l
            while r < len(chars) and chars[r] == chars[l]:
                r += 1
            
            chars[s_idx] = chars[l]
            s_idx += 1
            
            count = r - l
            if count > 1:
                for digit in str(count):
                    chars[s_idx] = digit
                    s_idx += 1
            
            l = r

        return s_idx
