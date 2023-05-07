from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
import paho.mqtt.client as mqtt
import time

from .serializers import SensorSerializer
from .models import Sensor


# Create your views here.
def index(request):
    sfarm_1_1 = Sensor.objects.get(name="sfarm_1_1")
    sfarm_1_2 = Sensor.objects.get(name="sfarm_1_2")
    sfarm_1_3 = Sensor.objects.get(name="sfarm_1_3")
    sfarm_2_1 = Sensor.objects.get(name="sfarm_2_1")
    sfarm_2_2 = Sensor.objects.get(name="sfarm_2_2")
    sfarm_2_3 = Sensor.objects.get(name="sfarm_2_3")
    sfarm_3_1 = Sensor.objects.get(name="sfarm_3_1")
    sfarm_3_2 = Sensor.objects.get(name="sfarm_3_2")
    sfarm_3_3 = Sensor.objects.get(name="sfarm_3_3")

    splant_1_1 = Sensor.objects.get(name="splant_1_1")
    splant_1_2 = Sensor.objects.get(name="splant_1_2")
    splant_1_3 = Sensor.objects.get(name="splant_1_3")
    splant_2_1 = Sensor.objects.get(name="splant_2_1")
    splant_2_2 = Sensor.objects.get(name="splant_2_2")
    splant_2_3 = Sensor.objects.get(name="splant_2_3")
    splant_3_1 = Sensor.objects.get(name="splant_3_1")
    splant_3_2 = Sensor.objects.get(name="splant_3_2")
    splant_3_3 = Sensor.objects.get(name="splant_3_3")

    sresto_1_1 = Sensor.objects.get(name="sresto_1_1")
    sresto_1_2 = Sensor.objects.get(name="sresto_1_2")
    sresto_1_3 = Sensor.objects.get(name="sresto_1_3")
    sresto_2_1 = Sensor.objects.get(name="sresto_2_1")
    sresto_2_2 = Sensor.objects.get(name="sresto_2_2")
    sresto_2_3 = Sensor.objects.get(name="sresto_2_3")
    sresto_3_1 = Sensor.objects.get(name="sresto_3_1")
    sresto_3_2 = Sensor.objects.get(name="sresto_3_2")
    sresto_3_3 = Sensor.objects.get(name="sresto_3_3")


    context = {
        "sfarm_1_1": str(sfarm_1_1.value),
        "sfarm_1_2": str(sfarm_1_2.value),
        "sfarm_1_3": str(sfarm_1_3.value),
        "sfarm_2_1": str(sfarm_2_1.value),
        "sfarm_2_2": str(sfarm_2_2.value),
        "sfarm_2_3": str(sfarm_2_3.value),
        "sfarm_3_1": str(sfarm_3_1.value),
        "sfarm_3_2": str(sfarm_3_2.value),
        "sfarm_3_3": str(sfarm_3_3.value),

        "splant_1_1": str(splant_1_1.value),
        "splant_1_2": str(splant_1_2.value),
        "splant_1_3": str(splant_1_3.value),
        "splant_2_1": str(splant_2_1.value),
        "splant_2_2": str(splant_2_2.value),
        "splant_2_3": str(splant_2_3.value),
        "splant_3_1": str(splant_3_1.value),
        "splant_3_2": str(splant_3_2.value),
        "splant_3_3": str(splant_3_3.value),

        "sresto_1_1": str(sresto_1_1.value),
        "sresto_1_2": str(sresto_1_2.value),
        "sresto_1_3": str(sresto_1_3.value),
        "sresto_2_1": str(sresto_2_1.value),
        "sresto_2_2": str(sresto_2_2.value),
        "sresto_2_3": str(sresto_2_3.value),
        "sresto_3_1": str(sresto_3_1.value),
        "sresto_3_2": str(sresto_3_2.value),
        "sresto_3_3": str(sresto_3_3.value)
    }

    return render(request, 'index.html', context)


def on_message_sfarm_1_1(client, userdata, msg):
    sfarm_1_1 = Sensor.objects.get(name = 'sfarm_1_1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sfarm_1_1, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_sfarm_1_2(client, userdata, msg):
    sfarm_1_2 = Sensor.objects.get(name = 'sfarm_1_2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sfarm_1_2, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_sfarm_1_3(client, userdata, msg):
    sfarm_1_3 = Sensor.objects.get(name = 'sfarm_1_3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sfarm_1_3, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))


def on_message_sfarm_2_1(client, userdata, msg):
    sfarm_2_1 = Sensor.objects.get(name = 'sfarm_2_1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sfarm_2_1, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_sfarm_2_2(client, userdata, msg):
    sfarm_2_2 = Sensor.objects.get(name = 'sfarm_2_2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sfarm_2_2, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_sfarm_2_3(client, userdata, msg):
    sfarm_2_3 = Sensor.objects.get(name = 'sfarm_2_3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sfarm_2_3, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))


def on_message_sfarm_3_1(client, userdata, msg):
    sfarm_3_1 = Sensor.objects.get(name = 'sfarm_3_1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sfarm_3_1, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_sfarm_3_2(client, userdata, msg):
    sfarm_3_2 = Sensor.objects.get(name = 'sfarm_3_2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sfarm_3_2, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_sfarm_3_3(client, userdata, msg):
    sfarm_3_3 = Sensor.objects.get(name = 'sfarm_3_3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sfarm_3_3, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))

################################################

def on_message_splant_1_1(client, userdata, msg):
    splant_1_1 = Sensor.objects.get(name = 'splant_1_1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(splant_1_1, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_splant_1_2(client, userdata, msg):
    splant_1_2 = Sensor.objects.get(name = 'splant_1_2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(splant_1_2, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_splant_1_3(client, userdata, msg):
    splant_1_3 = Sensor.objects.get(name = 'splant_1_3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(splant_1_3, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))


def on_message_splant_2_1(client, userdata, msg):
    splant_2_1 = Sensor.objects.get(name = 'splant_2_1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(splant_2_1, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_splant_2_2(client, userdata, msg):
    splant_2_2 = Sensor.objects.get(name = 'splant_2_2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(splant_2_2, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_splant_2_3(client, userdata, msg):
    splant_2_3 = Sensor.objects.get(name = 'splant_2_3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(splant_2_3, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))


def on_message_splant_3_1(client, userdata, msg):
    splant_3_1 = Sensor.objects.get(name = 'splant_3_1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(splant_3_1, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_splant_3_2(client, userdata, msg):
    splant_3_2 = Sensor.objects.get(name = 'splant_3_2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(splant_3_2, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_splant_3_3(client, userdata, msg):
    splant_3_3 = Sensor.objects.get(name = 'splant_3_3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(splant_3_3, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))

#####################################################################

def on_message_sresto_1_1(client, userdata, msg):
    sresto_1_1 = Sensor.objects.get(name = 'sresto_1_1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sresto_1_1, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_sresto_1_2(client, userdata, msg):
    sresto_1_2 = Sensor.objects.get(name = 'sresto_1_2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sresto_1_2, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_sresto_1_3(client, userdata, msg):
    sresto_1_3 = Sensor.objects.get(name = 'sresto_1_3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sresto_1_3, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))


def on_message_sresto_2_1(client, userdata, msg):
    sresto_2_1 = Sensor.objects.get(name = 'sresto_2_1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sresto_2_1, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_sresto_2_2(client, userdata, msg):
    sresto_2_2 = Sensor.objects.get(name = 'sresto_2_2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sresto_2_2, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_sresto_2_3(client, userdata, msg):
    sresto_2_3 = Sensor.objects.get(name = 'sresto_2_3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sresto_2_3, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))


def on_message_sresto_3_1(client, userdata, msg):
    sresto_3_1 = Sensor.objects.get(name = 'sresto_3_1')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sresto_3_1, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_sresto_3_2(client, userdata, msg):
    sresto_3_2 = Sensor.objects.get(name = 'sresto_3_2')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sresto_3_2, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))
def on_message_sresto_3_3(client, userdata, msg):
    sresto_3_3 = Sensor.objects.get(name = 'sresto_3_3')
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sresto_3_3, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new data', msg.payload.decode('utf-8'))

client = mqtt.Client("sensor")

client.message_callback_add('s-farm1/1', on_message_sfarm_1_1)
client.message_callback_add('s-farm1/2', on_message_sfarm_1_2)
client.message_callback_add('s-farm1/3', on_message_sfarm_1_3)
client.message_callback_add('s-farm2/1', on_message_sfarm_2_1)
client.message_callback_add('s-farm2/2', on_message_sfarm_2_2)
client.message_callback_add('s-farm2/3', on_message_sfarm_2_3)
client.message_callback_add('s-farm3/1', on_message_sfarm_3_1)
client.message_callback_add('s-farm3/2', on_message_sfarm_3_2)
client.message_callback_add('s-farm3/3', on_message_sfarm_3_3)

client.message_callback_add('s-plant1/1', on_message_splant_1_1)
client.message_callback_add('s-plant1/2', on_message_splant_1_2)
client.message_callback_add('s-plant1/3', on_message_splant_1_3)
client.message_callback_add('s-plant2/1', on_message_splant_2_1)
client.message_callback_add('s-plant2/2', on_message_splant_2_2)
client.message_callback_add('s-plant2/3', on_message_splant_2_3)
client.message_callback_add('s-plant3/1', on_message_splant_3_1)
client.message_callback_add('s-plant3/2', on_message_splant_3_2)
client.message_callback_add('s-plant3/3', on_message_splant_3_3)

client.message_callback_add('s-resto1/1', on_message_sresto_1_1)
client.message_callback_add('s-resto1/2', on_message_sresto_1_2)
client.message_callback_add('s-resto1/3', on_message_sresto_1_3)
client.message_callback_add('s-resto2/1', on_message_sresto_2_1)
client.message_callback_add('s-resto2/2', on_message_sresto_2_2)
client.message_callback_add('s-resto2/3', on_message_sresto_2_3)
client.message_callback_add('s-resto3/1', on_message_sresto_3_1)
client.message_callback_add('s-resto3/2', on_message_sresto_3_2)
client.message_callback_add('s-resto3/3', on_message_sresto_3_3)


client.connect('localhost', 1883)
client.loop_start()
client.subscribe('#')