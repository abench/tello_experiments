from djitellopy import Tello

tello = Tello()

tello.connect()
#print("Battery:",tello.get_battery())
tello.takeoff()

tello.move("forward",300)

tello.land()
tello.end()
