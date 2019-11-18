
def knapsack( max, item, i=0, ans=[] ):

  # * plus item into answer
  ans.append(item[i])

  # * recursion with smaller list
  if sum(ans) < max:
      if i+1 < len(item):
        knapsack(max, item, i+1, ans)

  # * show ANS
  elif sum(ans) == max:
      print(ans) 
  
  # * remove last answer when end each recursion & move index
  ans.pop()
  if i+1 < len(item):
      knapsack(max, item, i+1, ans)
      

# ! Main
max_money = 20
all_items = [20,10,5,5,3,2,20,10] 

knapsack(max_money, all_items)
