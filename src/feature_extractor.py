import numpy as np
import pandas as pd
import csv
from date_time import timevalue 
from process import categorize
from process import lr_holdtime


fr=open('date_Naman.txt','rb')   # date file of person whose features to train
info=fr.readlines() 
fw=open('info.csv','wb')

in_txt=csv.reader(info,delimiter='\t')
out_csv=csv.writer(fw)
out_csv.writerows(in_txt)

fr.close()
fw.close()
columns=['Event_Type','Key_Code','Shift','Alt','Control','Time']
df=pd.read_csv('info.csv')
if len(df.columns)>6:
    for i in range(len(df.columns)-1,5,-1):
        df=df.drop(df.columns[[i]],axis=1)
df.columns=columns;

del_rows=[10,38,39,40,41,165,161,163,162,164,166]
for i in del_rows:
    df=df[df.Key_Code!=i]
df=df[df.Alt==False]
df=df[df.Control==False]
df=df.drop('Alt',axis=1)
df=df.drop('Control',axis=1)

dates=df.Time.tolist()
dates=pd.Series(timevalue(dates))
df=df.reset_index()
df.Time=dates
df=df.drop('index',axis=1)




final_features=pd.DataFrame(columns=('lr','rl','lR','Lr','rL','Rl','lL','rR','ll','rr','l','r','L','R','Space','Enter',
                                     'Backspace','cpm'))

label=2

#initial value
index=-1
count=0

while index<len(df)-1:
    
    tmp_df=pd.DataFrame(columns=('Event_Type','Key_Code','Shift','Time'))
    feature_list=np.zeros((2,11))
    mean_latencies=np.zeros(11)
    i=0    
    index=index+1
    
    tmp=[df.Event_Type[index],df.Key_Code[index],df.Shift[index],df.Time[index]]
    tmp_df.loc[i]=tmp

    i=i+1

    while 1:
        
        if index>len(df)-1:
            break
        
        tmp=[df.Event_Type[index],df.Key_Code[index],df.Shift[index],df.Time[index]]
        if tmp[3]-tmp_df.Time[i-1]>10:
            break
        
        if tmp[3]-tmp_df.Time[0]>60:
            break
        
        tmp_df.loc[i]=tmp
        i=i+1
        index=index+1
            
    
    
    if len(tmp_df.Time)<100:
        continue
    
   ############################################################################
    #Calculating latencies of the different features

    
    
    for j in range(0,len(tmp_df.Time)-1):
        
        flag=0
        
        if tmp_df.Event_Type[j]=='KeyDown':
            for k in range(j+1,len(tmp_df.Time)):
                if tmp_df.Event_Type[k]=='KeyDown':
                    flag=1
                    chars=[tmp_df.Key_Code[j],tmp_df.Shift[j],tmp_df.Key_Code[k],tmp_df.Shift[k]]
                    latency=tmp_df.Time[k]-tmp_df.Time[j]
                    break
                
        if flag==1 and latency<1.5:           
            feature=categorize(chars)
            feature_list[0][feature]=feature_list[0][feature]+latency
            feature_list[1][feature]=feature_list[1][feature]+1
    
    mean_latencies=feature_list[0]/feature_list[1]
   ############################################################################            
    
    #Calculating hold times and number of backspaces and cpm
    feature_list_holdtime=np.zeros((2,7))
    backspaces=0
    characters=0
    cpm=float('NaN')
    backspace_per_character=float('NaN')
    
    for j in range(0,len(tmp_df.Time)-1):
        
        flag=0
        
        if tmp_df.Event_Type[j]=='KeyDown':
            key=tmp_df.Key_Code[j]    
            for k in range(j+1,len(tmp_df.Time)):
                if tmp_df.Key_Code[k]==key:
                    flag=1
                    chars=[key,tmp_df.Shift[j]]
                    holdtime=tmp_df.Time[k]-tmp_df.Time[j]
                    break
        
            characters=characters+1
            
            if key==9:
                backspaces=backspaces+1
                
        if flag==1 and holdtime<1.5:
            feature=lr_holdtime(chars)
            feature_list_holdtime[0][feature]=feature_list_holdtime[0][feature]+holdtime
            feature_list_holdtime[1][feature]=feature_list_holdtime[1][feature]+1
        
    mean_holdtime=feature_list_holdtime[0]/feature_list_holdtime[1]
        
    if characters>100:
        cpm=characters/(tmp_df.Time[len(tmp_df.Time)-1]-tmp_df.Time[0])*60
        backspace_per_character=float(backspaces)/characters
    
   ############################################################################
    
    mean_latencies=np.delete(mean_latencies,0,0)
    mean_holdtime=np.delete(mean_holdtime,0,0)    
    total_features=np.append(mean_latencies,mean_holdtime)
    total_features=np.append(total_features,backspace_per_character)
    total_features=np.append(total_features,cpm)
    
        
    
    final_features.loc[count]=total_features
    count=count+1    
    
    print count,'-',index, '-',len(tmp_df.Time)
    

           
#final_features.to_csv('tmp_final.csv')
new_final_features=final_features.dropna(how='all')
new_final_features=new_final_features.reset_index()
tmp=np.empty(len(new_final_features))
tmp.fill(label)

new_final_features['y'] = pd.Series(tmp)
new_final_features_median=new_final_features.fillna(final_features.median())
new_final_features_median.to_csv('final_median.csv',index=False)
new_final_features_mean=new_final_features.fillna(final_features.mean())
new_final_features_mean.to_csv('final_mean.csv',index=False)
