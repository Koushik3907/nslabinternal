#1.b

def det_matrix(matrix):
    det=(matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    print("Determinant",det%26)
    
def adjo_matrix(matrix):
    adjo=[[matrix[1][1]%26,-matrix[1][0]] ,[-matrix[0][1],matrix[0][0]]]
    print("Adjoint",adjo)
    
    
    
my_matrix=[[2,3],[4,5]]
det_matrix(my_matrix)
adjo_matrix(my_matrix)