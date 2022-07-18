import io
import pandas as pd

def analyser():
    print('TEST')
    data = pd.read_excel(io='./csv example.xlsx',sheet_name='BAVERAGE-USD-Sols')

    #transforming dataframe to list
    data_list = data.values.tolist()
    print(data_list[0][1])

    #calculating the all time average
    sum = 0
    for element in data_list:
        sum += element[1]
    all_time_average = sum / (len(data_list))
    print(all_time_average)

analyser()