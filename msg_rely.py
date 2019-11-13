import EV3BT
import time
import serial

EV3 = serial.Serial(port='/dev/rfcomm0', baudrate=9600, timeout=None)
print (EV3.name)
print (EV3.is_open)
counter = 1
try:
    while (1):
        if counter == 1:
            send = EV3BT.encodeMessage(EV3BT.MessageType.Numeric,'hello',1)
            counter += 1
        else:
            send = EV3BT.encodeMessage(EV3BT.MessageType.Numeric,'hello not',99)
            counter -= 1
        EV3.write(send)
        n = 0
        while (n==0):
            n=EV3.inWaiting()
        s = EV3.read(n)
        mail,values,s = EV3BT.decodeMessage(s,EV3BT.MessageType.Text)
        print (mail,values)
        time.sleep(1)

except KeyboardInterrupt:
    pass
    EV3.close()
EV3.close()
