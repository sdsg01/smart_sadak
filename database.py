import time, datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('serviceKey.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-db-7be24.firebaseio.com'
})
ref = db.reference('/')

class offences:
    def __init__(self, rfid_ID, timestamp, offence_type):
        self.rfid_ID = rfid_ID
        self.timestamp = timestamp
        self.offence_type = offence_type

    def add(self):
        ref1 = ref.child('Offences')
        ref1.push({
                'rfid_ID': self.rfid_ID,
                'timestamp': self.timestamp,
                'offence_type': self.offence_type
            })

    def get_by_rfid(self, rfid_ID):
        ref1 = fa.db.reference('Offences')
        result = ref1.order_by_child('rfid_ID').equal_to(rfid_ID).limit_to_first(1).get()
        for key, value in result.items():
            #print('{0}:{1} '.format(key, value))
            for x, y in value.items():
                print('{0}:{1} '.format(x, y))

"""
ref.set({
    'Details':
        {
            'rfid':'null',
            'name_plate':'null',
            'driver_no':'null',
            'car_type':'null',
        }
})
"""

class scan_details:
    def __init__(self, rfid_ID, scanner_id, timestamp):
        self.rfid_ID = rfid_ID
        self.scanner_id = scanner_id
        self.timestamp = timestamp

    def add(self):
        ref1 = ref.child('Scan_Details_' + str(self.scanner_id))
        ref1.push({
                'rfid': self.rfid_ID,
                'time': self.timestamp,
                #'scanner_id': self.scanner_id
            })
        ref_log = ref.child('Scan_Details_log')
        ref_log.push({
                'rfid': self.rfid_ID,
                'time': self.timestamp,
                'scanner_id': self.scanner_id
            })

    def get_by_rfid(self, rfid_ID):
        ref1 = db.reference('Scan_Details_log')
        try:
            result = ref1.order_by_child('rfid').equal_to(rfid_ID).limit_to_first(5).get()
            for key, value in result.items():
                for x, y in value.items():
                    #print(value.items())
                    print('{0}:{1} '.format(x, y))
        except:
            print("Exception occured. No entry of given ID in db\n")


class vehicle_details:
    def __init__(self):
        self.rfid_ID = None

    def __init__(self, rfid_ID, vehicle_class, number_plate, owner_name, owner_contact, prev_offences):
        self.rfid_ID = rfid_ID
        self.vehicle_class = vehicle_class
        self.number_plate = number_plate
        self.owner_name = owner_name
        self.owner_contact = owner_contact
        self.prev_offences = prev_offences

    def add(self):
        ref1 = ref.child('Vehicle_details')
        ref1.push({
                'rfid_ID': self.rfid_ID,
                'vehicle_class': self.vehicle_class,
                'number_plate': self.number_plate,
                'owner_name' : self.owner_name,
                'owner_contact' : self.owner_contact,
                'prev_offences' : self.prev_offences
            })


    def get_by_rfid(self, rfid_ID):
        ref1 = db.reference('Vehicle_details')
        result = ref1.order_by_child('rfid_ID').equal_to(rfid_ID).limit_to_first(10).get()
        for key, value in result.items():
            #print(value['timestamp'])
            for x, y in value.items():
                print('{0}:{1} '.format(x, y))

    def get_class_by_rfid(self, rfid_ID):
        ref1 = db.reference('Vehicle_details')
        result = ref1.order_by_child('rfid_ID').equal_to(rfid_ID).limit_to_first(1).get()
        for key, value in result.items():
            return value['vehicle_class']


def get_latest_time(rfid_ID, scanner_ID):
    ref1 = ref.child('Scan_Details_' + str(scanner_ID))
    q = ref1.order_by_child('rfid').equal_to(rfid_ID).limit_to_last(1).get()
    for key, val in q.items():
        return val['time']

def get_speed(rfid_ID, start, end, distance):
        timestamp1 = get_latest_time(rfid_ID, start)
        timestamp2 = get_latest_time(rfid_ID, end)
        a1 = time.strptime(timestamp1, "%H:%M:%S")
        a2 = time.strptime(timestamp2, "%H:%M:%S")
        sec1=datetime.timedelta(hours=a1.tm_hour, minutes=a1.tm_min, seconds=a1.tm_sec).seconds
        sec2=datetime.timedelta(hours=a2.tm_hour, minutes=a2.tm_min, seconds=a2.tm_sec).seconds
        duration = sec2 - sec1
        return distance / duration



def remove(rfid_ID, scanner_ID):
    ref1 = ref.child('Scan_Details_' + str(scanner_ID))
    result = ref1.order_by_child('rfid').equal_to(rfid_ID).limit_to_last(1).get()
    for i in result.keys():
        ref1.child(i).delete()


'''
def add(temp):
    #import tagScan
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    #hour = time.strftime("%H", t)
    hr_chk = t.tm_hour
    offence_type = "heavy_duty" #offence check function
    if(hr_chk<6) or (hr_chk>22):
        print("blah")
        o = offences(temp,current_time,offence_type)
        o.add()
    else:
        print("Correct time for heavy duty")

    #current_date = datetime.datetime("%x")
    ref1 = ref.child('Scan_Details')
    ref1.push({
            'rfid': temp,
            #'time': {'.sv': 'timestamp'},
            'time': current_time,
            'scanner_id': 1
            #'date': current_date,
        })

def get_by_rfid(temp):
    ref1 = db.reference('Scan_Details')
    try:
        result = ref1.order_by_child('rfid').equal_to(temp).limit_to_first(10).get()
        for key, value in result.items():
            for x, y in value.items():
                #print(value.items())
                print('{0}:{1} '.format(x, y))
    except:
        print("Exception occured.No entry of given ID in db\n")
'''

"""
def add():
    import scan_code
    ref1 = ref.child('Details')
    ref1.push({
            'rfid': scan_code.temp,
            'name_plate': 'xyz',
            'driver_no': 12345,
            'car_type': 'Heavy_Weight'
        })

"""
