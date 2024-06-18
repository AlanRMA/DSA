# Implementacão Imperativa
def LinearSearch(li,target):
    for item in li:
        if item == target:
            return True
    return False

# Implementacão Funcional
def RecLinearSearch(li,target):
    def helper(n):
        if li[n] == target:
            return True
        elif n == 0:
            return False
        else:
            return helper(n-1)
    return  helper(len(li)-1)




# Testing setup - - - - - - - - - - - - - - - - - - - - -
test_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

print(LinearSearch(test_list, 12))
print(RecLinearSearch(test_list, 12))

print(LinearSearch(test_list, 20))
print(RecLinearSearch(test_list, 20))
# - - - - - - - - - - - - - - - - - - - - - -

