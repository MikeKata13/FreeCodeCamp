def calculate(list):
    import numpy as np
    if (len(list)) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
        matrix = np.array(list).reshape(3,3)

    mean = [np.mean(matrix,axis=0).tolist(), np.mean(matrix,axis=1).tolist() , matrix.flatten().mean()]
    variance = [np.var(matrix, axis = 0).tolist(), np.var(matrix, axis = 1).tolist(), matrix.flatten().var()]
    standard  = [np.std(matrix, axis = 0).tolist(), np.std(matrix, axis = 1).tolist(), matrix.flatten().std()]
    max= [np.amax(matrix, axis = 0).tolist(), np.amax(matrix, axis = 1).tolist(), matrix.flatten().max()]
    min = [np.amin(matrix, axis = 0).tolist(), np.amin(matrix, axis = 1).tolist(), matrix.flatten().min()]
    sum = [np.sum(matrix, axis = 0).tolist(), np.sum(matrix, axis = 1).tolist(), matrix.flatten().sum()]
    calculations = {'mean': mean, 'variance': variance, 'standard deviation': standard, 'max': max, 'min': min, 'sum': sum}
    return calculations
