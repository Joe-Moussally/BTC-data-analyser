import sys
import pandas as pd

def analyser():

    path = input('Enter path of excel file: ')

    print('TEST')
    data = pd.read_excel(io=path,sheet_name='BAVERAGE-USD-Sols')

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
    dates = []
    for element in data_list: #extract the years available
        print(element[0].year)
        time = {'year':element[0].year,'month':element[0].month}
        if(time not in dates):
            dates.append(time)
    print(dates)

    #calculate the average for each month
    for date in dates:
        values = []
        for value in data_list:
            value_date = {'year':value[0].year,'month':value[0].month}
            if(date == value_date):
                values.append(value[1])

        avg_value = 0
        sum = 0

        max_value = 0
        min_value = values[0]

        for value in values:
            #compare min value
            if(value < min_value):
                min_value = value
            
            #compare max value
            if(value>max_value):
                max_value = value
            
            sum += value
        
        avg_value = sum / len(values)
        print('---------',date['year'],'/',date['month'],'---------')
        print('Min Value:',min_value)
        print('Max Value:',max_value)
        print('Avg Value:',avg_value)

           


analyser()