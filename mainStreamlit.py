import streamlit as st


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


#*****************************************************************************************************************************************

# Define the list of sections in the app
sections = ['About', 'Project Description', 'Dataset Description', 'Steps']

# Define a function to create a table of contents
def create_toc(sections):
    st.sidebar.header('Table of Contents')
    
    st.sidebar.markdown(f"""
                            - 1. [{sections[0]}](#{sections[0].lower().replace(' ','-')}) 
                        """)
    st.sidebar.markdown(f"""
                            - 2. [{sections[1]}](#{sections[1].lower().replace(' ','-')}) 
                        """)
    st.sidebar.markdown(f"""
                            - 3. [{sections[2]}](#{sections[2].lower().replace(' ','-')}) 
                               - 3.1 [Dataset Sample](#dataset-sample)
                        """)
    st.sidebar.markdown(f"""
                            - 4. [{sections[3]}](#{sections[3].lower().replace(' ','-')}) 
                               - 4.1 [Push Data To Database](#push-data-to-database)
                               - 4.2 [Data Cleaning](#data-cleaning)
                               - 4.2 [Building Tableau Dashboard](#dashboard)
                        """)

# Create the table of contents in the sidebar
create_toc(sections)

#*****************************************************************************************************************************************

# Add the sections to the app
st.title("Exploring, Analyzing and Visualize Real Call Center Data with Tableau: Trends, Patterns, Metrics and Predictive Analytics")
st.divider()

st.header(sections[0])
st.write('By: Youssef Sameh\n\nIn: April 2023\n\ncontact: youssefpasha49@gmail.com')
st.divider()

st.header(sections[1])
st.write('The aim of this project is to transform real call center system data for an Egyptian company, from unorganized data to a dashboard that contains the visualizations to display insights. Additionally, the project aims to measure some KPIs and display patterns to assist managers and decision-makers in making informed decisions.')
st.write('To achieve the final product in its first version, several techniques were used. The process started by creating a tool using Python to read the data file from the local server and send it to a database (Google Sheets in the first version, and then SQL in the next version). This was followed by data cleaning operations and exporting the data to Tableau to build the dashboard for insights.')
st.write('Although the dashboard is closer to an operational dashboard, it was primarily designed based on the requirements of decision-makers. The project presented here is a mini version, and the statistics and names have been changed for data security reasons. The displayed version is for analyzing data during the year 2022 only.')
st.divider()

st.header(sections[2])
st.markdown("""
The provided data is a small sample of a larger dataset consisting of Thousands of rows of call center data.

Each row represents a single call made to the call center and contains 29 columns of data after cleaning proccess. The columns include:

- `historyid`: a unique identifier for each call
- `cllid`: a unique identifier for each caller
- `duration`: the length of the call in hours, minutes, and seconds
- `time-start`: the date and time the call started
- `time-end`: the date and time the call ended
- `hour`: the hour of the day the call was made
- `day`: the day of the week the call was made
- `month`: the month the call was made
- `year`: the year the call was made
- `reason-terminated`: the reason the call was terminated (by the caller or by the call center)
- `from-no`: the phone number the call originated from (if applicable)
- `to-no`: the phone number the call was directed to (if applicable)
- `from-dn`: the direct number the call originated from (if applicable)
- `to-dn`: the direct number the call was directed to (if applicable)
- `dial-no`: the phone number dialed (if applicable)
- `reason-changed`: the reason for any changes made during the call (e.g. transferred to another agent)
- `final-number`: the final phone number the call was directed to (if applicable)
- `final-dn`: the final direct number the call was directed to (if applicable)
- `chain`: a record of any changes made during the call (e.g. transferred between agents)
- `from-type`: the type of number the call originated from (line, extension, queue, etc.)
- `to-type`: the type of number the call was directed to (line, extension, queue, etc.)
- `final-type`: the final type of number the call was directed to (line, extension, queue, etc.)
- `from-dispname`: the display name associated with the number the call originated from (if applicable)
- `to-dispname`: the display name associated with the number the call was directed to (if applicable)
- `final-dispname`: the final display name associated with the number the call was directed to (if applicable)
- `missed-queue-calls`: the number of calls missed while in the queue (if applicable)
- `ext-queue-name`: the name of the extension or queue the call was directed to (if applicable)
- `status-queue`: the status of the call while in the queue (if applicable)
- `call-type`: the type of call (inbound or outbound)

This data can be used to analyze call center performance, including metrics such as call volume, call duration, and wait times. It can also be used to identify trends in customer behavior and preferences, as well as areas for improvement in call center operations.
""")

st.subheader('Dataset Sample')
import pandas as pd
data = {'historyid': ['Call 998343', 'Call 998549', 'Call 994490', 'Call 999231', 'Call 992692', 'Call 997793', 'Call 998894'],
        'cllid': ['00000C15E9F555D012_1', '00000C15EA1Ctt0548_7', '00000C15E33A1EAA26_8', '00000C15E22A1F7B78_10', '00000C15EA243202C87_12', '00000C15EA226B14_14', '00000C15EA3B1191_16'],
        'duration': ['00:00:21', '00:00:37', '00:00:21', '00:00:30', '00:00:42', '00:00:28', '00:00:14'],
        'time-start': ['02/02/2022 09:04', '02/02/2022 09:45', '02/02/2022 09:48', '02/02/2022 09:49', '02/02/2022 09:50', '02/02/2022 09:52', '02/02/2022 10:19'],
        'time-end': ['02/02/2022 09:04', '02/02/2022 09:46', '02/02/2022 09:49', '02/02/2022 09:50', '02/02/2022 09:51', '02/02/2022 09:53', '02/02/2022 10:20'],
        'hour': [9, 9, 9, 9, 9, 9, 10],
        'day': ['Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed'],
        'month': ['Feb', 'Feb', 'Feb', 'Feb', 'Feb', 'Feb', 'Feb'],
        'year': [2022, 2022, 2022, 2022, 2022, 2022, 2022],
        'reason-terminated': ['TerminatedBySrc', 'TerminatedBySrc', 'TerminatedByDst', 'TerminatedByDst', 'TerminatedByDst', 'TerminatedByDst', 'TerminatedBySrc'],
        'from-no': [0, 0, 0, 0, 0, 0, 0],
        'to-no': ['Ext.801', 'Ext.800', 'Ext.801', 'Ext.802', 'Ext.801', 'Ext.802', 'Ext.802'],
        'from-dn': [1005, 1006, 1003, 1006, 1002, 1005, 1002],
        'to-dn': [801, 802, 801, 804, 802, 804, 801],
        'dial-no': ['', '', '', '', '', '', ''],
        'reason-changed': ['Chain: 01091766760;Ext.8002;', 'Chain: 01000103296;Ext.8002;', 'Chain: 01000103296;Ext.8003;Ext.1002;', 'Chain: 01000103296;Ext.8002;Ext.1002;', 'Chain: 01000103296;Ext.8004;Ext.1010;', 'Chain: 01000103296;Ext.8007;Ext.1010;', 'Chain: 01000103296;Ext.8004;Ext.1010;'],
        'final-number': ['Line', 'Line', 'Extension', 'Extension', 'Extension', 'Extension', 'Extension'],
        'final-dn': ['Queue', 'Queue', 'Queue', 'Queue', 'Queue', 'Queue', 'Queue'],
        'chain': ['', '', '', '', '', '', ''],
       'from-type': ['private_name', 'private_name', 'private_name', 'private_name', 'private_name', 'private_name', 'private_name'],
        'to-type': ['Queue', 'Queue', 'Queue', 'Queue', 'Queue', 'Queue', 'Queue'],
        'final-type': ['private_name', 'private_name', 'private_name', 'private_name', 'private_name', 'private_name', 'private_name'],
        'from-dispname': ['Instagram', 'Facebook', 'Facebook', 'Instagram', 'Tiktok', 'Tiktok', 'Instagram'],
        'to-dispname': ['', '', '', '', '', '', ''],
        'final-dispname': ['Malek', 'Unanswered', 'Fatima', 'Malek', 'Farida', 'Farida', 'Malek'],
        'missed-queue-calls': ['1010;', '1010;', '1010;', '1010;', '1002;', '1002;', '1002;'],
        'ext-queue-name': ['', '', '', '', '', '', ''],
        'status-queue': ['Unanswered', 'Unanswered', 'Answered', 'Answered', 'Answered', 'Answered', 'Answered'],
        'call-type': ['Inbound', 'Inbound', 'Inbound', 'Inbound', 'Inbound', 'Inbound', 'Inbound']
        }

df = pd.DataFrame(data)
df
st.divider()

st.header(sections[3])
st.write('This data is automatically generated from the company call center system and stored on the local server in a log file. There is no way to send it to a database or store it elsewhere. Therefore, I built a tool using Python to run as an executable file (exe). Its function is to access the file path, read it, add some other data such as column names, connect to a database, and send it to the database. This file is automatically executed at a predetermined interval to resend the new data.')
st.write('When reading the file, it reads the data that was previously sent alongside the new data to be sent. Therefore, it must be ensured each time that the data that was previously sent is ignored by reading the data from the database and comparing it with the new file.')

st.subheader('Push Data To Database')
st.write('This is part of the code used.')
st.code("""
        import pandas as pd
        import numpy as np
        import datetime
        import pytz
        import mysql.connector

        #.................................................................................................................

        cdr = pd.read_csv('cdr.log', sep=',', header=None, names=['historyid', 'callid', 'duration', 'time-start', 'time-answered',
            'time-end', 'reason-terminated', 'from-no', 'to-no', 'from-dn', 'to-dn',
            'dial-no', 'reason-changed', 'final-number', 'final-dn', 'bill-code',
            'bill-rate', 'bill-cost', 'bill-name', 'chain', 'from-type', 'to-type',
            'final-type', 'from-dispname', 'to-dispname', 'final-dispname',
            'missed-queue-calls'])

        #.................................................................................................................
        def clean_cdr():
            cdr.drop(['bill-code', 'bill-rate', 'bill-cost', 'bill-name'],inplace=True, axis=1)

            cdr['duration'].fillna('00:00:00', inplace=True)
            cdr['time-answered'].fillna(cdr['time-start'], inplace=True)
            cdr.fillna("NaN", inplace=True)
            cdr['ext-queue-name'] = cdr['final-dn'].astype(str)+' '+cdr['final-dispname']

            indexQueue = cdr[cdr['to-type']!='Queue'].index
            cdr.drop(index=indexQueue, inplace=True)
            cdr.reset_index(inplace=True, drop=True)

            cdr['queue-status'] = np.where(cdr['final-dispname'].isnull(), 'Unanswered', 'Answered')
            
        #.................................................................................................................

        def convert_datetime_timezone(dt, tz_old, tz_new):
            tz_old = pytz.timezone(tz_old)
            tz_new = pytz.timezone(tz_new)
            dt = datetime.datetime.strptime(dt,"%Y/%m/%d %H:%M:%S")
            dt = tz_old.localize(dt)
            dt = dt.astimezone(tz_new)
            dt = dt.strftime("%Y-%m-%d %H:%M:%S")
            return dt

        def convert_now():
            try:
                for i in range(cdr.shape[0]):
                    cdr['time-start'][i] = convert_datetime_timezone(cdr['time-start'][i],'UTC','Africa/Cairo')
                    cdr['time-end'][i] = convert_datetime_timezone(cdr['time-end'][i],'UTC','Africa/Cairo')
                    cdr['time-answered'][i] = convert_datetime_timezone(cdr['time-answered'][i],'UTC','Africa/Cairo')
            except:
                pass

        #..................................................................................................................

        def add_date():
            cdr['year'] = [datetime.datetime.strptime(val,"%Y-%m-%d %H:%M:%S").year for val in cdr['time-start']]
            cdr['month'] = [datetime.datetime.strptime(val,"%Y-%m-%d %H:%M:%S").month for val in cdr['time-start']]
            cdr['day'] = [datetime.datetime.strptime(val,"%Y-%m-%d %H:%M:%S").day for val in cdr['time-start']]
            cdr['hour'] = [datetime.datetime.strptime(val,"%Y-%m-%d %H:%M:%S").hour for val in cdr['time-start']]
        #.................................................................................................................
        def connect_db():
            global connector
            connector = mysql.connector.connect(host='localhost',
                                            user='root',
                                            passwd='',
                                            database='cdr_db')
            global cursor
            cursor = connector.cursor()

        #..................................................................................................................

        def return_last_callid():
            sql = "SELECT * FROM `cdr`"
            cursor.execute(sql)
            return cursor.fetchall()[-1][1]

        #..................................................................................................................

        def insert_data(cdr_new):
            cols = "`,`".join([str(i) for i in cdr.columns.tolist()])
            for i,row in cdr_new.iterrows():
                sql = "INSERT INTO `cdr` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
                cursor.execute(sql, tuple(row))
            connector.commit()
            
            
        def cdr_to_insert(callid):    
            return cdr[cdr['callid'] > callid]

        #.................................................................................................................

        def get_db_status():
            cdr_table_exist = False
            cdr_table_empty = False
            cdr_status = ''

            sql = "SHOW TABLES"
            cursor.execute(sql)
            if ('cdr',) in cursor.fetchall():
                cdr_table_exist = True
                
            if cdr_table_exist:
                sql = "SELECT * FROM `cdr`"
                cursor.execute(sql)
                if len(cursor.fetchall()) == 0:
                    cdr_table_empty = True
                    
            if cdr_table_exist == False:
                cdr_status = 'table_not_exist'
            elif cdr_table_empty:
                cdr_status = 'table_exist_empty'
            else:
                cdr_status = 'table_exist_data'
            
            return cdr_status

        #.................................................................................................................

        #.................................................................................................................
        #.................................................................................................................
        #.................................................................................................................

        clean_cdr()
        convert_now()
        add_date()
        connect_db()

        if get_db_status()=='table_not_exist':
            sql = "CREATE TABLE `cdr_db`.`cdr` (`historyid` TEXT NOT NULL , `callid` TEXT NOT NULL , `duration` TIME NOT NULL , `time-start` DATETIME NOT NULL , `time-answered` DATETIME NOT NULL , `time-end` DATETIME NOT NULL , `reason-terminated` TEXT NOT NULL , `from-no` TEXT NOT NULL , `to-no` TEXT NOT NULL , `from-dn` TEXT NOT NULL , `to-dn` TEXT NOT NULL , `dial-no` TEXT NOT NULL , `reason-changed` TEXT NOT NULL , `final-number` TEXT NOT NULL , `final-dn` TEXT NOT NULL , `chain` TEXT NOT NULL , `from-type` TEXT NOT NULL , `to-type` TEXT NOT NULL , `final-type` TEXT NOT NULL , `from-dispname` TEXT NOT NULL , `to-dispname` TEXT NOT NULL , `final-dispname` TEXT NOT NULL , `missed-queue-calls` TEXT NOT NULL , `ext-queue-name` TEXT NOT NULL , `queue-status` TEXT NOT NULL , `year` YEAR NOT NULL , `month` TEXT NOT NULL , `day` TEXT NOT NULL , `hour` TEXT NOT NULL , INDEX `callid` (`callid`)) ENGINE = InnoDB;"
            cursor.execute(sql)
            insert_data(cdr)
        elif get_db_status()=='table_exist_empty':
            #verify cols and insert data
            pass
        else:
            cdr_new = cdr_to_insert(return_last_callid())
            insert_data(cdr_new)

        """,language='python')

st.subheader('Data Cleaning',anchor='data-cleaning')
st.write('It was displayed in the previous code.')
st.write('However, some additional cleaning was performed that was not present in the code, such as removing some columns, correcting incorrect values, and deleting rows based on specific criteria.')


st.subheader('Building Tableau Dashboard', anchor='dashboard')
st.write('The below dashboard is built using Tableau Public')

#import looker_sdk
#html = f'<iframe width="1600" height="2200" src="" frameborder="0" style="border:0" allowfullscreen></iframe>'
#st.markdown(html, unsafe_allow_html=True)

video_file = open('vedio.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.divider()










