import numpy as np
import pandas

# 1
primeNumbers = pandas.Series([], copy=False, dtype=object)

for num in range(2, 101):
    prime = True
    for i in range(2, num):
        if(num % i == 0):
            prime = False
    if prime:
        if len(primeNumbers) < 10:
            primeNumbers[len(primeNumbers)] = num

# 2
print("2 Prime numbers at odd indices:\n", primeNumbers.iloc[1::2], "\n")

# 5
dataFrame = {'id': [2, 5, 10, 15, 20], 'first_name': ['Jason', 'Jason', 'Tina', 'Jake', 'Amy'], 'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 'age': [42, 52, 36, 24, 73], 'preTestScore': [4, 24, 31, 2, 3], 'postTestScore': [25, 94, 57, 62, 70]}
pdf = pandas.DataFrame(data = dataFrame)
print("5 Pandas DataFrame (pdf):\n", pdf, "\n")

# 6
pdf6 = pdf.set_index('id')
print("6 pdf with id as index:\n", pdf6, "\n")

# 7
print("7 first_name column of pdf:\n", pdf6['first_name'], "\n")

# 8
print("8 Age of Tina:", pdf.loc[pdf['first_name'] == 'Tina', 'age'].item(), "\n")

# 9
pdfDiffMean = pdf[['preTestScore', 'postTestScore']].diff(axis=1)
print("9 Mean difference of pre and post test scores:", pdfDiffMean['postTestScore'].mean(), "\n")

# 10
pdf.loc[pdf['first_name'].isin(['Amy', 'Jake']), 'postTestScore'] = np.NaN
print("10 Set postTestScore of Amy and Jake to NaN:\n", pdf, "\n")

# 11
print("11 Show all rows where there is no NaN:\n", pdf[~pdf.isnull().any(axis=1)], "\n")

# 12
pdf.reset_index()
pdf12 = pdf.set_index(['first_name', 'last_name'])
print("12 Set index of pdf to first_name and last_name:\n", pdf12, "\n")

#  di13
print("13 Show age of Tina in new DataFrame:\n", pdf12.loc['Amy']['age'], "\n")