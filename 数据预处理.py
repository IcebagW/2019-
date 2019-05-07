import pandas as pd
import featuretools as ft
applys_data=pd.read_csv('F:/anaconda/envs/mathematical modeling/data/Model_Train_Val_Data.csv',error_bad_lines=True)

applys_label=pd.read_csv('F:/anaconda/envs/mathematical modeling/data/Model_Train_Val_Label.csv',error_bad_lines=True)

apply_id_data=applys_data['apply_id']
apply_create_dt_data=applys_data['apply_create_dt']
apply_real_dt_data=applys_data['apply_real_dt']
apply_expect_dt_data=applys_data['apply_expect_dt']




apply_id=applys_label['apply_id']
apply_list=[]
for i in range(0,185137):
    apply_list.append(apply_id[i])
    
apply_create_dt=pd.Series(apply_list,index=apply_list)
apply_real_dt=pd.Series(apply_list,index=apply_list)
apply_expect_dt=pd.Series(apply_list,index=apply_list)

        
        
apply_create_dt[apply_id_data[0]]=apply_create_dt_data[0]
for i in range(1,17550531):
   if apply_create_dt_data[i]!=apply_create_dt_data[i+1]:
        apply_create_dt[apply_id_data[i]]=apply_create_dt_data[i]
print("*"*100)


apply_real_dt[apply_id_data[0]]=apply_real_dt_data[0]
for i in range(1,17550531):
   if apply_real_dt_data[i]!=apply_real_dt_data[i+1]:
        apply_real_dt[apply_id_data[i]]=apply_real_dt_data[i]
print("*"*100)

apply_expect_dt[apply_id_data[0]]=apply_expect_dt_data[0]
for i in range(1,17550531):
   if apply_expect_dt_data[i]!=apply_expect_dt_data[i+1]:
        apply_expect_dt[apply_id_data[i]]=apply_expect_dt_data[i]
print("*"*100)


entry_times=applys_data.groupby('apply_id')['entry_time'].nunique()

lists_1=pd.DataFrame({
                    'apply_create_dt':apply_create_dt,

                     'apply_list':apply_list,
                    
                    },index=apply_list
    

)

lists_2=pd.DataFrame({
                   
                    'apply_real_dt':apply_real_dt,

                     'apply_list':apply_list,
                   
                    },index=apply_list
    

)

lists_3=pd.DataFrame({

                     'apply_list':apply_list,
					 
                    'apply_expect_dt':apply_expect_dt,
					
                    },index=apply_list
    

)

lists_4=pd.DataFrame({

                     'apply_list':apply_list,
					 
                    'entry_times':entry_times
					
                    },index=apply_list
    

)
es=es.entity_from_dataframe(entity_id='lists_1',dataframe=lists_1,index='apply_list')
es=es.entity_from_dataframe(entity_id='lists_2',dataframe=lists_2,index='apply_list')
es=es.entity_from_dataframe(entity_id='lists_3',dataframe=lists_3,index='apply_list')
es=es.entity_from_dataframe(entity_id='lists_4',dataframe=lists_3,index='apply_list')
