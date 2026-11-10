class Solution:

    def encode(self, strs: List[str]) -> str:
        dict1={}
        string=""
        for i in range(len(strs)):
            dict1[i]=dict1.get(i, strs[i])
        return str(dict1)
            
    def decode(self, s: str) -> List[str]:
        encoded=ast.literal_eval(s)
        decoded=[]
        for key, value in encoded.items():
            decoded.append(value)
        
        return decoded
