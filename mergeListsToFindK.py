import heapq
def merge(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        print(str("list ") + str(list(heap)))
        val, list_ind, element_ind = heapq.heappop(heap)
        merged_list.append(val)
        print("pop_tuple : " + str(val) + " " + str(list_ind) + " " + str(element_ind))

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            print("next_tuple : " + str(next_tuple)+"\n")
            heapq.heappush(heap, next_tuple)
    return merged_list

lists = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
print(merge(lists))