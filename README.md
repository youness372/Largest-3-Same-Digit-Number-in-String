## *The Problem 🤔*    
---   

- You are given a string num representing a large integer. An integer is good if it meets the following conditions:

- It is a substring of num with `length 3`.   

- It consists of only` one` unique digit.  

- Return the `maximum good integer` as a string or an empty string `""` if no such integer exists.   

## *Approach ⛓️‍💥*   
---

-  The first Thing we should do is compared the Cases we have :   

    -  `num[i] == nums[i+1] == nums[i+2]`   
    - And stock each element who has This Condition   



###  *The code of the part 1️⃣*  
```py
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
```       

-  I creat Liste To stock any `Good Number`    
- I start  `cpt = 1`  because each element in the string we have it `1` single time or more.


![image.png](https://assets.leetcode.com/users/images/a6359f4e-1c2a-4c84-92ae-9cce08c0498c_1755179887.8927388.png)   

-  After i take the Substrings whose have the length Greater than 3 .   
- I take the `Max(liste)`  value from the list  and i repeat this Max 3 times   
    - `max(liste) *   3`     

###  *The Code of the part 2️⃣*     


```pyt
if len(liste)  == 0  :   
    return  ""   
else :   
    return  max(liste)*3 
```



## *Complexitry ⏳*    
---   

- Time complexity:  $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

##  *The Sumilation 💻*   
```python3 []
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
```   


![monkey-d-luffy-leetcode](https://github.com/user-attachments/assets/68e1a9e8-ee51-4b24-8286-707e08dd4c83)
