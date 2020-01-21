numArray = []

numArray.append(float(input('num 1 de 3:')))
numArray.append(float(input('num 2 de 3:')))
numArray.append(float(input('num 3 de 3:')))

sortedArr = numArray[:]
sortedArr.sort()

if numArray == sortedArr:
  print('crescente')
else:
  print('não está em ordem crescente')
