#Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))
print(every_three_nums(120))

#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  return item2
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#Write your function here
def double_index(lst, index):
  if (index >= len(lst)) or (index < -len(lst)):
    return lst
  else:
    new_lst = lst[:index]
    new_lst.append(lst[index]*2)
    end_lst = lst[index + 1:]
    return new_lst + end_lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

#Write your function here
def middle_element(lst):
  if len(lst) % 2 == 1:
    return lst[int(len(lst)/2)]
  else:
    first_median = lst[(int(len(lst)/2)) -1 ]
    second_median = lst[int(len(lst)/2)]
    return (first_median + second_median)/2

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))