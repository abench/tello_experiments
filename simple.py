from djitellopy import Tello

tello = Tello()

tello.connect()
print("Battery:",tello.get_battery())
tello.takeoff()

tello.move_left(100)
tello.rotate_clockwise(90)
tello.move_forward(100)

tello.land()
