#Written by Arif Aulakh
def dp(c, s, t):
  array = [0 for i in range(t+1)]
  array[0] = 1
  for i in range(0,s):
    for j in range(c[i],t+1):
      array[j]+=array[j-c[i]]
  return array[t]
coins = [1,2,5,10,20,50,100,200]
size = len(coins)
target = 200
print(dp(coins,size,target))
