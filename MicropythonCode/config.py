# RGB led config

neopixel_pin = 16
neopixel_brightness = 1

# MPU6050 config

mpu_sda=0
mpu_scl=1
mpu_i2c=0
G=9.806666
mpu_accel_convert=1670.7
mpu_rotation_convert=131
mpu_g_error=1.086835714

# Parachute servo config

servo_pin=3
servo_freq=50
servo_duty_max=8000
servo_duty_min=2000
servo_range=180
parachute_open=30
parachute_closed=90
parachute_setup_time=0.5
minimum_deploy_time=5
maximum_deploy_time=10

# Status colors

color_booting="yellow"
color_waiting_for_launch="green"
color_launch_setup="blue"
color_ascending="orange"
color_descending="red"
color_landed_1="purple"
color_landed_2="black"

# Other

liftoff_accel=2
descend_accel=0.5
landed_accel=0.9
reading_delay=0.05
landed_readings=20

