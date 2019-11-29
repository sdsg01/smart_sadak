import time
from database import *
from datetime import datetime
#from dateutil.tz import *
global SIGNAL_FLAG

while True:
    SIGNAL_FLAG = True

    temp = input('Type what you want to send, hit enter:\r\n')
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    curr = datetime.now()

    veh = scan_details(temp, 2, current_time)
    veh.add()

    veh_d = vehicle_details(None, None, None, None, None, None)

    try:
        #Overspeeding offence
        speed = get_speed(temp, 1, 2, 100)
        print(speed)
        if(speed > 3):
            o_speed = offences(temp, current_time, 'overspeeding')
            o_speed.add()
    except:
        #Wrong Way offence
        o_ww = offences(temp, current_time, 'wrong_way')
        o_ww.add()
        SIGNAL_FLAG = False


    #Heavy vehicle offence
    if(veh_d.get_class_by_rfid(temp) == 'Heavy'):
        hr_chk = t.tm_hour
        #offence_type = "heavy_duty"
        if(hr_chk<6) or (hr_chk>15):
            o1 = offences(temp,current_time,'heavy_duty')
            o1.add()

    #Traffic signal offence
    if(SIGNAL_FLAG):
        signal = db.reference('/Traffic_light').get()
        if(signal == 'red'):
            o2 = offences(temp,current_time,"signal_violation")#offence_type)
            o2.add()
        #show_message('signal_violation')
    #    client.messages.create(to="+919767034552",
    #                   from_="+12512203113",
    #                   body="Dear citizen, your vehicle has been detected in a traffic signal violation!!")
    if(SIGNAL_FLAG):
        remove(temp, 1)

    remove(temp, 2)
