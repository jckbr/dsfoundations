import numpy
import pandas
from pandas_datareader import data

# 1
headers = [numpy.array(['', 'Price', 'Price', 'Price', 'Price to Earnings Ratio (P/E)', 'Price to Earnings Ratio (P/E)', 'Price to Earnings Ratio (P/E)']), numpy.array(['Dates', 'Facebook', 'Google', 'Microsoft', 'Facebook', 'Google', 'Microsoft'])]
dates = [pandas.date_range("6/5/2017", freq = "D", periods = 5)]
dataFrame = pandas.DataFrame([[dates[0][0], 155, 955, 66, 37.10, 32.0, 30.31],
                              [dates[0][1], 150, 987, 69, 36.98, 31.3, 30.59],
                              [dates[0][2], 153, 963, 62, 36.78, 31.7, 30.46],
                              [dates[0][3], 155, 1000, 61, 36.11, 31.2, 30.11],
                              [dates[0][4], 156, 1012, 66, 37.07, 30.0, 31.00]], columns = headers)
print("1:\n", dataFrame, "\n")

# 2
dataFrame2 = dataFrame.set_index([('', 'Dates')])
print("2:\n", dataFrame2.loc['2017-06-05', :], "\n")

# 3
avgDataFrame = pandas.DataFrame({'Avg Price': [numpy.mean(dataFrame[('Price', 'Facebook')]), numpy.mean(dataFrame[('Price', 'Google')]), numpy.mean(dataFrame[('Price', 'Microsoft')])], 'Avg P/E': [numpy.mean(dataFrame[('Price to Earnings Ratio (P/E)', 'Facebook')]), numpy.mean(dataFrame[('Price to Earnings Ratio (P/E)', 'Google')]), numpy.mean(dataFrame[('Price to Earnings Ratio (P/E)', 'Microsoft')])]}, index = ['Facebook', 'Google', 'Microsoft'])
print("3:\n", avgDataFrame, "\n")

# 4
studentDataFrame = pandas.DataFrame({'Name': ['John', 'Bob', 'Suzan'], 'Age':[20, 30, 22]})
courseDataFrame = pandas.DataFrame({'Department': ['CS', 'CS', 'ENGL'], 'Course Number': [233, 455, 433], 'Description': ['FILL', 'FILL', 'FILL']})
takesDataFrame = pandas.DataFrame({'Department': ['CS', 'CS', 'ENGL'], 'Course Number': [233, 455, 433], 'Grade': ['C', 'B', 'A']})

studentInfoDataFrame = (studentDataFrame.join(courseDataFrame)).merge(takesDataFrame, how = 'left')
print("4:")
print("studentDataFrame:\n", studentDataFrame, "\n")
print("courseDataFrame:\n", courseDataFrame, "\n")
print("takesDataFrame:\n", takesDataFrame, "\n")
print("Combined dataframe (studentInfoDataFrame):\n", studentInfoDataFrame, "\n")

# 5
gradeScaleDataFrame = pandas.DataFrame({'Grade': ['A', 'B', 'C', 'D', 'E', ''], 'Points': [4, 3, 2, 1, 0, 0]})
studentInfoDataFrame = studentInfoDataFrame.merge(gradeScaleDataFrame, how = 'left')
print("5:\n", studentInfoDataFrame, "\n")

# 6
print("6:\n", studentInfoDataFrame.loc[studentInfoDataFrame['Grade'] == '', 'Name'], "\n")

# 7
dateSeries = pandas.Series(pandas.bdate_range("1/1/2018", "12/31/2018"))
dateSeriesSwapped = pandas.Series(dateSeries.index.values, index = dateSeries)
print("7:\n", dateSeriesSwapped, "\n")

# 8
dayHeaders = numpy.array(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
countData = numpy.empty(0)
for day in dayHeaders:
    countData = numpy.append(countData, len(pandas.date_range('2018-01-01', '2018-12-31', freq = ('W-' + day))))
dayCountDataFrame = pandas.DataFrame([countData], columns = dayHeaders, index = ['2018'], dtype = 'int')
print("8:\n", dayCountDataFrame, "\n")

# 9
GOOGdata = data.DataReader('GOOG', 'yahoo', start = '2017', end = '2018')
GOOGdata['Profit'] = GOOGdata['Open'] - GOOGdata['Close']
daysOfWeek = pandas.DataFrame({'Day': [0, 1, 2, 3, 4, 5, 6], 'Name': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']})
GOOGdata['Day'] = pandas.to_datetime(GOOGdata.index).dayofweek
GOOGdata = GOOGdata.merge(daysOfWeek, how = 'left')

GOOGdataFrame = ((GOOGdata[['Name', 'Profit']].copy()).groupby('Name').sum()).reindex(index = daysOfWeek['Name'][:5]).rename_axis('DOW')
print("9:\n", GOOGdataFrame)