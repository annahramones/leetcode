"""
875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i]
bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, 
she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and 
will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas 
before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Notes: So we know that h is greater than or equal to the length of piles, and we
       know that the max k will be the greatest number in the list. The least
       number is 1 (eating 1 banana an hour). So we do a binary search through the 
       options [1,greatestNum]. We have to calculate the number of hours it takes 
       to eat all the bananas (cacluate by dividing #num bananas in pile / k). 
       If number of hours is less than or equal to 8, we can update the result we
       will return and then only look in the first half of the options. Else
       only look at the second half of options
"""

import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        greatest = max(piles)
        if h == len(piles): return greatest
        least = 1
        res = greatest

        while least <= greatest:
            k = (greatest - least) // 2 + least
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                res = k
                greatest = k - 1
            else:
                least = k + 1
            
        return res