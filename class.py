list = [2,4,6,7,24,1,5,0,8,89]



def value(L, n):
    minValue = L[0]
    
    counter = 1
    
    while counter <= n:
        v = L[counter]
        if v <=minValue:
            minValue = v
          
        counter +=1
    return minValue
         
        
  
        
print(value(list , 9))
    
    
    
        
    