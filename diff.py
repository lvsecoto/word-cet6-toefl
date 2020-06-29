import nltk
import pandas as pd

datat = pd.read_csv('p_toefl.txt', header=None)
data = pd.read_csv('p_cet6.txt', header=None)

datat.sort_values(by=0, inplace=True)
data.sort_values(by=0, inplace=True)
dtl=list(datat[0].apply(lambda x : str(x).lower()))
dl=list(data[0].apply(lambda x : str(x).lower()))

print('origin length',len(dtl))
for i in dl:
    if i in dtl:
        dtl.remove(i)
print('removed length',len(dtl))
dtl=list(set(dtl))
print('set length',len(dtl))

from nltk.stem import WordNetLemmatizer, PorterStemmer
porter = PorterStemmer()
wnl = WordNetLemmatizer()
#dtl.sort(reverse=True)
tokens = dtl
s_list=[]
for token in tokens:
    prot = token
    s_list.append(prot)

    #prot  = wnl.lemmatize(token) if wnl.lemmatize(token).endswith('e') else porter.stem(token) 
    #if not (prot+'e' in s_list):
    #    s_list.append(prot)


final_list=list(set(s_list))
print('set length',len(final_list))
final_list.sort()

ft=open('toefl.txt','r')
ff=ft.read()
fl=ff.split('\n')
ft.close()
s=''
for j in fl:
    j = j.lower()
    for i in final_list:
        if j.find(i)>=0 and len(i)>2 :
            s+=j+ '\n'

sout=list(set(s.split('\n')))
sout.sort()
print(len(sout), type(sout))
f=open('out.txt','w')        
sw = ''
for si in list(sout):
    sw=sw+si+'\n'

f.write(sw)
f.close()
