import paho.mqtt.client as mqtt
from django.conf import settings

from .models import Sensor, SensorLog

def on_message_mqtt(sensor_name):
    def template(client, userdata, msg):
        sen = Sensor.objects.get(name=sensor_name)
        sen.value = msg.payload.decode('utf-8')
        sen.save()
        sen_log = SensorLog(name=sen, value=msg.payload.decode('utf-8'))
        sen_log.save()
    return template

def on_connect(client, userdata, rc, result):
    client.subscribe('s-farm1/#')
    client.subscribe('s-farm2/#')
    client.subscribe('s-farm3/#')
    client.subscribe('s-plant1/#')
    client.subscribe('s-plant2/#')
    client.subscribe('s-plant3/#')
    client.subscribe('s-resto1/#')
    client.subscribe('s-resto2/#')
    client.subscribe('s-resto3/#')

#sistem 1

on_message_sensor111 = on_message_mqtt('sfarm_1_1')
on_message_sensor112 = on_message_mqtt('sfarm_1_2')
on_message_sensor113 = on_message_mqtt('sfarm_1_3')

on_message_sensor121 = on_message_mqtt('sfarm_2_1')
on_message_sensor122 = on_message_mqtt('sfarm_2_2')
on_message_sensor123 = on_message_mqtt('sfarm_2_3')

on_message_sensor131 = on_message_mqtt('sfarm_3_1')
on_message_sensor132 = on_message_mqtt('sfarm_3_2')
on_message_sensor133 = on_message_mqtt('sfarm_3_3')

#sistem 2
on_message_sensor211 = on_message_mqtt('splant_1_1')
on_message_sensor212 = on_message_mqtt('splant_1_2')
on_message_sensor213 = on_message_mqtt('splant_1_3')

on_message_sensor221 = on_message_mqtt('splant_2_1')
on_message_sensor222 = on_message_mqtt('splant_2_2')
on_message_sensor223 = on_message_mqtt('splant_2_3')

on_message_sensor231 = on_message_mqtt('splant_3_1')
on_message_sensor232 = on_message_mqtt('splant_3_2')
on_message_sensor233 = on_message_mqtt('splant_3_3')

#sistem 3
on_message_sensor311 = on_message_mqtt('sresto_1_1')
on_message_sensor312 = on_message_mqtt('sresto_1_2')
on_message_sensor313 = on_message_mqtt('sresto_1_3')

on_message_sensor321 = on_message_mqtt('sresto_2_1')
on_message_sensor322 = on_message_mqtt('sresto_2_2')
on_message_sensor323 = on_message_mqtt('sresto_2_3')

on_message_sensor331 = on_message_mqtt('sresto_3_1')
on_message_sensor332 = on_message_mqtt('sresto_3_2')
on_message_sensor333 = on_message_mqtt('sresto_3_3')

client = mqtt.Client()

#=============================================================================================

#sistem 1
client.message_callback_add('s-farm1/1', on_message_sensor111)
client.message_callback_add('s-farm1/2', on_message_sensor112)
client.message_callback_add('s-farm1/3', on_message_sensor113)

client.message_callback_add('s-farm2/1', on_message_sensor121)
client.message_callback_add('s-farm2/2', on_message_sensor122)
client.message_callback_add('s-farm2/3', on_message_sensor123)

client.message_callback_add('s-farm3/1', on_message_sensor131)
client.message_callback_add('s-farm3/2', on_message_sensor132)
client.message_callback_add('s-farm3/3', on_message_sensor133)

#sistem2
client.message_callback_add('s-plant1/1', on_message_sensor211)
client.message_callback_add('s-plant1/2', on_message_sensor212)
client.message_callback_add('s-plant1/3', on_message_sensor213)

client.message_callback_add('s-plant2/1', on_message_sensor221)
client.message_callback_add('s-plant2/2', on_message_sensor222)
client.message_callback_add('s-plant2/3', on_message_sensor223)

client.message_callback_add('s-plant3/1', on_message_sensor231)
client.message_callback_add('s-plant3/2', on_message_sensor232)
client.message_callback_add('s-plant3/3', on_message_sensor233)

#sistem3
client.message_callback_add('s-resto1/1', on_message_sensor311)
client.message_callback_add('s-resto1/2', on_message_sensor312)
client.message_callback_add('s-resto1/3', on_message_sensor313)

client.message_callback_add('s-resto2/1', on_message_sensor321)
client.message_callback_add('s-resto2/2', on_message_sensor322)
client.message_callback_add('s-resto2/3', on_message_sensor323)

client.message_callback_add('s-resto3/1', on_message_sensor331)
client.message_callback_add('s-resto3/2', on_message_sensor332)
client.message_callback_add('s-resto3/3', on_message_sensor333)

client.on_connect = on_connect

client.connect(settings.MQTT_HOST, settings.MQTT_PORT)
