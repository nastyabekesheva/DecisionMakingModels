import numpy as np

class BinaryRelationship:

    def __init__(self, matrix):
        if len(matrix.shape) == 2 and matrix.shape[0] == matrix.shape[1]:
            self._matrix = matrix
        else:
            raise ValueError("Incorrect shape of a matrix")

    def reflexive(self):
        for i in range(len(self._matrix)):
            if self._matrix[i][i] == 0:
                return False
            
        return True
            
    def antireflexive(self):
        for i in range(len(self._matrix)):
            if self._matrix[i][i] == 1:
                return False

        return True
                
    def symmetric(self):
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix)):
                if self._matrix[i][j] != self._matrix[j][i]:
                    return False
                
        return True
                
    def antisymmetric(self):
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix)):
                if i != j and (self._matrix[i][j] & self._matrix[j][i]) != 0:
                    return False
                
        return True
                   
    def asymmetric(self):
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix)):
                if (self._matrix[i][j] & self._matrix[j][i]) != 0:
                    return False
                
        return True
                    
    def transitive(self):
        squared_matrix = self._matrix ** 2
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix)):
                if squared_matrix[i][j] > self._matrix[i][j]:
                    return False

        return True
                    
    def worst(self):
        worst_elements = np.where(np.all(self._matrix == 1, axis=0))[0]

        return worst_elements
    
    def best(self):
        best_elements = np.where(np.all(self._matrix == 1, axis=1))[0]

        return best_elements
    
    def inverse(self):
        return np.transpose(self._matrix)
    
    def compliment(self):
        compliment_matrix = self._matrix
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix)):
                compliment_matrix[i][j] = 1 - self._matrix[i][j]

        return compliment_matrix

    def min(self):
        inverse_matrix = self.inverse()
        strong_matrix = self._matrix - inverse_matrix
        min_elements = np.where(np.all(strong_matrix == 0, axis=0))[0]

        return min_elements
    
    def max(self):
        inverse_matrix = self.inverse()
        strong_matrix = self._matrix - inverse_matrix
        max_elements = np.where(np.all(strong_matrix == 0, axis=1))[0]

        return max_elements
    


matrix = np.array([
    [1, 0, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 1, 0]
])

BR = BinaryRelationship(matrix)

if BR.reflexive() == True:
    print("Relationship is reflexive")
else:
    print("Relationship is not reflexive")

if BR.antireflexive() == True:
    print("Relationship is antireflexive")
else:
    print("Relationship is not antireflexive")

if BR.symmetric() == True:
    print("Relationship is symmetric")
else:
    print("Relationship is not symmetric")

if BR.antisymmetric() == True:
    print("Relationship is antisymmetric")
else:
    print("Relationship is not antisymmetric")

if BR.asymmetric() == True:
    print("Relationship is asymmetric")
else:
    print("Relationship is not asymmetric")

if BR.transitive() == True:
    print("Relationship is transitive")
else:
    print("Relationship is not transitive")


print(f"Worst elemnts are: {BR.worst()}")

print(f"Best elemnts are: {BR.best()}")

print(f"Min elemnts are: {BR.min()}")

print(f"Max elemnts are: {BR.max()}")