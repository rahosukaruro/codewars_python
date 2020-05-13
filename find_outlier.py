def find_outlier(integers):
    even_count = 0
    odd_count = 0
    even = 0
    odd = 0
    
    for num in integers:  
        div = num % 2
    
        #even
        if div == 0:
            even = num
            even_count += 1
                
        #odd
        if div != 0:
            odd = num
            odd_count += 1
            
    return even if even_count < odd_count else odd