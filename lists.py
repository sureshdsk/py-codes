# Python Lists
# @IdiotInside_

print ("Creating List:")
colors = ['red', 'blue', 'green']
print (colors[0])   ## red
print (colors[1])   ## blue
print (colors[2])    ## green
print (len(colors))  ## 3

print ("Append to the List")
colors.append("orange")
print (colors[3]) ##orange

print ("Insert to the List")
colors.insert(3, "yellow")
print (colors[3]) ##yellow
print (colors[4]) ##orange

print ("Remove from the List")
print (colors[1])   ## blue
colors.remove("blue") ## deletes blue and shifts elements to the left
print (colors[1])   ## green

print ("Sorting Ascending order using sorted")
nums = [98,22,45,30]
numsAsc = sorted(nums)
print (numsAsc[0])   ## 22
print (numsAsc[1])   ## 30
print (numsAsc[2])    ## 45

print ("Sorting Descending order using sorted")
numsDesc = sorted(nums,reverse=True)
print (numsDesc[0])   ## 98
print (numsDesc[1])   ## 45
print (numsDesc[2])    ## 30
