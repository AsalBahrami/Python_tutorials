#THIS PEACE OF CODE HAS SPLITTED MY ASS
def maxOfLeft(list,left,m):
    currentMax=0
    currentSum=0
    #for mid of list to the left
    for l in range(m,left-1,-1):
        currentSum+=list[l]
        if currentMax<currentSum:
            currentMax=currentSum
    return currentMax

def maxOfRight(list,m,right):
    currentMax=0
    currentSum=0
    for r in range(m+1,right):
        currentSum+=list[r]
        if currentMax<currentSum:
            currentMax=currentSum
    return currentMax

def maxOfArray(list,left,right):
    if left==right:
#Folge hat ein Element: element zurueckgeben oder 0 falls element negativ
        return max(list[1],0)
    elif right>left:
        m=int(right+left)//2
        max1=maxOfArray(list,left,m)
        max2=maxOfArray(list,m+1,right)
        max3=maxOfLeft(list,left,m)+maxOfRight(list,m,right)
#Maximum der drei kandidaten zurueckgeben
        return max(max1,max2,max3,0)

    else:
        return -1


list = [3, 9, 0, -12, 2, -10, 0, 4, -2]
print(maxOfArray(list,0,len(list)))

'''
def main():
    list=[3,9,0,-12,2,-10,0,4,-2]
    print(maxArray(list))


def maxArray(list):
    currentMax=0

    for left in range(0,len(list)):
        for right in range(left,len(list)):
            currentSum=0
            for i in range(left,right+1):
                currentSum+=list[i]
                if currentSum>currentMax:
                    currentMax=currentSum
    return currentMax

if __name__ == '__main__':
    main()'''