import pandas as pd
data=pd.read_csv('Workbook2.csv')
#print(data)


print(data.columns.values)
print(data['ID'])
print(data['BRANCH'])
print(data[['ID','CHEMISTRY','PHYSICS']])
print(data['ID'].tolist())
#data=data.fillna('Nan')
#print(data)

#data=data.dropna()   #remove missing data
#print(data)


data['TOTAL']=data['MATHS']+data['PHYSICS']+data['CHEMISTRY']
print(data)

print(data[data['TOTAL']>200])


#print(data.drop(['CHEMISTRY','PHYSICS'],axis=1))


data['CHEMISTRY_RESULT']= data['CHEMISTRY'].apply(lambda x: 'pass' if x>35 else 'fail')
print(data)


data.to_csv('data.csv')


