from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        current = "JFK"
        route = [current]
        return self.findItineraryHelper(tickets, current, route)
    
    def findItineraryHelper(self, tickets, current, route):
        if len(tickets) == 0:
            return route
        
        for i, (origin, destination) in enumerate(tickets):
            if origin == current:
                newTicket = tickets[:i] + tickets[i+1:]
                current = destination
                route.append(current)
                return self.findItineraryHelper(newTicket, current, route)
        return None
    
    def findItineraryHelper2(self, tickets):
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)
        route, stack = [], ["JFK"]

        print(targets)
        while stack:
            print(stack[-1])
            while targets[stack[-1]]:
                l = targets[stack[-1]].pop()
                stack.append(l) #targets[stack[-1]].pop(),
            top = stack.pop()
            route.append(top)
        return route[::-1]

        # while stack:
        #     while targets[stack[-1]]:
        #         stack += targets[targets[-1]].pop()
        #     route.append(stack.pop())
        # return route[::-1]

#tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
s = Solution()
print(s.findItineraryHelper2(tickets))