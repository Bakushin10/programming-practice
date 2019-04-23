"""
https://leetcode.com/problems/most-profit-assigning-work/
"""
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = zip(difficulty, profit)
        jobs = sorted(jobs)

        ans = 0
        i = 0
        best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans


difficulty = [85,47,57]
profit = [24,66,99]
worker = [40,25,25]

difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker =  [4,5,6,7]
s = Solution()
s.maxProfitAssignment(difficulty, profit, worker)



def get_itinerary(flights, current_itinerary):
    # If we've used up all the flights, we're done
    if not flights:
        return current_itinerary
    last_stop = current_itinerary[-1]
    for i, (origin, destination) in enumerate(flights):
        # Make a copy of flights without the current one to mark it as used
        flights_minus_current = flights[:i] + flights[i + 1:]
        current_itinerary.append(destination)
        if origin == last_stop:
            return get_itinerary(flights_minus_current, current_itinerary)
        current_itinerary.pop()
    return None