
def get_itinerary(flights, current):
    """
     flights : [[]]
     current : []
    """
    if len(flights) == 0:
        return current

    for i, (origin, destination) in enumerate(flights):
        if origin == current[-1]:
            current.append(destination)
            # remove the current index of the list
            flights_minus_current = flights[:i] + flights[i+1:]
            return get_itinerary(flights_minus_current, current)
    return None


"""
 diff version
"""
# def flightIntenary(flights)
	
# 	res = []
# 	origin = "YUL"
# 	return flightIntenaryHelper(flights, current,res)

# def flightIntenaryHelper(flights, current, res):

# 	if not len(flights):
# 		return res

# 	for i, (origin, destination) in enumerate(flights):
# 		if current == origin:
# 			res.append(origin)
# 			newFlight = flights[:i] + flights[i+1:]
# 			flightIntenaryHelper(newFlights, destination, res)
# 	return None

flights = [["HNL", "AKL"], ["YUL", "ORD"], ["ORD", "SFO"], ["SFO", "HNL"]]
current = ["YUL"]
print(get_itinerary(flights, current))
 

# def subset_sum(numbers, target, partial=[]):
#     s = sum(partial)
#     print(partial)
#     # check if the partial sum is equals to target
#     if s == target: 
#         print "sum(%s)=%s" % (partial, target)
#     if s >= target:
#         return  # if we reach the number why bother to continue

#     for i in range(len(numbers)):
#         n = numbers[i]
#         remaining = numbers[i+1:]
#         subset_sum(remaining, target, partial + [n]) 
        
# subset_sum([3,9,8,4,5,7,10],15)

