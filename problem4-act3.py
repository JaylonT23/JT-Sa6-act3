def intersection(list1, list2):
    # Use filter() to keep only the elements present in both lists
    intersected_elements = list(filter(lambda x: x in list2, list1))
    return intersected_elements


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection_list = intersection(list1, list2)
print("Intersection:", intersection_list)