import EV3BT
import serial
import time
from bluepy import sensortag as sensortag

# Since we could not find our sensor tag
# after running bluetooth scans, we don't have
# its' MAC address. The code below requires a an actual MAC address
sensor_tag_mac = 'OUR_SENSOR_TAG_MAC_ADDRESS'
sensor_tag = sensortag.SensorTag(sensor_tag_mac)

# Function that reads light data from the sensortag
def getLightData():
    sensor_tag.lightmeter.enable()
    lightData = sensor_tag.lightmeter.read();
    return lightData

EV3 = serial.Serial(port='/dev/rfcomm0',baudrate=9600,timeout=None)

print (EV3.name)
print (EV3.is_open)

try:
    while (1):
        lightData = getLightData()
        print (lightData)
        send = EV3BT.encodeMessage(EV3BT.MessageType.Numeric,'1231413',lightData)
        EV3.write(send)
        n = 0
        while (n==0):
            n=EV3.inWaiting()
        s = EV3.read(n)
        mail,values,s = EV3BT.decodeMessage(s,EV3BT.MessageType.Text)
        print (values)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass
    EV3.close()
EV3.close()