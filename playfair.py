import numpy
def generateKeyMatrix (key): 
  simpleKeyArr = []
  for c in key:
    if c not in simpleKeyArr:
      (simpleKeyArr.append('I') if c=='J' else simpleKeyArr.append(c))
  is_I_exist = "I" in simpleKeyArr
  for i in range(65,91):
    if chr(i) not in simpleKeyArr:
      if i==73 and not is_I_exist:
        simpleKeyArr.append("I")
        is_I_exist = True
      elif i==73 or i==74 and is_I_exist:
        pass
      else:
        simpleKeyArr.append(chr(i))
    
  matrix_5x5=numpy.reshape(simpleKeyArr,(5,5))
  print("Key Matrix:")
  [print(row) for row in matrix_5x5]
  return matrix_5x5

def indexLocator (char,cipherKeyMatrix):
  indexOfChar = []
  if char=="J": char = "I"

  for i,j in enumerate(cipherKeyMatrix):
    for k,l in enumerate(j):
      if char == l:
        indexOfChar.append(i)
        indexOfChar.append(k)
        return indexOfChar

def encryption (plainText,key):
  cipherText =[]
  keyMatrix = generateKeyMatrix(key)
  for s in range(0,len(plainText)+1,2):
    if s<len(plainText)-1:
      if plainText[s]==plainText[s+1]:plainText=plainText[:s+1]+'X'+plainText[s+1:]

  if len(plainText)%2 != 0: plainText = plainText[:]+'X'

  i = 0
  while i < len(plainText):
    n1 = indexLocator(plainText[i],keyMatrix)
    n2 = indexLocator(plainText[i+1],keyMatrix)
    i1 = (n1[0] + 1) % 5 if n1[1] == n2[1] else (n1[0] if n1[0]==n2[0] else n1[0])
    j1= n1[1]if n1[1] == n2[1] else ((n1[1] + 1) % 5 if n1[0]==n2[0] else n2[1])
    
    i2 = (n2[0] + 1) % 5 if n1[1] == n2[1] else (n2[0] if n1[0]==n2[0] else n2[0])
    j2= n2[1]if n1[1] == n2[1] else ((n2[1] + 1) % 5 if n1[0]==n2[0] else n1[1])
    cipherText.append(keyMatrix[i1][j1])
    cipherText.append(keyMatrix[i2][j2])
    cipherText.append(" ")
    i += 2  
  return cipherText

key = input("Enter key: ").replace(" ","").upper()
plainText =input("Plain Text: ").replace(" ","").upper()
cipherText =encryption(plainText,key)
print("CipherText",end=': ')
[print(cipher,end='') for cipher in cipherText]
