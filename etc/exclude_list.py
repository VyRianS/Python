
list_a = [2,3,4,7,8,9,13,17]
list_b = [1,4,8,10,12,17,22,23]

#  Write function to return list of numbers which are
#+ in list_b BUT not in list_a.

def exclude_list(list_a, list_b):
    ret_list = []
    for element_b in list_b:
        if element_b not in list_a:
            ret_list.append(element_b)
    return ret_list

def exclude_list_fast(list_a, list_b):
    ret_list = []

    # 3 scenarios,
    #   1. list_b[idx_b] < list_a[idx_a], immediately add into ret_list.
    #        - idx_b += 1
    #        - no change to idx_a
    #   2. list_b[idx_b] = list_a[idx_a], item is found.
    #       - idx_b += 1
    #       - no change to idx_a
    #   3. list_b[idx_b] > list_a[idx_a], item may still be ahead.
    #       - idx_a += 1
    #       - no change to idx_b
    #       - compare again until result falls within the first 2 cases

    idx_a = 0

    for idx_b in range(len(list_b)):

         # If idx_a has already reached max length, add to the ret_list.
         if idx_a == len(list_a)-1:
             ret_list.append(list_b[idx_b])
         elif list_b[idx_b] < list_a[idx_a]:
             ret_list.append(list_b[idx_b])
         elif list_b[idx_b] == list_a[idx_a]:
             continue
         elif list_b[idx_b] > list_a[idx_a]:
             print("entering while loop...")
             while list_b[idx_b] > list_a[idx_a] and idx_a < (len(list_a)-1):

                 idx_a += 1
                 print("idx_a", idx_a)
                 print("list_a[idx_a]", list_a[idx_a])
                 print("idx_b", idx_b)
                 print("list_b[idx_b]", list_b[idx_b])
                 print("----------")
                 if list_b[idx_b] < list_a[idx_a]:
                     ret_list.append(list_b[idx_b])
                 elif list_b[idx_b] == list_a[idx_a]:
                     break

             print("exiting while loop...")

    return ret_list


if __name__ == "__main__":

    print("list_a:", list_a)
    print("list_b:", list_b)

    print(exclude_list_fast(list_a, list_b))

