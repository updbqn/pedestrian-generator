import ProSivicDDS as psvdds
import ProSiVIC_TCP as psctcp
import os

tcp = psctcp.ProSiVIC_TCP("127.0.0.1", 4444)
tcp._connect()
tcp._cmd("new sivicTime time")
tcp._synchro()


# set  DDS configuration file location
carOrderH = psvdds.carOrderHandler("audi/car")
carEnvH = psvdds.carEnvironmentHandler("audi/car")

tcp._play()

# receive last sample emitting by prosivic
order = carOrderH.receive()
order.throttle = 1
carOrderH.transmit(order)

env = carEnvH.receive()
# loop until speed is 10m/s is reached
while env.speed[0] <= 10.0:
    env = carEnvH.receive()
    order = carOrderH.receive()
    order.throttle = 1
    carOrderH.transmit(order)
# set the car to speed control and set speed to 10km/h
order.movementOrderMode = psvdds.emovementOrder.speed
order.speedOrder = 10

# send order to prosivic
carOrderH.transmit(order)

# store timestamp
timestamp = order.timestamp

# loop for 8 simulated second
timeend = timestamp + 8000000
while timestamp <= timeend:
    order = carOrderH.receive()
    timestamp = order.timestamp

# stop the car , back in manual control
order.movementOrderMode = psvdds.emovementOrder.pedals
order.brake = 1

# send order to prosivic
carOrderH.transmit(order)

tcp._stop()
# pause program
os.system("pause")
