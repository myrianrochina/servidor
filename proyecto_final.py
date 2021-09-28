from machine import Pin
from time import sleep
from random import randint
# variables
boton1 = Pin(4, Pin.IN, Pin.PULL_UP)
boton2 = Pin(16, Pin.IN, Pin.PULL_UP)
led = Pin(0, Pin.OUT)
a='OFF' 
b='OFF'
# variables para almacenar el estado de los botones
aa='OFF' 
bb='OFF'
#Configuracion MQTT
from umqtt.simple import MQTTClient
cliente=MQTTClient('mm', 'maqiatto.com', 1883, 'my-ro03@hotmail.com', '//MyriaN2019//')
#controla los mensajes que llegan de la web
def nuevoMensaje(topic,msg):
    print(msg)
    if msg.decode() == "ON":
        led.on()
    elif msg.decode() == "OFF":
        led.off()     
cliente.set_callback(nuevoMensaje)
cliente.connect()
cliente.subscribe('my-ro03@hotmail.com/t1')
sleep(3)

while 1:
    cliente.check_msg()
   #Si se presiona el boton1
    if (boton1.value() == 0):
        a='ON'
    else:
        a='OFF'
    #Si se presiona el boton2
    if (boton2.value() == 0):
        b='ON'
    else:
        b='OFF'
#     comprueba el estado de los botones
    if (a!=aa or b!=bb):
        aa=a
        bb=b
        print('Enviado '+ str(a)+'*'+str(b))
        cliente.publish('my-ro03@hotmail.com/t2', str(a)+'*'+str(b))
        sleep(0.1)