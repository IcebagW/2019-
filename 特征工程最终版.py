#coding=utf-8
'''
__byIce_bag
'''
import numpy
import pandas as pd
import featuretools as ft
applys_data=pd.read_csv('F:/anaconda/envs/math_modeling/data/Model_Train_Val_Data.csv',error_bad_lines=True)

applys_label=pd.read_csv('F:/anaconda/envs/math_modeling/data/Model_Train_Val_Label.csv',error_bad_lines=True)

apply_create_dt=applys_data.groupby('apply_id')['apply_create_dt'].mean()

apply_real_dt=applys_data.groupby('apply_id')['apply_real_dt'].mean()

apply_id=applys_label['apply_id']
apply_list=[]
for i in range(0,185137):
    apply_list.append(apply_id[i])

apply_label_data=applys_label['label']
apply_label=[]
for i in range(0,185137):
    apply_label.append(apply_label_data[i])

entry_times=applys_data.groupby('apply_id')['entry_time'].nunique()
entry_ip=applys_data.groupby('apply_id')['ip'].nunique()
entry_type=applys_data.groupby('apply_id')['entry_type'].nunique()


time=[]
for i in apply_list:
    time.append(feature['apply_real_dt'][i]-feature['apply_create_dt'][i])

feature=pd.DataFrame({
                      'time':time,
                      'entry_ip':entry_ip,
                      'entry_type':entry_type,
                      'entry_times':entry_times,
                      'label':apply_label
                        
    
                    },index=apply_list
    

)