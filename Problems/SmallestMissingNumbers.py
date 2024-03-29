

## Return smallest Positive Integer from an array

def smallMissingNumber(a, n) :  
      
    #unordered map 
    mp = dict();  
  
    #checking value of array is positive or not
    #if positive, store in mp 
    for i in range(n) : 
        if (a[i] > 0) : 
            if a[i] not in mp.keys() : 
                mp[a[i]] = 0
            
            mp[a[i]] += 1
  
    index = 1;  
 
    ## One way to lookup in dictionary:

    # while (1) : 
    #     if (index not in mp.keys()) :  
    #         return index;  
          
  
    #     index += 1;
    
    ## Way 2:
    for i in range(1,len(arr)):
        if (i not in mp.keys()):
            return i
        
        

  
arr = [ -5, 2, 0, -1, -10, 15 ];  
size = len(arr);  
  
print("Smallest positive missing number is : ",smallMissingNumber(arr, size));  

## Time COmplexity O(n)
