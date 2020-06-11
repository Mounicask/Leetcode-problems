class Solution:
    def toGoatLatin(self, S: str) -> str:
        output = []
        for count,sub in enumerate(S.split()): 
            if sub[0] not in 'aeiouAEIOU':
                sub = sub[1:] + sub[0]
            output.append(sub +  'ma' + 'a'*(count+1))
        return ' '.join(output)