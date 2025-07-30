def merge(lst_1, lst_2):
  i = 0
  j = 0
  lst = []
  while i < len(lst_1) and j < len(lst_2):
    if lst_1[i] <= lst_2[j]:
      lst.append(lst_1[i])
      i += 1
    else:
      lst.append(lst_2[j])
      j +=1

  lst = lst + lst_1[i:]
  lst = lst + lst_2[j:]
  return lst

print(merge([1, 3, 5, 7, 10, 11, 12], [-10, -1, 2, 3]) )