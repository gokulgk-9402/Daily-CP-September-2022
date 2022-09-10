class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        weak = 0
        
        properties.sort(key= lambda x: (-x[0], x[1]))
        
        max_atk = properties[0][0]
        max_def = properties[0][1]
        
        for i in range(1, len(properties)):
            if properties[i][0] < max_atk and properties[i][1] < max_def:
                weak += 1
                
            else:
                max_atk = properties[i][0]
                max_def = properties[i][1]
                    
        return weak