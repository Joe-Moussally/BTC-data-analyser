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
    print('Total Average: ',all_time_average)


    #calculating for each month
    #average each month
    years = []
    for element in data_list: #extract the years available
        print(element[0].year)
        time = {'year':element[0].year,'month':element[0].month}
        if(time not in years):
            years.append(time)
    print(years)

analyser()