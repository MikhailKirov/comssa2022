import RPi.GPIO as GPIO
import time
import pigpio
servo = 12
servo2 = 13
servoPIN2 = 13
pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)
pwm.set_PWM_frequency( servo, 50 )
print("starting")

try:
  print( "0 deg" )
  pwm.set_servo_pulsewidth( servo, 500 ) ;
  pwm.set_servo_pulsewidth( servo2, 500 ) ;
  time.sleep( 3 )

  print( "90 deg" )
  pwm.set_servo_pulsewidth( servo, 1500 ) ;
  pwm.set_servo_pulsewidth( servo2, 1500 ) ;
  time.sleep( 3 )

  print( "180 deg" )
  pwm.set_servo_pulsewidth( servo, 2500 ) ;
  pwm.set_servo_pulsewidth( servo2, 2500 ) ;
  time.sleep( 3 )

except KeyboardInterrupt:
  pwm.set_PWM_dutycycle( servo, 0 )
  pwm.set_PWM_frequency( servo2, 0 )
  GPIO.cleanup()
