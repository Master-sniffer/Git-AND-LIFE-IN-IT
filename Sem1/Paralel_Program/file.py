
from multiprocessing import Process, Pool
import copy
import numpy


res=0



def element(index, A, B):
    result = copy.copy(B)
    i, j = index
    global res
    # get a middle dimension
    N = len(A[0]) or len(B)
    # iterate through rows of X
    for i in range(N):
      # iterate through columns of Y
      for j in range(N):
          # iterate through rows of Y
          for k in range(N):

              result[i][j] += int(A[i][k]) * int(B[k][j])
    print (result)

    print (res, "done")
    with open ('myfile.txt', 'a') as f:
      f.write(str(result) + " this is the result\n\n")

    return res
    

with open ('myfile.txt', 'w+') as f:
  pass

# print(element((1, 0), matrix1, matrix2))

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[2, 0], [1, 2]]


p1 = Process(target=element, args=[(0, 0), matrix1, matrix2])
p1.start()
p1.join()

matrix1 = [[5,4,2], [5,2,1],[2,2,2]]
matrix2 = [[5,4,5], [1,2,3],[4,2,1]]


p1 = Process(target=element, args=[(0, 0), matrix1, matrix2])
p1.start()
p1.join()

with open ("matrix.txt", "r") as f:
  matrix1=f.readline()

matrix1=matrix1.split()
matrix1=numpy.array(matrix1)
matrix1=numpy.resize(matrix1,(2,2))
print(matrix1)
matrix2=numpy.copy(matrix1)
matrix1=matrix1.astype(int)
matrix2=matrix2.astype(int)



p1 = Process(target=element, args=[(0, 0), matrix1, matrix2])
p1.start()
p1.join()

print(res)



