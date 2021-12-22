import random



def even():
    """random choose from 1 to 10 for even"""
    while check is True
        check = false
        even = random.randint(1,10)
        if even % 2 == 0:
            return even
        else:
            check = false
def odd():
    """random choose from 1 to 11 for odd"""
    while check is True
        check = false
        odd = random.randint(1,11)
        if odd % 2 != 0:
            return odd
        else:
            check = false

def compare():
    even = even()
    odd = odd()
    
    if even > odd:
        return 8
    elif even < odd:
        return 3

def cal_score():
    """calculate the total score 
    Args:
        even (int) : even score by randomly choosing 1 to 3
        odd (int) : odd score by randomly choosing 1 to 3
    Returns:
        (int) : the result by calculating even, odd, and touchdown
    """
    touchdown_team = 0
    counter = 0
    
    While counter < 5:
        score_team = compare()
        
        touchdown_team = touchdown_team + score_team
        
        counter = counter + 1
        
    
    return touchdown_team
    

    
    
