# Implementacão Imperativa
def RecBinarySearch(li,target):
    def helper(li,min_index,max_index,target):
        if min_index > max_index:
            return False  
        mid = (min_index + max_index) // 2  # Calculate midpoint index once

        if li[mid] == target:
            return True
        elif li[mid] > target:
            return helper(li, min_index, mid - 1, target)
        else:
            return helper(li, mid + 1, max_index, target)
    return helper(li, 0, len(li) - 1, target)
        
        


# Testing setup - - - - - - - - - - - - - - - - - - - - -
test_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

print(RecBinarySearch(test_list, 12))
# - - - - - - - - - - - - - - - - - - - - - -

