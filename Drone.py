from pickle import FALSE
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
from pymavlink import mavutil

drone = connect('127.0.0.1:14550', wait_ready=True)

print("Drone kalkabilme durumu: ", drone.is_armable)
print(f'Drone kalkma durumu: {drone.armed}')

print(f'{drone.location.global_frame}')
print(f'{drone.location.global_relative_frame}')

print(f' İrtifa durumu: {drone.location.global_relative_frame.alt}')


def takeoff(irtifa):
    while drone.is_armable:
        print("İHA arm edilebilir.")

        drone.mode = VehicleMode("GUIDED")

        drone.armed = True

        while drone.armed is not True:
            print("Motorlar çalışıyor.")
            time.sleep(2)

        drone.simple_takeoff(irtifa)
        break
    if (drone.is_armable == False):
        print("İha arm edilebilir durumda değil!")
    time.sleep(1)


takeoff(10)

# konum = LocationGlobalRelative(-35.36221975,149.16512240,20)
# drone.simple_goto(konum)
