import time
from database import *
from datetime import datetime
from dateutil.tz import *

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
curr = datetime.now()
print(curr)

temp = input('Type what you want to send, hit enter:\r\n')

veh1 = scan_details(temp, 1, current_time)
veh1.add()
veh_d = vehicle_details(None, None, None, None, None, None)

if(veh_d.get_class_by_rfid(temp) == 'Heavy'):
    hr_chk = t.tm_hour
    #offence_type = "heavy_duty"
    if(hr_chk<6) or (hr_chk>22):
        o1 = offences(temp,current_time,"heavy_duty")#offence_type)
        o1.add()
#    else:
#        print("Correct time for heavy duty")



traffic_signal = None

def signal_listener(event):
    global traffic_signal
    traffic_signal = event.data

signal = db.reference('/Traffic_light').get()
#l = signal.listen(signal_listener)
#l.close()

if(signal == 'red'):
    o2 = offences(temp,current_time,"signal_violation")#offence_type)
    o2.add()



'''
while 1:
    #init_serial()
    temp = input('Type what you want to send, hit enter:\r\n')
    database.add(temp)
    tmp = input('Type ID to be retreived :\n')
    #print(type(tmp))
    database.get_by_rfid(tmp)
    #ser.write(temp)         #Writes to the SerialPort
    #print(temp)
'''
