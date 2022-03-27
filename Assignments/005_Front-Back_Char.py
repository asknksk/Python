"""
(Using Function)
Given a string, return a new string where the first and last chars have been exchanged.
Example :
- print(front_back('clarusway'))  output => ylaruswac
- print(front_back('ab'))   output => ba
"""
def front_back(word) :
    return word[-1] + word[1:-1] + word[0]

print(front_back('clarusway'))