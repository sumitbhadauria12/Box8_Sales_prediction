default_box8_own_buffer = 1.05 #5% buffer is added for all days

from datetime import datetime,timedelta

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
print date_list,date_type_list
date_type = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
data = get_query_result(5010)['rows']


################################################################## Special Day

google_sheet_id1 = '19q8g0n2UJ1BVH1MQTlDs6luqWUViKmfb0a8KM6mOmG4|2'
gs_table1 = execute_query("Box8-Google-Service-Account", google_sheet_id1)['rows']





google_sheet_id = '19q8g0n2UJ1BVH1MQTlDs6luqWUViKmfb0a8KM6mOmG4|0'
gs_table = execute_query("Box8-Google-Service-Account", google_sheet_id)['rows']

for each in data:
    final_row = {}
    for row in gs_table:
        if each['outlet'] == row['Box8_Outlet']:
            final_row['outlet'] = row['Box8_Outlet']
            final_row[str(date_type_list[0]) + " Prediction"] = each[str(date_type_list[0]) + " Prediction"]
            final_row["CF1_Box8_"+str(date_type_list[0])] = row["Box8_"+str(date_type_list[0])]
            cf1_0 = row["Box8_"+str(date_type_list[0])]
            
            final_row[str(date_type_list[1]) + " Prediction"] = each[str(date_type_list[1]) + " Prediction"]
            final_row["CF1_Box8_"+str(date_type_list[1])] = row["Box8_"+str(date_type_list[1])]
            cf1_1 = row["Box8_"+str(date_type_list[1])]
            
            final_row[str(date_type_list[2]) + " Prediction"] = each[str(date_type_list[2]) + " Prediction"]
            final_row["CF1_Box8_"+str(date_type_list[2])] = row["Box8_"+str(date_type_list[2])]
            cf1_2 = row["Box8_"+str(date_type_list[2])]
            
            final_row[str(date_type_list[3]) + " Prediction"] = each[str(date_type_list[3]) + " Prediction"]
            final_row["CF1_Box8_"+str(date_type_list[3])] = row["Box8_"+str(date_type_list[3])]
            cf1_3 = row["Box8_"+str(date_type_list[3])]
            
            final_row[str(date_type_list[4]) + " Prediction"] = each[str(date_type_list[4]) + " Prediction"]
            final_row["CF1_Box8_"+str(date_type_list[4])] = row["Box8_"+str(date_type_list[4])]
            cf1_4 = row["Box8_"+str(date_type_list[4])]
            
            final_row[str(date_type_list[5]) + " Prediction"] = each[str(date_type_list[5]) + " Prediction"]
            final_row["CF1_Box8_"+str(date_type_list[5])] = row["Box8_"+str(date_type_list[5])]
            cf1_5 = row["Box8_"+str(date_type_list[5])]
            
            final_row[str(date_type_list[6]) + " Prediction"] = each[str(date_type_list[6]) + " Prediction"]
            final_row["CF1_Box8_"+str(date_type_list[6])] = row["Box8_"+str(date_type_list[6])]
            cf1_6 = row["Box8_"+str(date_type_list[6])]
    final_row[str(date_type_list[0]) + " Override"] = "<div class='btn btn-danger container'>NA</div>"
    final_row[str(date_type_list[1]) + " Override"] = "<div class='btn btn-danger container'>NA</div>"
    final_row[str(date_type_list[2]) + " Override"] = "<div class='btn btn-danger container'>NA</div>"
    final_row[str(date_type_list[3]) + " Override"] = "<div class='btn btn-danger container'>NA</div>"
    final_row[str(date_type_list[4]) + " Override"] = "<div class='btn btn-danger container'>NA</div>"
    final_row[str(date_type_list[5]) + " Override"] = "<div class='btn btn-danger container'>NA</div>"
    final_row[str(date_type_list[6]) + " Override"] = "<div class='btn btn-danger container'>NA</div>"



    final_row["CF2_Box8_"+str(date_type_list[0])] = 1
    final_row["CF2_Box8_"+str(date_type_list[1])] = 1
    final_row["CF2_Box8_"+str(date_type_list[2])] = 1
    final_row["CF2_Box8_"+str(date_type_list[3])] = 1
    final_row["CF2_Box8_"+str(date_type_list[4])] = 1
    final_row["CF2_Box8_"+str(date_type_list[5])] = 1
    final_row["CF2_Box8_"+str(date_type_list[6])] = 1

    for row in gs_table1:
        if each['outlet'] == row['box8_own_override_outlet']:
            final_row[str(date_type_list[0]) + " Override"] = "<div class='btn btn-warning container'>{0}</div>".format(row["box8_own_override_" + str(date_type_list[0])])
            final_row[str(date_type_list[1]) + " Override"] = "<div class='btn btn-warning container'>{0}</div>".format(row["box8_own_override_" + str(date_type_list[1])])
            final_row[str(date_type_list[2]) + " Override"] = "<div class='btn btn-warning container'>{0}</div>".format(row["box8_own_override_" + str(date_type_list[2])])
            final_row[str(date_type_list[3]) + " Override"] = "<div class='btn btn-warning container'>{0}</div>".format(row["box8_own_override_" + str(date_type_list[3])])
            final_row[str(date_type_list[4]) + " Override"] = "<div class='btn btn-warning container'>{0}</div>".format(row["box8_own_override_" + str(date_type_list[4])])
            final_row[str(date_type_list[5]) + " Override"] = "<div class='btn btn-warning container'>{0}</div>".format(row["box8_own_override_" + str(date_type_list[5])])
            final_row[str(date_type_list[6]) + " Override"] = "<div class='btn btn-warning container'>{0}</div>".format(row["box8_own_override_" + str(date_type_list[6])])
        try:
            for i in range(0,len(date_list)):
                if datetime.strptime(str(row['special_date']), '%Y-%m-%dT%H:%M:%S').strftime('%d-%m-%y') == date_list[i]:
                    if date_type_list[i] == 'Monday' : final_row["CF2_Box8_Monday"] = row['sp_box8_own']
                    if date_type_list[i] == 'Tuesday' : final_row["CF2_Box8_Tuesday"] = row['sp_box8_own']
                    if date_type_list[i] == 'Wednesday' : final_row["CF2_Box8_Wednesday"] = row['sp_box8_own']
                    if date_type_list[i] == 'Thursday' : final_row["CF2_Box8_Thursday"] = row['sp_box8_own']
                    if date_type_list[i] == 'Friday' : final_row["CF2_Box8_Friday"] = row['sp_box8_own']
                    if date_type_list[i] == 'Saturday' : final_row["CF2_Box8_Saturday"] = row['sp_box8_own']
                    if date_type_list[i] == 'Sunday' : final_row["CF2_Box8_Sunday"] = row['sp_box8_own']
        except:
            pass
    final_row[str(date_type_list[0]) + " Final Prediction"] = "<div class='btn btn-success container'>{0}</div>".format("{:.2f}".format(cf1_0 * final_row["CF2_Box8_"+str(date_type_list[0])] * each[str(date_type_list[0]) + " Prediction"] * default_box8_own_buffer))
    final_row[str(date_type_list[1]) + " Final Prediction"] = "<div class='btn btn-success container'>{0}</div>".format("{:.2f}".format(cf1_1 * final_row["CF2_Box8_"+str(date_type_list[1])] * each[str(date_type_list[1]) + " Prediction"] * default_box8_own_buffer))
    final_row[str(date_type_list[2]) + " Final Prediction"] = "<div class='btn btn-success container'>{0}</div>".format("{:.2f}".format(cf1_2 * final_row["CF2_Box8_"+str(date_type_list[2])] * each[str(date_type_list[2]) + " Prediction"] * default_box8_own_buffer))
    final_row[str(date_type_list[3]) + " Final Prediction"] = "<div class='btn btn-success container'>{0}</div>".format("{:.2f}".format(cf1_3 * final_row["CF2_Box8_"+str(date_type_list[3])] * each[str(date_type_list[3]) + " Prediction"] * default_box8_own_buffer))
    final_row[str(date_type_list[4]) + " Final Prediction"] = "<div class='btn btn-success container'>{0}</div>".format("{:.2f}".format(cf1_4 * final_row["CF2_Box8_"+str(date_type_list[4])] * each[str(date_type_list[4]) + " Prediction"] * default_box8_own_buffer))
    final_row[str(date_type_list[5]) + " Final Prediction"] = "<div class='btn btn-success container'>{0}</div>".format("{:.2f}".format(cf1_5 * final_row["CF2_Box8_"+str(date_type_list[5])] * each[str(date_type_list[5]) + " Prediction"] * default_box8_own_buffer))
    final_row[str(date_type_list[6]) + " Final Prediction"] = "<div class='btn btn-success container'>{0}</div>".format("{:.2f}".format(cf1_6 * final_row["CF2_Box8_"+str(date_type_list[6])] * each[str(date_type_list[6]) + " Prediction"] * default_box8_own_buffer))
    

            
    # if each[str(date_type_list[0]) + " Prediction"] != 0:
    add_result_row(result, final_row)
    # break
add_result_column(result, "outlet", "", "string")
add_result_column(result, str(date_type_list[0]) + " Prediction", "", "string")
add_result_column(result, "CF1_Box8_"+str(date_type_list[0]), "", "string")
add_result_column(result, "CF2_Box8_"+str(date_type_list[0]), "", "string")
add_result_column(result, str(date_type_list[0]) + " Override", "", "string")
add_result_column(result, str(date_type_list[0]) + " Final Prediction", "", "string")

add_result_column(result, str(date_type_list[1]) + " Prediction", "", "string")
add_result_column(result, "CF1_Box8_"+str(date_type_list[1]), "", "string")
add_result_column(result, "CF2_Box8_"+str(date_type_list[1]), "", "string")
add_result_column(result, str(date_type_list[1]) + " Override", "", "string")
add_result_column(result, str(date_type_list[1]) + " Final Prediction", "", "string")

add_result_column(result, str(date_type_list[2]) + " Prediction", "", "string")
add_result_column(result, "CF1_Box8_"+str(date_type_list[2]), "", "string")
add_result_column(result, "CF2_Box8_"+str(date_type_list[2]), "", "string")
add_result_column(result, str(date_type_list[2]) + " Override", "", "string")
add_result_column(result, str(date_type_list[2]) + " Final Prediction", "", "string")

add_result_column(result, str(date_type_list[3]) + " Prediction", "", "string")
add_result_column(result, "CF1_Box8_"+str(date_type_list[3]), "", "string")
add_result_column(result, "CF2_Box8_"+str(date_type_list[3]), "", "string")
add_result_column(result, str(date_type_list[3]) + " Override", "", "string")
add_result_column(result, str(date_type_list[3]) + " Final Prediction", "", "string")

add_result_column(result, str(date_type_list[4]) + " Prediction", "", "string")
add_result_column(result, "CF1_Box8_"+str(date_type_list[4]), "", "string")
add_result_column(result, "CF2_Box8_"+str(date_type_list[4]), "", "string")
add_result_column(result, str(date_type_list[4]) + " Override", "", "string")
add_result_column(result, str(date_type_list[4]) + " Final Prediction", "", "string")

add_result_column(result, str(date_type_list[5]) + " Prediction", "", "string")
add_result_column(result, "CF1_Box8_"+str(date_type_list[5]), "", "string")
add_result_column(result, "CF2_Box8_"+str(date_type_list[5]), "", "string")
add_result_column(result, str(date_type_list[5]) + " Override", "", "string")
add_result_column(result, str(date_type_list[5]) + " Final Prediction", "", "string")

add_result_column(result, str(date_type_list[6]) + " Prediction", "", "string")
add_result_column(result, "CF1_Box8_"+str(date_type_list[6]), "", "string")
add_result_column(result, "CF2_Box8_"+str(date_type_list[6]), "", "string")
add_result_column(result, str(date_type_list[6]) + " Override", "", "string")
add_result_column(result, str(date_type_list[6]) + " Final Prediction", "", "string")
