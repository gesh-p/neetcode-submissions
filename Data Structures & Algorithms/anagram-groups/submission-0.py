class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for word in strs:
            curr = ''.join(sorted(word))
            if curr not in dic:
                dic[curr] = [word]
            else:
                dic[curr].append(word)

        res = []
        for key in dic:
            res.append(dic[key])
            
        return res
    

        
            

