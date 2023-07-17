#Exploring, Analyzing and Visualize Real Call Center Data with Tableau: Trends, Patterns, Metrics and Predictive Analytics
About

#YOU CAN FIND THIS PROJECT DEPLOYED HERE
#https://tableau-cc.onrender.com/


By: Youssef Sameh
In: April 2023
contact: youssefpasha49@gmail.com

Project Description
The aim of this project is to transform real call center system data for an Egyptian company, from unorganized data to a dashboard that contains the visualizations to display insights. Additionally, the project aims to measure some KPIs and display patterns to assist managers and decision-makers in making informed decisions.

To achieve the final product in its first version, several techniques were used. The process started by creating a tool using Python to read the data file from the local server and send it to a database (Google Sheets in the first version, and then SQL in the next version). This was followed by data cleaning operations and exporting the data to Tableau to build the dashboard for insights.

Although the dashboard is closer to an operational dashboard, it was primarily designed based on the requirements of decision-makers. The project presented here is a mini version, and the statistics and names have been changed for data security reasons. The displayed version is for analyzing data during the year 2022 only.

Dataset Description
The provided data is a small sample of a larger dataset consisting of Thousands of rows of call center data.

Each row represents a single call made to the call center and contains 29 columns of data after cleaning proccess. The columns include:

historyid: a unique identifier for each call
cllid: a unique identifier for each caller
duration: the length of the call in hours, minutes, and seconds
time-start: the date and time the call started
time-end: the date and time the call ended
hour: the hour of the day the call was made
day: the day of the week the call was made
month: the month the call was made
year: the year the call was made
reason-terminated: the reason the call was terminated (by the caller or by the call center)
from-no: the phone number the call originated from (if applicable)
to-no: the phone number the call was directed to (if applicable)
from-dn: the direct number the call originated from (if applicable)
to-dn: the direct number the call was directed to (if applicable)
dial-no: the phone number dialed (if applicable)
reason-changed: the reason for any changes made during the call (e.g. transferred to another agent)
final-number: the final phone number the call was directed to (if applicable)
final-dn: the final direct number the call was directed to (if applicable)
chain: a record of any changes made during the call (e.g. transferred between agents)
from-type: the type of number the call originated from (line, extension, queue, etc.)
to-type: the type of number the call was directed to (line, extension, queue, etc.)
final-type: the final type of number the call was directed to (line, extension, queue, etc.)
from-dispname: the display name associated with the number the call originated from (if applicable)
to-dispname: the display name associated with the number the call was directed to (if applicable)
final-dispname: the final display name associated with the number the call was directed to (if applicable)
missed-queue-calls: the number of calls missed while in the queue (if applicable)
ext-queue-name: the name of the extension or queue the call was directed to (if applicable)
status-queue: the status of the call while in the queue (if applicable)
call-type: the type of call (inbound or outbound)
This data can be used to analyze call center performance, including metrics such as call volume, call duration, and wait times. It can also be used to identify trends in customer behavior and preferences, as well as areas for improvement in call center operations.
