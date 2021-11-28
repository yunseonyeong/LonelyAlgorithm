def solution(rows, columns, queries):
    
    answer = []
  
    matrix = [[row*columns + col for col in range(1,columns+1)] for row in range(rows)]
       
    for a,b,c,d in queries :
        
        top,left,bottom,right = a-1, b-1, c-1, d-1
        tmp = matrix[top][left]
        minimum = tmp
        
        for i in range(top,bottom):
            matrix[i][left] = matrix[i+1][left]
            minimum = min(minimum, matrix[i][left])
            
            
        for j in range(left, right):
            matrix[bottom][j] = matrix[bottom][j+1]
            minimum = min(minimum, matrix[bottom][j])
            
            
        for k in range(bottom,top,-1):
            matrix[k][right] = matrix[k-1][right]
            minimum = min(minimum, matrix[k][right])
            
            
        for l in range(right,left,-1):
            matrix[top][l] = matrix[top][l-1]
            minimum = min(minimum, matrix[top][l])
        
        matrix[top][left+1] = tmp
        answer.append(minimum)    
    
    return answer