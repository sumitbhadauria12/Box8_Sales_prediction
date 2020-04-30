from datetime import datetime,timedelta
import email
global get_recipients_list
    
today_date = datetime.now().date()
today_day = datetime.now().strftime('%A')
print today_date
print today_day

################################################################## Next 7 days Dataframe [X_pred]
date_list = []
date_type_list = []
for i in range(0,7):
    date_list.append((datetime.today() + timedelta(days=i)).strftime('%Y-%m-%d'))
    date_type_list.append((datetime.today() + timedelta(days=i)).strftime('%A'))
print date_list,date_type_list
date_type = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}


data = execute_query("Python",5035)['rows']

negative_outlets = []
for row in data:
    final_row = {}
    # print (row['outlet'], row['Friday Final Prediction'], row['Friday Override'])
    # print row['Friday Final Prediction'][row['Friday Final Prediction'].find('>')+1:row['Friday Final Prediction'].find('</')]
    final_row['outlet'] = str(row['outlet'])
    final_row[str(date_list[0])] = str(row[str(date_type_list[0]) + " Final Prediction"][row[str(date_type_list[0]) + " Final Prediction"].find('>')+1:row[str(date_type_list[0]) + " Final Prediction"].find('</')]) if str(row[str(date_type_list[0]) + " Override"][row[str(date_type_list[0]) + " Override"].find('>')+1:row[str(date_type_list[0]) + " Override"].find('</')]) == 'NA' else str(row[str(date_type_list[0]) + " Override"][row[str(date_type_list[0]) + " Override"].find('>')+1:row[str(date_type_list[0]) + " Override"].find('</')])
    final_row[str(date_list[1])] = str(row[str(date_type_list[1]) + " Final Prediction"][row[str(date_type_list[1]) + " Final Prediction"].find('>')+1:row[str(date_type_list[1]) + " Final Prediction"].find('</')]) if str(row[str(date_type_list[1]) + " Override"][row[str(date_type_list[1]) + " Override"].find('>')+1:row[str(date_type_list[1]) + " Override"].find('</')]) == 'NA' else str(row[str(date_type_list[1]) + " Override"][row[str(date_type_list[1]) + " Override"].find('>')+1:row[str(date_type_list[1]) + " Override"].find('</')])
    final_row[str(date_list[2])] = str(row[str(date_type_list[2]) + " Final Prediction"][row[str(date_type_list[2]) + " Final Prediction"].find('>')+1:row[str(date_type_list[2]) + " Final Prediction"].find('</')]) if str(row[str(date_type_list[2]) + " Override"][row[str(date_type_list[2]) + " Override"].find('>')+1:row[str(date_type_list[2]) + " Override"].find('</')]) == 'NA' else str(row[str(date_type_list[2]) + " Override"][row[str(date_type_list[2]) + " Override"].find('>')+1:row[str(date_type_list[2]) + " Override"].find('</')])
    final_row[str(date_list[3])] = str(row[str(date_type_list[3]) + " Final Prediction"][row[str(date_type_list[3]) + " Final Prediction"].find('>')+1:row[str(date_type_list[3]) + " Final Prediction"].find('</')]) if str(row[str(date_type_list[3]) + " Override"][row[str(date_type_list[3]) + " Override"].find('>')+1:row[str(date_type_list[3]) + " Override"].find('</')]) == 'NA' else str(row[str(date_type_list[3]) + " Override"][row[str(date_type_list[3]) + " Override"].find('>')+1:row[str(date_type_list[3]) + " Override"].find('</')])
    final_row[str(date_list[4])] = str(row[str(date_type_list[4]) + " Final Prediction"][row[str(date_type_list[4]) + " Final Prediction"].find('>')+1:row[str(date_type_list[4]) + " Final Prediction"].find('</')]) if str(row[str(date_type_list[4]) + " Override"][row[str(date_type_list[4]) + " Override"].find('>')+1:row[str(date_type_list[4]) + " Override"].find('</')]) == 'NA' else str(row[str(date_type_list[4]) + " Override"][row[str(date_type_list[4]) + " Override"].find('>')+1:row[str(date_type_list[4]) + " Override"].find('</')])
    final_row[str(date_list[5])] = str(row[str(date_type_list[5]) + " Final Prediction"][row[str(date_type_list[5]) + " Final Prediction"].find('>')+1:row[str(date_type_list[5]) + " Final Prediction"].find('</')]) if str(row[str(date_type_list[5]) + " Override"][row[str(date_type_list[5]) + " Override"].find('>')+1:row[str(date_type_list[5]) + " Override"].find('</')]) == 'NA' else str(row[str(date_type_list[5]) + " Override"][row[str(date_type_list[5]) + " Override"].find('>')+1:row[str(date_type_list[5]) + " Override"].find('</')])
    final_row[str(date_list[6])] = str(row[str(date_type_list[6]) + " Final Prediction"][row[str(date_type_list[6]) + " Final Prediction"].find('>')+1:row[str(date_type_list[6]) + " Final Prediction"].find('</')]) if str(row[str(date_type_list[6]) + " Override"][row[str(date_type_list[6]) + " Override"].find('>')+1:row[str(date_type_list[6]) + " Override"].find('</')]) == 'NA' else str(row[str(date_type_list[6]) + " Override"][row[str(date_type_list[6]) + " Override"].find('>')+1:row[str(date_type_list[6]) + " Override"].find('</')])
    if float(final_row[str(date_list[0])]) < 0 or float(final_row[str(date_list[1])]) < 0 or float(final_row[str(date_list[2])]) < 0 or float(final_row[str(date_list[3])]) < 0 or float(final_row[str(date_list[4])]) < 0 or float(final_row[str(date_list[5])]) < 0 or float(final_row[str(date_list[6])]) < 0:
        negative_outlets.append(final_row)
    add_result_row(result, final_row)
    # break

add_result_column(result, "outlet", "", "string")
add_result_column(result, str(date_list[0]), "", "string")
add_result_column(result, str(date_list[1]), "", "string")
add_result_column(result, str(date_list[2]), "", "string")
add_result_column(result, str(date_list[3]), "", "string")
add_result_column(result, str(date_list[4]), "", "string")
add_result_column(result, str(date_list[5]), "", "string")
add_result_column(result, str(date_list[6]), "", "string")

def build_html_from_query_result(query_result, column_name_sequence):
    header_html = ''
    content_html = ''
    for  header in column_name_sequence:
        header_html = header_html + "<th align = 'center'>"+ header.upper() +"</th>"
    for index in range(0,len(query_result)):
        row_content = ''
        for key in column_name_sequence:
            row_content = row_content + "<td align = 'center'>"+ str(query_result[index][key])+"</td>"
        content_html = content_html + "<tr>" + row_content + "</tr>"
    final_html = """<html><head><style>table{font-family: arial, sans-serif;border-collapse: collapse;border: 1px solid #000000;width: 100%;}td{border: 1px solid #000000;text-align: centre;padding: 2px;}th {border: 1px solid #000000;text-align: centre;padding: 8px;color: #000000;}tr:nth-child(even){background-color: #dddddd;}</style></head><body><table border = '1'><tr>"""+header_html+"""</tr>"""+ content_html+"""</table></body></html>"""
    return final_html


def get_recipients_list(recipients_list):
    if not isinstance(recipients_list, basestring):
        recipients_list = ','.join(recipients_list)
    return recipients_list


def create_mime_message(email, sender, to, subject, text_body, html_body, bcc=None):
    msg = email.mime.multipart.MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = get_recipients_list(to)
    if bcc:
        msg['Bcc'] = get_recipients_list(bcc)
    text_part = email.mime.text.MIMEText(text_body, 'plain')
    html_part = email.mime.text.MIMEText(html_body, 'html')
    msg.attach(text_part)
    msg.attach(html_part)
    return msg


column_name = ['outlet'] + date_list
final_result = negative_outlets

html_body = build_html_from_query_result(final_result, column_name)
text_body = 'Please add these outlets to OverRide in Input for Sales Prediction Sheet '

if len(final_result) > 0:
    sender = 'Outlet Override<assets@box8letters.com>'
    to = ['sourav.roy@box8.in', 'vishal.chandra@box8.in','bimlesh@box8.in','akash.mishra@box8.in','kd@box8.in']
    bcc = []
    subject = 'Please add these outlets to OverRide [Box8-Own] / {0}'.format(str(datetime.now()).split(" ")[0])
    message = create_mime_message(email, sender, to, subject, text_body, html_body, bcc)
    # print "Message : " + str(message)
    send_mime_message(to,message)