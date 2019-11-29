import time
from database import *
from datetime import datetime
#from dateutil.tz import *
import requests
global SIGNAL_FLAG
#from twilio.rest import Client

#client = Client("AC9013a67233fa74a0a2630e3b8794f339", "7619f91e69f61219a386290e65478239")

url = "https://www.fast2sms.com/dev/bulk"



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
            payload = "sender_id=FSTSMS&message=Dear Citizen, Overspeeding detected! &language=english&route=p&numbers=9145499132"
            headers = {
                'authorization': "NQSGHVbJK6rMqIv2kWXEhLwncC50PU3zxsajO9ul8ofpyZA7BiG1j6Nc8DbUmd4J0MwvSWQZs3YeuOhA",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            # client.messages.create(to="+919767034552",
            #                      from_="+12512203113",
            #                     body="Dear citizen, your vehicle has been detected overspeeding!!")
    except:
        #Wrong Way offence
        o_ww = offences(temp, current_time, 'wrong_way')
        o_ww.add()
        payload = "sender_id=FSTSMS&message=Dear Citizen, Wrong way rule violation! &language=english&route=p&numbers=9145499132"
        headers = {
            'authorization': "NQSGHVbJK6rMqIv2kWXEhLwncC50PU3zxsajO9ul8ofpyZA7BiG1j6Nc8DbUmd4J0MwvSWQZs3YeuOhA",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        # client.messages.create(to="+919767034552",
        #                      from_="+12512203113",
        #                     body="Dear citizen, your vehicle has been detected in a wrong lane!!")
        SIGNAL_FLAG = False


    #Heavy vehicle offence
    if(veh_d.get_class_by_rfid(temp) == 'Heavy'):
        hr_chk = t.tm_hour
        #offence_type = "heavy_duty"
        if(hr_chk<6) or (hr_chk>15):
            o1 = offences(temp,current_time,'heavy_duty')
            o1.add()
            payload = "sender_id=FSTSMS&message=Dear Citizen, Heavy Vehicle detected! &language=english&route=p&numbers=9145499132"
            headers = {
                'authorization': "NQSGHVbJK6rMqIv2kWXEhLwncC50PU3zxsajO9ul8ofpyZA7BiG1j6Nc8DbUmd4J0MwvSWQZs3YeuOhA",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            #client.messages.create(to="+919767034552",
             #                      from_="+12512203113",
              #                     body="Dear citizen, your vehicle has been detected in a no heavy-vehicle zone!!")

    #Traffic signal offence
    if(SIGNAL_FLAG):
        signal = db.reference('/Traffic_light').get()
        if(signal == 'red'):
            o2 = offences(temp,current_time,"signal_violation")#offence_type)
            o2.add()
            payload = "sender_id=FSTSMS&message=Dear Citizen, Signal Violation! &language=english&route=p&numbers=9145499132"
            headers = {
                'authorization': "NQSGHVbJK6rMqIv2kWXEhLwncC50PU3zxsajO9ul8ofpyZA7BiG1j6Nc8DbUmd4J0MwvSWQZs3YeuOhA",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
            }
            response = requests.request("POST", url, data=payload, headers=headers)

        #show_message('signal_violation')
    #    client.messages.create(to="+919767034552",
    #                   from_="+12512203113",
    #                   body="Dear citizen, your vehicle has been detected in a traffic signal violation!!")
    if(SIGNAL_FLAG):
        remove(temp, 1)

    remove(temp, 2)

