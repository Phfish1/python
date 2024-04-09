def min_path_sum(matrix):
    if not matrix:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Opprett en kopi av matrisen for å lagre de akkumulerte summen for hver celle
    dp = [[0] * cols for _ in range(rows)]
    
    # Initialiser den første cellen
    dp[0][0] = matrix[0][0]
    
    # Fyll ut første rad
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
    
    # Fyll ut første kolonne
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
        
    # Fyll ut resten av matrisen
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
            
    # Returner den siste cellen, som representerer den minste summen for å nå dit
    return dp[rows-1][cols-1]

# Eksempelmatrise
matrix = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

# Få den minste summen for å nå siste element
min_sum = min_path_sum(matrix)
print("Den minste summen for å nå siste element er:", min_sum)
