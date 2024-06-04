from machine import Pin, PWM
import neopixel
import time
from mpu6050 import MPU6050
from config import *
import math as m

#===============================#
#      Initialize modules       #
#===============================#

mpu=MPU6050(mpu_scl,mpu_sda,mpu_i2c)
mpu.MPU_Init()

np = neopixel.NeoPixel(Pin(neopixel_pin, Pin.OUT), 1)
np[0]=(0,0,0)
np.write()

#===============================#
#     Controlling functions     #
#===============================#

def color(c): # Sets the neopixel to a color
    if c == "red":
        c=(255,0,0)
    elif c == "green":
        c=(0,255,0)
    elif c == "blue":
        c=(0,0,255)
    elif c == "cyan":
        c=(0,255,255)
    elif c == "yellow":
        c=(255,255,0)
    elif c == "purple":
        c=(255,0,255)
    elif c == "black":
        c=(0,0,0)
    elif c == "white":
        c=(255,255,255)
    elif c == "orange":
        c=(255,50,0)
    c=(int(round(c[0]*neopixel_brightness)),int(round(c[1]*neopixel_brightness)),int(round(c[2]*neopixel_brightness)))
    np[0]=c
    np.write()

color(color_booting)
    

def servo(angle): # Sets the parachute's servo to an angle
    sv=PWM(Pin(servo_pin), freq=servo_freq)
    duty=((servo_duty_max-servo_duty_min)*angle/servo_range)+servo_duty_min
    sv.duty_u16(int(round(duty)))


def imu_data(rep=15): # Gives back the imu's data in m/s^2 and deg/s
    ta=[0,0,0]
    tg=[0,0,0]
    for i in range(rep):
        accel=mpu.MPU_Get_Accelerometer()
        gyro=mpu.MPU_Get_Gyroscope()
        ta[0]+=accel[0]
        ta[1]+=accel[1]
        ta[2]+=accel[2]
        tg[0]+=gyro[0]
        tg[1]+=gyro[1]
        tg[2]+=gyro[2]
    ta[0]/=rep
    ta[1]/=rep
    ta[2]/=rep
    tg[0]/=rep
    tg[1]/=rep
    tg[2]/=rep
    tax,tay,taz=-1*ta[0],ta[2],-1*ta[1]
    tgx,tgy,tgz=-1*tg[0],tg[2],-1*tg[1]
    accel=(tax,tay,taz)
    gyro=(tgx,tgy,tgz)
    return accel[0]/mpu_accel_convert/mpu_g_error,accel[1]/mpu_accel_convert/mpu_g_error,accel[2]/mpu_accel_convert/mpu_g_error,gyro[0]/mpu_rotation_convert,gyro[1]/mpu_rotation_convert,gyro[2]/mpu_rotation_convert


def tot_accel(use_g=True): # Gives back the imu's total acceleration vector
    accel=imu_data()
    tot=m.sqrt(abs(accel[0])**2+abs(accel[1])**2+abs(accel[2])**2)
    if use_g:
        return tot/G
    else:
        return tot
    
def tot_vector(accel):
    return m.sqrt(abs(accel[0])**2+abs(accel[1])**2+abs(accel[2])**2)

def dat_string(dat):
    return str(dat[0])+";"+str(dat[1])+";"+str(dat[2])+";"+str(dat[3])+";"+str(dat[4])+";"+str(dat[5])+";"+str(tot_vector(dat))+";"+str(dat[6])+"\n"

time.sleep(1) # Wait for everything to setup correctly

def exporter(dat):
    k=np[0]
    color("green")
    l=""
    
    for i in dat:
        l=l+dat_string(i)
    
    with open("log.csv","a") as log:
        log.write(l)
    print("Log saved")
    color(k)

#===============================#
#        Pre-flight setup       #
#===============================#

color(color_launch_setup)
print(tot_accel())
servo(parachute_open)
time.sleep(parachute_setup_time)
servo(parachute_closed)

color(color_waiting_for_launch)

with open("log.csv.bk1","r") as log:
    with open("log.csv.bk2", "w") as log2:
        log2.write(log.read())


with open("log.csv","r") as log:
    with open("log.csv.bk1", "w") as log2:
        log2.write(log.read())

while tot_accel() < liftoff_accel:
    pass

#===============================#
#      During-flight code       #
#===============================#

with open("log.csv","w") as log:
    log.write("Accel X;Accel Y;Accel Z;Gyro X;Gyro Y; Gyro Z;Total Accel;Time\n")

print("Liftoff",tot_accel())

color(color_ascending)

liftoff=time.ticks_us()

ms=[]

des=False

lt=0

while True:
    me=list(imu_data())
    me.append((time.ticks_us()-liftoff)/1000000)
    ms.append(me)
    if (tot_accel() < descend_accel and not des and time.ticks_us()-liftoff > minimum_deploy_time*1000000) or (time.ticks_us()-liftoff > maximum_deploy_time*1000000 and not des):
        print("Descending")
        servo(parachute_open)
        des=True
        color(color_descending)
    
    if len(ms) >= 40:
        exporter(ms)
        ms=[]
            
    if des and tot_accel() > landed_accel:
        lt+=1
    else:
        lt=0
    
    if lt == landed_readings:
        print("Landed")
        break
    #time.sleep(reading_delay/1000)


#===============================#
#       After-flight code       #
#===============================#

exporter(ms)

while True:
    color(color_landed_1)
    time.sleep(1)
    color(color_landed_2)
    time.sleep(1)


