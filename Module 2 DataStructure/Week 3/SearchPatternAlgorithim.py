#python3

import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))
    
def poly_hash(s, prime, x):
    """Hash function to convert the pattern and text"""
    
    ans = 0
    for c in reversed(s):
    	ans = (ans * x + ord(c)) % prime
    return ans

def AreEqual(S1,S2):
    """To test if the two strings are equal if they collide"""
    
    if len(S1) != len(S2):
        return False
    
    for i in range(len(S1)-1):
        if S1[i] != S2[i]:
            return False
    return True

def PreCompute(plength,T,p,x):
    """ To precompute the hash value of the text"""
    
    H = [0] * (len(T) - plength + 1)
    s = T[-plength:]
    H[len(T)-plength] = poly_hash(s, p, x)
    y = 1
    
    #precompute x to the power of the length of the pattern and store it in y
    #to compute the last substring hash value
    for i in range(1,plength):
        y = (y*x) % p #?what is this
    
    #compute the hash values for substrings of text from right to left    
    for i in range((len(T) - plength - 1),0,-1):
        prehash = x * H[i + 1] + ord(T[i]) - y * ord(T[i + plength])  
        H[i] = prehash % p
    
    return H
    

def process(P,T):
    p = 100002000000000007
    x = random.randint(1, p)
    result = []
    pHash = poly_hash(P,p,x)
    H = PreCompute(len(P),T,p,x)
    
    for i in range(0,len(T)-len(P)+1):
        if pHash != H[i]:
            pass
        
        if AreEqual(T[i:i + len(P)],P):
            result.append(i)
    
    return result
        
if __name__ == '__main__':
    print_occurrences(process(*read_input()))        
