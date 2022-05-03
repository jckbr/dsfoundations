import pandas
import matplotlib.pyplot as plt
pandas.set_option('display.max.colwidth', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)

titanicData = pandas.read_csv('titanic.csv')
nbaData = pandas.read_csv('nba_2013.csv')

# 1
survivalData = titanicData.groupby(['pclass', 'sex']).survived.sum()
survivalDataPerc = survivalData.div(survivalData.sum(level = 0), level = 0, )

print(survivalData)
print(survivalDataPerc)

survivalData.unstack().plot(kind = 'bar')
plt.ylabel("Number of survivors")
plt.xlabel("Passenger class")
plt.title("Number of survivors by class and gender")
plt.show()
survivalDataPerc.unstack().plot(kind = 'line')
plt.ylabel("Surival Percentage")
plt.xlabel("Passenger class")
plt.title("Percentage of survivors by class and gender")
plt.show()

# 2
playerData = nbaData.groupby('age')['pts'].mean()
playerData.plot(kind = 'bar')
plt.ylabel("Points Scored")
plt.xlabel("Player Age")
plt.title("Average Points Scored by Age")
plt.show()

# 3
playerData = pandas.DataFrame(nbaData)
print(playerData)
playerData.plot(kind = 'scatter', x = 'age', y = 'pts')
plt.ylabel("Points Scored")
plt.xlabel("Player Age")
plt.title("Average Points Scored by Age")
plt.show()
#   The scatter plot is difficult to understand how many points are scored per
#   age range since some ages might score a lot but only a few points at a time
#   and some may only score a lot of points once