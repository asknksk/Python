"""
- In this kata you have to correctly return who is the "survivor", ie: the last element of a Josephus 
permutation.
- Basically you have to assume that n people are put into a circle and that
they are eliminated in steps of k elements, like this:
josephus_survivor(7,3) => means 7 people in a circle;

one every 3 is eliminated until one remains
3 is counted out. New list :  [1, 2, 4, 5, 6, 7]
6 is counted out. New list :  [1, 2, 4, 5, 7]
2 is counted out. New list :  [1, 4, 5, 7]
7 is counted out. New list :  [1, 4, 5]
5 is counted out. New list :  [1, 4]
1 is counted out. New list :  [4]
"""
# First solution is with functions

def survivor(n, k) :
    new_list = list(range(1,n+1))
    
    k = k -1
    def survivor2(n, k) :
        
        print(f"{new_list.pop(k)} is counted out. New list : ", end=" ")
        
        print(new_list)
        if n == 2 :
            pass
        else :
            n -= 1
            k = (k + 2) % n
            
            
            return survivor2(n, k)
    survivor2(n, k)

print(survivor(7,3))

# Second solution is with while loop

n = 7
k = 3
k = k - 1
new_list = list(range(1, n+1))

while n != 1 :  

    print(f"{new_list.pop(k)} is counted out. New list : ", end=" ")
    print(new_list)
    
    if n == 2 :
        break
    else : 
        n -= 1
        k = (k + 2) % n
