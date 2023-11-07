import pandas as pd
data = pd.read_csv(r'D:\pycharmpractice\bishi\fyx_chinamoney.csv')
li = []
li.append(112282672)
for i in data['112282672']:
    li.append(i)
def split_list(lst,size):
    return [lst[i:i+size] for i in range(0,len(lst),size)]
result = split_list(li,80)
print(result)
for i in result:
    print(i)