import pandas as pd
import numpy as np
from datetime import datetime,timedelta
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

today_date = datetime.now().date()
today_day = datetime.now().strftime('%A')
print today_date
print today_day



################################################################## Next 7 days Dataframe [X_pred]
date_list = []
date_type_list = []
for i in range(0,7):
    date_list.append((datetime.today() + timedelta(days=i)).strftime('%d-%m-%y'))
    date_type_list.append((datetime.today() + timedelta(days=i)).strftime('%A'))
print (date_type_list,date_list)
date_type = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
test_dict = {}
for i in date_list:
    test_dict[str(i)] = ''
test_list = [test_dict]

df_test = pd.DataFrame(test_list).transpose()
df_test.columns = ["Sales"]
df_test.index = pd.to_datetime(df_test.index, format = '%d-%m-%y')
df_test['Weekday'] = df_test.index.weekday
df_test['Year'] = df_test.index.year
df_test['Month'] = df_test.index.month
df_test['Date'] = df_test.index.day

X_pred = df_test[['Weekday','Date', 'Month','Year']].values


################################################################## Data Collection

data = get_query_result(4969)['rows']
print ("All Data:",len(data))

###################################################### Extracting Box8-own records only
new_data = []
for row in data:
    if str(row['brand']) == '1' and str(row['seller']) == 'own':
        new_data.append(row)
print ("Box8-own Count:",len(new_data))
data = new_data

distinct_outlet_list = [row['outlet'] for row in data]
distinct_outlet_list = list(set(distinct_outlet_list))
print list(set(distinct_outlet_list))

################################################################## Model Building along with ML ALgo for each outlet

train_score = []
test_score = []
all_data = []
for outlet in distinct_outlet_list:    
    new_data = []
    temp_data = {}
    ready_df = {}
    all_sales = []
    for row in data:
        if outlet == row['outlet']:
            temp_data['outlet'] = row['outlet']
            temp_data['city'] = row['city']
            temp_data[row['bill_date']] = float(row['sales'])
            all_sales.append(float(row['sales']))
    temp_data['mean_sales'] = np.mean(all_sales)
    temp_data['std_sales'] = np.std(all_sales)
    lower_bound = temp_data['mean_sales'] - temp_data['std_sales']
    upper_bound = temp_data['mean_sales'] + temp_data['std_sales']
    
    ################################################################## overall outlier hatana
    # for k,v in temp_data.items():
    #     if k not in ['city','outlet','mean_sales','std_sales']:
    #         if v > upper_bound or v < lower_bound:
    #             # print "hello"
    #             del temp_data[k]
    ready_df = dict(temp_data)
    del ready_df['outlet']
    del ready_df['mean_sales']
    del ready_df['std_sales']
    del ready_df['city']
    new_data.append(ready_df)
    df = pd.DataFrame(new_data)
    df = df.transpose()
    df.columns = ["Sales"]
    df.index = pd.to_datetime(df.index, format = '%Y-%m-%d')
    df['Weekday'] = df.index.weekday
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    df['Date'] = df.index.day
    
    ###################################################### DOW dekh k Outlier hatana
    for i in range(0,7):
        mean = np.mean((df.loc[df['Weekday'] == i ])['Sales'].values.tolist())
        std = np.std((df.loc[df['Weekday'] == i ])['Sales'].values.tolist())
        df.loc[df['Weekday'] == i , 'Mean'] = mean
        df.loc[df['Weekday'] == i , 'Std'] = std
        
    df = df[(df['Sales'] >= (df['Mean'] - 2*df['Std'])) & (df['Sales'] <= (df['Mean'] + 0*df['Std']))]
    ###########################
    
    df_all = []
    df_all.append((df.loc[df['Weekday'] == 0])['Sales'].values.tolist())
    df_all.append((df.loc[df['Weekday'] == 1])['Sales'].values.tolist())
    df_all.append((df.loc[df['Weekday'] == 2])['Sales'].values.tolist())
    df_all.append((df.loc[df['Weekday'] == 3])['Sales'].values.tolist())
    df_all.append((df.loc[df['Weekday'] == 4])['Sales'].values.tolist())
    df_all.append((df.loc[df['Weekday'] == 5])['Sales'].values.tolist())
    df_all.append((df.loc[df['Weekday'] == 6])['Sales'].values.tolist())
    # print ("Test",outlet,len(df_all[0]),len(df_all[1]),len(df_all[2]),len(df_all[3]),len(df_all[4]),len(df_all[5]),len(df_all[6]), len(df_all[date_type[str(date_type_list[0])]]) )
    if (len(df_all[0])+len(df_all[1])+len(df_all[2])+len(df_all[3])+len(df_all[4])+len(df_all[5])+len(df_all[6])) <= 14:
        print (outlet, " is very new")
        final_row = {}
        final_row['outlet'] = outlet
        final_row['Monday Prediction'] = 0.0
        final_row['Tuesday Prediction'] = 0.0
        final_row['Wednesday Prediction'] = 0.0
        final_row['Thursday Prediction'] = 0.0
        final_row['Friday Prediction'] = 0.0
        final_row['Saturday Prediction'] = 0.0
        final_row['Sunday Prediction'] = 0.0
        all_data.append(final_row)
        # add_result_row(result, final_row)
        continue
    
    # X = df['Weekday'].values.reshape(-1,1)
    X = df[['Weekday','Date', 'Month','Year']].values
    y = df['Sales'].values.reshape(-1,1)
    X_train, X_test, Y_train, Y_test = train_test_split (X, y, test_size = 0.20, random_state = 1)
    
    regressor_backup = RandomForestRegressor(n_estimators = 1000, criterion='mse', random_state = 42)
    regressor_backup.fit(X_train, Y_train)
    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)
    
    train_score = (regressor.score(X_train, Y_train))   ## And score it on your training data.
    test_score = (regressor.score(X_test, Y_test))   ## And score it on your testing data.
    y_pred = regressor.predict(X_pred)
    y_pred_backup = regressor_backup.predict(X_pred)
    # print ("Test:",outlet, y_pred[0], df_all[date_type[str(date_type_list[0])]], 
        # ((np.mean(df_all[date_type[str(date_type_list[0])]])*0.40) + (y_pred[0]*0.40) + (df_all[date_type[str(date_type_list[0])]][-1]*0.10) + (df_all[date_type[str(date_type_list[0])]][-2]*0.10))
        # )
    final_row = {}
    final_row['outlet'] = outlet
    final_row['accuracy'] = str(train_score) + "," + str(test_score)
    try:
        if (y_pred[0][0]*0.40) < 800 and (y_pred[0][0]*0.40) > 90000:
            final_row[str(date_type_list[0])+" Prediction"] = ((np.mean(df_all[date_type[str(date_type_list[0])]])*0.40) + (y_pred[0][0]*0.40) + (df_all[date_type[str(date_type_list[0])]][-1]*0.10) + (df_all[date_type[str(date_type_list[0])]][-2]*0.10))
            final_row[str(date_type_list[0])+" ML_Prediction"] = y_pred[0][0]
        else:
            final_row[str(date_type_list[0])+" Prediction"] = ((np.mean(df_all[date_type[str(date_type_list[0])]])*0.40) + (y_pred_backup[0]*0.40) + (df_all[date_type[str(date_type_list[0])]][-1]*0.10) + (df_all[date_type[str(date_type_list[0])]][-2]*0.10))
            final_row[str(date_type_list[0])+" ML_Prediction"] = y_pred_backup[0]
        final_row[str(date_type_list[0])+" Previous"] = str(df_all[date_type[str(date_type_list[0])]])
    except:
        final_row[str(date_type_list[0])+" Prediction"] = 0
        final_row[str(date_type_list[0])+" ML_Prediction"] = y_pred[0][0]
        final_row[str(date_type_list[0])+" Previous"] = str(df_all[date_type[str(date_type_list[0])]])
    
    try:
        if (y_pred[1][0]*0.40) < 800 and (y_pred[1][0]*0.40) > 90000:
            final_row[str(date_type_list[1])+" Prediction"] = ((np.mean(df_all[date_type[str(date_type_list[1])]])*0.40) + (y_pred[1][0]*0.40) + (df_all[date_type[str(date_type_list[1])]][-1]*0.10) + (df_all[date_type[str(date_type_list[1])]][-2]*0.10))
            final_row[str(date_type_list[1])+" ML_Prediction"] = y_pred[1][0]
        else:
            final_row[str(date_type_list[1])+" Prediction"] = ((np.mean(df_all[date_type[str(date_type_list[1])]])*0.40) + (y_pred_backup[1]*0.40) + (df_all[date_type[str(date_type_list[1])]][-1]*0.10) + (df_all[date_type[str(date_type_list[1])]][-2]*0.10))
            final_row[str(date_type_list[1])+" ML_Prediction"] = y_pred_backup[1]
        final_row[str(date_type_list[1])+" Previous"] = str(df_all[date_type[str(date_type_list[1])]])
    except:
        final_row[str(date_type_list[1])+" Prediction"] = 0
        final_row[str(date_type_list[1])+" ML_Prediction"] = y_pred[1][0]
        final_row[str(date_type_list[1])+" Previous"] = str(df_all[date_type[str(date_type_list[1])]])

    try:
        if (y_pred[2][0]*0.40) < 800 and (y_pred[2][0]*0.40) > 90000:
            final_row[str(date_type_list[2])+" Prediction"] = ((np.mean(df_all[date_type[str(date_type_list[2])]])*0.40) + (y_pred[2][0]*0.40) + (df_all[date_type[str(date_type_list[2])]][-1]*0.10) + (df_all[date_type[str(date_type_list[2])]][-2]*0.10))
            final_row[str(date_type_list[2])+" ML_Prediction"] = y_pred[2][0]
        else:
            final_row[str(date_type_list[2])+" Prediction"] = ((np.mean(df_all[date_type[str(date_type_list[2])]])*0.40) + (y_pred_backup[2]*0.40) + (df_all[date_type[str(date_type_list[2])]][-1]*0.10) + (df_all[date_type[str(date_type_list[2])]][-2]*0.10))
            final_row[str(date_type_list[2])+" ML_Prediction"] = y_pred_backup[2]
        final_row[str(date_type_list[2])+" Previous"] = str(df_all[date_type[str(date_type_list[2])]])
    except:
        final_row[str(date_type_list[2])+" Prediction"] = 0
        final_row[str(date_type_list[2])+" ML_Prediction"] = y_pred[2][0]
        final_row[str(date_type_list[2])+" Previous"] = str(df_all[date_type[str(date_type_list[2])]])
    
    try:
        if (y_pred[3][0]*0.40) < 800 and (y_pred[3][0]*0.40) > 90000:
            final_row[str(date_type_list[3])+" Prediction"] = ((np.mean(df_all[date_type[str(date_type_list[3])]])*0.40) + (y_pred[3][0]*0.40) + (df_all[date_type[str(date_type_list[3])]][-1]*0.10) + (df_all[date_type[str(date_type_list[3])]][-2]*0.10))
            final_row[str(date_type_list[3])+" ML_Prediction"] = y_pred[3][0]
        else:
            final_row[str(date_type_list[3])+" Prediction"] = ((np.mean(df_all[date_type[str(date_type_list[3])]])*0.40) + (y_pred_backup[3]*0.40) + (df_all[date_type[str(date_type_list[3])]][-1]*0.10) + (df_all[date_type[str(date_type_list[3])]][-2]*0.10))
            final_row[str(date_type_list[3])+" ML_Prediction"] = y_pred_backup[3]
        final_row[str(date_type_list[3])+" Previous"] = str(df_all[date_type[str(date_type_list[3])]])
    except:
        final_row[str(date_type_list[3])+" Prediction"] = 0
        final_row[str(date_type_list[3])+" ML_Prediction"] = y_pred[3][0]
        final_row[str(date_type_list[3])+" Previous"] = str(df_all[date_type[str(date_type_list[3])]])
    
    try:
        if (y_pred[4][0]*0.40) < 800 and (y_pred[4][0]*0.40) > 90000:
            final_row[str(date_type_list[4])+" Prediction"] = ((np.mean(df_all[date_type[str(date_type_list[4])]])*0.40) + (y_pred[4][0]*0.40) + (df_all[date_type[str(date_type_list[4])]][-1]*0.10) + (df_all[date_type[str(date_type_list[4])]][-2]*0.10))
            final_row[str(date_type_list[4])+" ML_Prediction"] = y_pred[4][0]
        else:
            final_row[str(date_type_list[4])+" Prediction"] = ((np.mean(df_all[date_type[str(date_type_list[4])]])*0.40) + (y_pred_backup[4]*0.40) + (df_all[date_type[str(date_type_list[4])]][-1]*0.10) + (df_all[date_type[str(date_type_list[4])]][-2]*0.10))
            final_row[str(date_type_list[4])+" ML_Prediction"] = y_pred_backup[4]
        final_row[str(date_type_list[4])+" Previous"] = str(df_all[date_type[str(date_type_list[4])]])
    except:
        final_row[str(date_type_list[4])+" Prediction"] = 0
        final_row[str(date_type_list[4])+" ML_Prediction"] = y_pred[4][0]
        final_row[str(date_type_list[4])+" Previous"] = str(df_all[date_type[str(date_type_list[4])]])

    try:
        if (y_pred[5][0]*0.40) < 800 and (y_pred[5][0]*0.40) > 90000:
            final_row[str(date_type_list[5])+" Prediction"] = ((np.mean(df_all[date_type[str(date_type_list[5])]])*0.40) + (y_pred[5][0]*0.40) + (df_all[date_type[str(date_type_list[5])]][-1]*0.10) + (df_all[date_type[str(date_type_list[5])]][-2]*0.10))
            final_row[str(date_type_list[5])+" ML_Prediction"] = y_pred[5][0]
        else:
            final_row[str(date_type_list[5])+" Prediction"] = ((np.mean(df_all[date_type[str(date_type_list[5])]])*0.40) + (y_pred_backup[5]*0.40) + (df_all[date_type[str(date_type_list[5])]][-1]*0.10) + (df_all[date_type[str(date_type_list[5])]][-2]*0.10))
            final_row[str(date_type_list[5])+" ML_Prediction"] = y_pred_backup[5]
        final_row[str(date_type_list[5])+" Previous"] = str(df_all[date_type[str(date_type_list[5])]])
    except:
        final_row[str(date_type_list[5])+" Prediction"] = 0
        final_row[str(date_type_list[5])+" ML_Prediction"] = y_pred[5][0]
        final_row[str(date_type_list[5])+" Previous"] = str(df_all[date_type[str(date_type_list[5])]])

    try:
        if (y_pred[6][0]*0.40) < 800 and (y_pred[6][0]*0.40) > 90000:
            final_row[str(date_type_list[6])+" Prediction"] = ((np.mean(df_all[date_type[str(date_type_list[6])]])*0.40) + (y_pred[6][0]*0.40) + (df_all[date_type[str(date_type_list[6])]][-1]*0.10) + (df_all[date_type[str(date_type_list[6])]][-2]*0.10))
            final_row[str(date_type_list[6])+" ML_Prediction"] = y_pred[6][0]
        else:
            final_row[str(date_type_list[6])+" Prediction"] = ((np.mean(df_all[date_type[str(date_type_list[6])]])*0.40) + (y_pred_backup[6]*0.40) + (df_all[date_type[str(date_type_list[6])]][-1]*0.10) + (df_all[date_type[str(date_type_list[6])]][-2]*0.10))
            final_row[str(date_type_list[6])+" ML_Prediction"] = y_pred_backup[6]
        final_row[str(date_type_list[6])+" Previous"] = str(df_all[date_type[str(date_type_list[6])]])
    except:
        final_row[str(date_type_list[6])+" Prediction"] = 0
        final_row[str(date_type_list[6])+" ML_Prediction"] = y_pred[6][0]
        final_row[str(date_type_list[6])+" Previous"] = str(df_all[date_type[str(date_type_list[6])]])

    all_data.append(final_row)
dataset = pd.DataFrame(all_data)
dataset.fillna(0, inplace=True)
result['rows'] = dataset.to_dict('records')
    # add_result_row(result, final_row)
    # df_1 = pd.DataFrame({'Actual': Y_test.flatten(), 'Predicted': y_pred.flatten()})
    # print ("Prediction:", y_pred)
    # break
print len(temp_data)
print df

add_result_column(result, "outlet", "", "string")
add_result_column(result, "accuracy", "", "string")
add_result_column(result, str(date_type_list[0])+" ML_Prediction", "", "string")
add_result_column(result, str(date_type_list[0])+" Prediction", "", "string")
add_result_column(result, str(date_type_list[0])+" Previous", "", "string")
add_result_column(result, str(date_type_list[1])+" ML_Prediction", "", "string")
add_result_column(result, str(date_type_list[1])+" Prediction", "", "string")
add_result_column(result, str(date_type_list[1])+" Previous", "", "string")
add_result_column(result, str(date_type_list[2])+" ML_Prediction", "", "string")
add_result_column(result, str(date_type_list[2])+" Prediction", "", "string")
add_result_column(result, str(date_type_list[2])+" Previous", "", "string")
add_result_column(result, str(date_type_list[3])+" ML_Prediction", "", "string")
add_result_column(result, str(date_type_list[3])+" Prediction", "", "string")
add_result_column(result, str(date_type_list[3])+" Previous", "", "string")
add_result_column(result, str(date_type_list[4])+" ML_Prediction", "", "string")
add_result_column(result, str(date_type_list[4])+" Prediction", "", "string")
add_result_column(result, str(date_type_list[4])+" Previous", "", "string")
add_result_column(result, str(date_type_list[5])+" ML_Prediction", "", "string")
add_result_column(result, str(date_type_list[5])+" Prediction", "", "string")
add_result_column(result, str(date_type_list[5])+" Previous", "", "string")
add_result_column(result, str(date_type_list[6])+" ML_Prediction", "", "string")
add_result_column(result, str(date_type_list[6])+" Prediction", "", "string")
add_result_column(result, str(date_type_list[6])+" Previous", "", "string")
