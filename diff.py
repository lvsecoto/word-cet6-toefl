
import pandas as pd

datat = pd.read_csv('p_toefl.txt', header=None)
data = pd.read_csv('p_cet6.txt', header=None)

datat.sort_values(by=0, inplace=True)
data.sort_values(by=0, inplace=True)
dtl=datat[0].apply(lambda x : str(x).lower())
dl=data[0].apply(lambda x : str(x).lower())

for i in dl:
    if i in dtl:
        dtl.remove(i)

s=''
for i in dtl:
    s+=i+'\n'

f=open('out.txt','w')        
f.write(s)
f.close()
