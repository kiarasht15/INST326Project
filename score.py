import random



def even():
    """random choose from 1 to 3 for even"""
    even = random.randint(1,3)
    return even
def odd():
    """random choose from 1 to 3 for odd"""
    odd = random.randint(1,3)
    return odd

def cal_score(even, odd):
    """calculate the total score 
    Args:
        even (int) : even score by randomly choosing 1 to 3
        odd (int) : odd score by randomly choosing 1 to 3
    Returns:
        (int) : the result by calculating even, odd, and touchdown
    """
    touchdown = 0
    if even > 1:
        touchdown += 3
        result = even + odd + touchdown
        return result
    if odd > 1:
        touchdown += 0 
        result = even + odd + touchdown
        return result

    

    
    
