def solution(orders, course):
    answer = []
    
    for i in course:            
      global recipe
      recipe = dict() 
      for o in orders:  
        comb(0, "", o, i)
      
      if len(recipe.keys()) == 0:
        continue
      
      max_value = max(recipe.values())
      max_value = max(2, max_value)
      
      for k in recipe.keys():
        if recipe[k] == max_value:
          answer.append(k)
      print(recipe)
    return sorted(answer)


def comb(i, w, ws, r):
    if len(w) == r:
        if w in recipe:
            recipe[w] += 1
        else: recipe[w] = 1
        return 
    
    for j in range(i, len(ws)):
        comb(j + 1, "".join(sorted(w + ws[j])), ws, r)
