from django.shortcuts import render
from django.views.generic import View
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

import joblib
from machinelearning import LinregML

from .models import Sensor, SensorLog, Actuator, ActuatorLog

class SensorTemplateView(APIView):
    sensor_name = ""
    def get(self, request, format=None):
        sensor = Sensor.objects.get(name=self.sensor_name)
        data = {
            "value": sensor.value
        }
        return Response(data)

class ActuatorTemplateView(APIView):
    actuator_name = ""
    sensor1_name  = ""
    sensor2_name  = ""
    sensor3_name  = ""
    training_csv  = ""
    def get(self, request, format=None):
        actuator = Actuator.objects.get(name=self.actuator_name)
        sensor1  = Sensor.objects.get(name=self.sensor1_name)
        sensor2  = Sensor.objects.get(name=self.sensor2_name)
        sensor3  = Sensor.objects.get(name=self.sensor3_name)
        model = mlmodel.BaseLinearRegression(settings.ML_ROOT + self.training_csv)
        prediction = model.predict([float(sensor1.value), float(sensor2.value), float(sensor3.value)])
        actuator.state = int(prediction)
        actuator.save()
        data = {
            "state": actuator.state
        }
        return Response(data)

class ActuatorTemplateSystemView(APIView):
    actuator_name = ""
    actuatorsubsystem1  = ""
    actuatorsubsystem2  = ""
    actuatorsubsystem3  = ""
    training_csv  = ""
    def get(self, request, format=None):
        actuator = Actuator.objects.get(name=self.actuator_name)
        actuatorsubsystem1 = Actuator.objects.get(name=self.actuatorsubsystem1)
        actuatorsubsystem2 = Actuator.objects.get(name=self.actuatorsubsystem2)
        actuatorsubsystem3 = Actuator.objects.get(name=self.actuatorsubsystem3)
        model = mlmodel.BaseLinearRegression(settings.ML_ROOT + self.training_csv)
        prediction = model.predict([float(actuatorsubsystem1.state), float(actuatorsubsystem2.state), float(actuatorsubsystem3.state)])
        actuator.state = int(prediction)
        actuator.save()
        data = {
            "state": actuator.state
        }
        return Response(data)

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

# Smart Farm ==========================================================================================================================================
# Susu Hewani dan Telur
class SensorSPCView(SensorTemplateView):
    sensor_name = "sfarm_1_1"
    
class SensorKekeruhanView(SensorTemplateView):
    sensor_name = "sfarm_1_2"

class SensorKepadatanView(SensorTemplateView):
    sensor_name = "sfarm_1_3"
    
class actuator1view(ActuatorTemplateView):
    actuator_name = "actuator1"
    sensor1_name = "sfarm_1_1"
    sensor2_name = "sfarm_1_2"
    sensor3_name = "sfarm_1_3"
    training_csv = "actuator1.csv"

# Daging Merah
class SensorMikroorganismeView(SensorTemplateView):
    sensor_name = "sfarm_2_1"
    
class SensorMioglobinView(SensorTemplateView):
    sensor_name = "sfarm_2_2"
    
class SensorBeratView(SensorTemplateView):
    sensor_name = "sfarm_2_3"
    
class actuator2view(ActuatorTemplateView):
    actuator_name = "actuator2"
    sensor1_name = "sfarm_2_1"
    sensor2_name = "sfarm_2_2"
    sensor3_name = "sfarm_2_3"
    training_csv = "actuator2.csv"
    
# Daging Putih
class SensorKadarNitrogenView(SensorTemplateView):
    sensor_name = "sfarm_3_1"
    
class SensorKadarOksigenView(SensorTemplateView):
    sensor_name = "sfarm_3_2"
    
class SensorKadarKarbondioksidaView(SensorTemplateView):
    sensor_name = "sfarm_3_3"

class actuator3view(ActuatorTemplateView):
    actuator_name = "actuator3"
    sensor1_name = "sfarm_3_1"
    sensor2_name = "sfarm_3_2"
    sensor3_name = "sfarm_3_3"
    training_csv = "actuator3.csv"

# Smart Plantation ==========================================================================================================================================
# 	Sumber Karbohidrat
class SensorKadarSeratView(SensorTemplateView):
    sensor_name = "splant_1_1"
    
class SensorKadarProteinView(SensorTemplateView):
    sensor_name = "splant_1_2"

class SensorKadarAirView(SensorTemplateView):
    sensor_name = "splant_1_3"
    
class actuator4view(ActuatorTemplateView):
    actuator_name = "actuator4"
    sensor1_name = "splant_1_1"
    sensor2_name = "splant_1_2"
    sensor3_name = "splant_1_3"
    training_csv = "actuator4.csv"

# Sayuran
class SensorKadarKlorofilView(SensorTemplateView):
    sensor_name = "splant_2_1"
    
class SensorKadarVitaminCView(SensorTemplateView):
    sensor_name = "splant_2_2"
    
class SensorKadarVitaminKView(SensorTemplateView):
    sensor_name = "splant_2_3"
    
class actuator5view(ActuatorTemplateView):
    actuator_name = "actuator5"
    sensor1_name = "splant_2_1"
    sensor2_name = "splant_2_2"
    sensor3_name = "splant_2_3"
    training_csv = "actuator5.csv"
    
# Buah-buahan
class SensorTeksturView(SensorTemplateView):
    sensor_name = "splant_3_1"
    
class SensorNN1View(SensorTemplateView):
    sensor_name = "splant_3_2"
    
class SensorNN2View(SensorTemplateView):
    sensor_name = "splant_3_3"

class actuator6view(ActuatorTemplateView):
    actuator_name = "actuator6"
    sensor1_name = "splant_3_1"
    sensor2_name = "splant_3_2"
    sensor3_name = "splant_3_3"
    training_csv = "actuator6.csv"

# Smart Restaurant ==========================================================================================================================================
# DeteKsi Musim
class SensorTemperatureView(SensorTemplateView):
    sensor_name = "sresto_1_1"
    
class SensorHumidityView(SensorTemplateView):
    sensor_name = "sresto_1_2"

class SensorWindSpeedView(SensorTemplateView):
    sensor_name = "sresto_1_3"
    
class actuator7view(ActuatorTemplateView):
    actuator_name = "actuator7"
    sensor1_name = "sresto_1_1"
    sensor2_name = "sresto_1_2"
    sensor3_name = "sresto_1_3"
    training_csv = "actuator7.csv"

# Deteksi Hasil Penjualan Berfluktuasi
class SensorFinanceView(SensorTemplateView):
    sensor_name = "sresto_2_1"
    
class SensorSatisfactionView(SensorTemplateView):
    sensor_name = "sresto_2_2"
    
class SensorNN3View(SensorTemplateView):
    sensor_name = "sresto_2_3"
    
class actuator8view(ActuatorTemplateView):
    actuator_name = "actuator8"
    sensor1_name = "sresto_2_1"
    sensor2_name = "sresto_2_2"
    sensor3_name = "sresto_2_3"
    training_csv = "actuator8.csv"
    
# Deteksi Jumlah Pengunjung Restoran
class SensorNN4View(SensorTemplateView):
    sensor_name = "sresto_3_1"
    
class SensorNN5View(SensorTemplateView):
    sensor_name = "sresto_3_2"
    
class SensorNN6View(SensorTemplateView):
    sensor_name = "sresto_3_3"

class actuator9view(ActuatorTemplateView):
    actuator_name = "actuator9"
    sensor1_name = "sresto_3_1"
    sensor2_name = "sresto_3_2"
    sensor3_name = "sresto_3_3"
    training_csv = "actuator9.csv"

class actuatorsubsystem1view(ActuatorTemplateSystemView):
    actuator_name = "actuatorsubsystem1"
    actuatorsubsystem1 = "actuator1"
    actuatorsubsystem2 = "actuator2"
    actuatorsubsystem3 = "actuator3"
    training_csv = "subsystem1.csv"

class actuatorsubsystem2view(ActuatorTemplateSystemView):
    actuator_name = "actuatorsubsystem2"
    actuatorsubsystem1 = "actuator4"
    actuatorsubsystem2 = "actuator5"
    actuatorsubsystem3 = "actuator6"
    training_csv = "subsystem2.csv"

class actuatorsubsystem3view(ActuatorTemplateSystemView):
    actuator_name = "actuatorsubsystem3"
    actuatorsubsystem1 = "actuator7"
    actuatorsubsystem2 = "actuator8"
    actuatorsubsystem3 = "actuator9"
    training_csv = "subsystem3.csv"

class actuatorsystemview(ActuatorTemplateSystemView):
    actuator_name = "actuatorsystem"
    actuatorsubsystem1 = "actuatorsubsystem1"
    actuatorsubsystem2 = "actuatorsubsystem2"
    actuatorsubsystem3 = "actuatorsubsystem3"
    training_csv = "actuator.csv"