def tribonacci(signature, n):
    
    if n == 0:
        signature = []
    elif n == 1:
        signature.remove(signature[-1])
        signature.remove(signature[-1])
    else:
        while n > 3: 
            signature.append(signature[-1] + signature[-2] + signature[-3])    
            n -= 1
    
    return signature