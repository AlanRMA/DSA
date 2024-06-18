def BubbleSort(li):
    while li != sorted(li):
        for n in range(len(li)-1):
            if li[n] > li[n+1]:
                li[n], li[n+1] = li[n+1], li[n]
    return li
        



def RecBubbleSort(li):
    def helper(li, n):
        if n == 1:
            return li
        for i in range(n-1):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
        return helper(li, n-1)
    return helper(li, len(li))
    






# Testing setup - - - - - - - - - - - - - - - - - - - - -

test_list = [2,6,8,0,4,10,12]

print(BubbleSort(test_list))
print(RecBubbleSort(test_list))
