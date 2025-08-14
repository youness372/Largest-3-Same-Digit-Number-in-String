class Solution:
    def largestGoodInteger(self, num: str) -> str:
        liste = []     
        cpt =  1  
        for i in  range (1 , len(num)) :    
            if num[i]  ==  num[i-1]  :    
                cpt +=  1   
            elif num[i]  !=  num[i-1]  :   
                cpt = 1    
            if cpt >=  3 :  
                liste.append(num[i])   
                cpt = 0   
        if len(liste) == 0 :   
            return  ""   
        return  max(liste) *  3  
