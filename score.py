import random



def even():
    even = random.randint(1,3)
    return even
def odd():
    odd = random.randint(1,3)
    return odd

def cal_score(even, odd):
    touchdown = 0
    if even > 1:
        touchdown += 3
        result = even + odd + touchdown
        return result
    if odd > 1:
        touchdown += 0 
        result = even + odd + touchdown
        return result

    

    
    
