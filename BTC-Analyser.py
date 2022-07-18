import io
import pandas as pd

def analyser():
    print('TEST')
    data = pd.read_excel(io='./csv example.xlsx',sheet_name='BAVERAGE-USD-Sols')
    print(data)

analyser()