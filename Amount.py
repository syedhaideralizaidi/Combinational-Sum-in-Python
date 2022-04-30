#!/usr/bin/env python
# coding: utf-8

def amount(A,sum):
  ans = []
  temp = [] 
  emp=[]
  test=[]
  copy=[]
  final=[]
  copy=A
  A = sorted(list(set(A)))
  findcombo(ans, A, temp, sum, 0)
  for i in ans:
      for j in range(1,10):
        if i.count(j)>copy.count(j):
          test.append(i)
  for i in ans[:]:
    if i in test:
      ans.remove(i)          
  if len(ans) <= 0:
    return emp 
  return ans


def findcombo(ans, A, temp, S, index):
  if(S == 0):
    ans.append(list(temp))
    return   
  for i in range(index, len(A)):
    if(S - A[i]) >= 0:
      temp.append(A[i])
      findcombo(ans, A, temp, S-A[i], i)
      temp.remove(A[i])  


arr = [1,1,2,2,5,7]
sum = 10
ans = amount(arr, sum)
print(ans)
      
 

