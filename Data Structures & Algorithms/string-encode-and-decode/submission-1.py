class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""
        else:
            encoded=""
            for i in strs:
                c=len(i)
                encoded+=str(c)+"#"+i
            return encoded
        print(encoded)

    def decode(self, s: str) -> List[str]:
        c = len(s)
        if c == 0:
            print(c)
            return []
        res ,i=[],0
        while i<c:
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        print(res)
        return res
