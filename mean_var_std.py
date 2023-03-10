import numpy as np


def calculate(list):
  if(len(list) !=9 ):
    raise ValueError("List must contain nine numbers.")

  
  a = np.array(list)
  mean_columns = ([
    a[[0, 3, 6]].mean(), a[[1, 4, 7]].mean(), a[[2, 5, 8]].mean()
  ])
  mean_rows = [a[[0, 1, 2]].mean(), a[[3, 4, 5]].mean(), a[[6, 7, 8]].mean()]

  var_columns = ([a[[0, 3, 6]].var(), a[[1, 4, 7]].var(), a[[2, 5, 8]].var()])
  var_rows = [a[[0, 1, 2]].var(), a[[3, 4, 5]].var(), a[[6, 7, 8]].var()]

  std_columns = ([a[[0, 3, 6]].std(), a[[1, 4, 7]].std(), a[[2, 5, 8]].std()])
  std_rows = [a[[0, 1, 2]].std(), a[[3, 4, 5]].std(), a[[6, 7, 8]].std()]

  max_columns = ([a[[0, 3, 6]].max(), a[[1, 4, 7]].max(), a[[2, 5, 8]].max()])
  max_rows = [a[[0, 1, 2]].max(), a[[3, 4, 5]].max(), a[[6, 7, 8]].max()]

  min_columns = ([a[[0, 3, 6]].min(), a[[1, 4, 7]].min(), a[[2, 5, 8]].min()])
  min_rows = [a[[0, 1, 2]].min(), a[[3, 4, 5]].min(), a[[6, 7, 8]].min()]

  sum_columns = ([a[[0, 3, 6]].sum(), a[[1, 4, 7]].sum(), a[[2, 5, 8]].sum()])
  sum_rows = [a[[0, 1, 2]].sum(), a[[3, 4, 5]].sum(), a[[6, 7, 8]].sum()]

  
  return {
    'mean': [mean_columns, mean_rows, a.mean()],
    'variance': [var_columns, var_rows, a.var()],
    'standard deviation': [std_columns, std_rows, a.std()],
    'max': [max_columns, max_rows, a.max()],
    'min': [min_columns, min_rows, a.min()],
    'sum': [sum_columns, sum_rows, a.sum()]
  }
