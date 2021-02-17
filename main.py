def permutation(n):
  if n == 1:
    yield [1]
  else:
    for seq in permutation(n-1):
      yield seq + [n]
      for x in range(n-1):
        temp = seq[x]
        seq[x] = n
        yield seq + [temp]
        seq[x] = temp
      
for seq in permutation(5):
  print(seq)