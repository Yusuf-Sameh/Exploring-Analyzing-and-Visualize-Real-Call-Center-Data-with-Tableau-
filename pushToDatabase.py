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