import ProSivicDDS as psvdds
import ProSiVIC_TCP as psctcp
import os

tcp = psctcp.ProSiVIC_TCP("127.0.0.1", 4444)
tcp._connect()
tcp._cmd("new sivicTime time")
tcp._synchro()

#  set  DDS configuration file location

carOrderH = psvdds.carOrderHandler("Vehicle/car")
carEnvH = psvdds.carEnvironmentHandler("Vehicle/car")
radarreceiver = psvdds.radarHandler("radar_1/radar")
eventH = psvdds.eventHandler("event")

tcp._play()

# wait to receive first sample
order = carOrderH.receive()
while order.timestamp == 0:
    order = carOrderH.receive()
order.movementOrderMode = psvdds.emovementOrder.speed
order.speedOrder = 40
carOrderH.transmit(order)

env = carEnvH.receive()
targets = radarreceiver.receive()
event = eventH.receive()
# loop until speed is 10m/s is reached

while True:
    if env.speed[0] <= 10:
        env = carEnvH.receive()
        order.movementOrderMode = psvdds.emovementOrder.speed
        order.speedOrder = 40
        carOrderH.transmit(order)
    else:
        env = carEnvH.receive()
        targets = radarreceiver.receive()
        if targets.nbTargetDetected == 1.0:
            if targets.data[0].distance < 15.0:
                # stop the car
                order.speedOrder = 0
                carOrderH.transmit(order)
                # execute event
                event.DDSvalue = 3.1
                eventH.transmit(event)
                break

os.system("pause")
