import pandas as pd

from SuRFM.db.sql_handler import SqlHandler

#____________________________________________________________________________________________

subscriber_handler=SqlHandler('subscription_database', 'subscriber')
sub_data=pd.read_csv('subscribers_data.csv')
#Inst.truncate_table()
subscriber_handler.insert_many(sub_data)
subscriber_handler.close_cnxn()

#____________________________________________________________________________________________

activities_handler=SqlHandler('subscription_database', 'activity')
activities_data=pd.read_csv('activities_data.csv')
#Inst.truncate_table()
activities_handler.insert_many(activities_data)
activities_handler.close_cnxn()

#____________________________________________________________________________________________

transaction_handler=SqlHandler('subscription_database', 'transactions')
transaction_data=pd.read_csv('transactions_data.csv')
#Inst.truncate_table()
transaction_handler.insert_many(transaction_data)
transaction_handler.close_cnxn()

#____________________________________________________________________________________________

payment_methods_handler=SqlHandler('subscription_database', 'payment_method')
payment_methods_data=pd.read_csv('payment_methods_data.csv')
#Inst.truncate_table()
payment_methods_handler.insert_many(payment_methods_data)
payment_methods_handler.close_cnxn()


#____________________________________________________________________________________________

rfm_segmentation_handler=SqlHandler('subscription_database', 'rfm_segmentation')
rfm_segmentation_data=pd.read_csv('rfm_segmentation_data.csv')
#Inst.truncate_table()
rfm_segmentation_handler.insert_many(rfm_segmentation_data)
rfm_segmentation_handler.close_cnxn()


#____________________________________________________________________________________________

retention_strategies_handler=SqlHandler('subscription_database', 'retention_strategy')
retention_strategies_data=pd.read_csv('retention_strategies_data.csv')
#Inst.truncate_table()
retention_strategies_handler.insert_many(retention_strategies_data)
retention_strategies_handler.close_cnxn()

#____________________________________________________________________________________________

clv_handler=SqlHandler('subscription_database', 'clv')
clv_data=pd.read_csv('clv_data.csv')
#Inst.truncate_table()
clv_handler.insert_many(clv_data)
clv_handler.close_cnxn()

