from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view()),

#Smart Farm
    # Susu Hewani dan Telur
    path('s-farm1/1', views.SensorSPCView.as_view()),
    path('s-farm1/2', views.SensorKekeruhanView.as_view()),
    path('s-farm1/3', views.SensorKepadatanView.as_view()),
    path('actuator/actuator1', views.actuator1view.as_view()),
    
    # Daging Merah
    path('s-farm2/1', views.SensorMikroorganismeView.as_view()),
    path('s-farm2/2', views.SensorMioglobinView.as_view()),
    path('s-farm2/3', views.SensorBeratView.as_view()),
    path('actuator/actuator2', views.actuator2view.as_view()),
    
    # Daging Merah 
    path('s-farm3/1', views.SensorKadarNitrogenView.as_view()),
    path('s-farm3/2', views.SensorKadarOksigenView.as_view()),
    path('s-farm3/3', views.SensorKadarKarbondioksidaView.as_view()),
    path('actuator/actuator3', views.actuator3view.as_view()),

#Smart Plantation
    # Sumber Karbohidrat
    path('s-plant1/1', views.SensorKadarSeratView.as_view()),
    path('s-plant1/2', views.SensorKadarProteinView.as_view()),
    path('s-plant1/3', views.SensorKadarAirView.as_view()),
    path('actuator/actuator4', views.actuator4view.as_view()),
    
    # Sayuran
    path('s-plant2/1', views.SensorKadarKlorofilView.as_view()),
    path('s-plant2/2', views.SensorKadarVitaminCView.as_view()),
    path('s-plant2/3', views.SensorKadarVitaminKView.as_view()),
    path('actuator/actuator5', views.actuator5view.as_view()),
    
    # Buah-buahan
    path('s-plant3/1', views.SensorTeksturView.as_view()),
    path('s-plant3/2', views.SensorNN1View.as_view()),
    path('s-plant3/3', views.SensorNN2View.as_view()),
    path('actuator/actuator6', views.actuator6view.as_view()),

#Smart Restaurant
    # DeteKsi Musim
    path('s-resto1/1', views.SensorTemperatureView.as_view()),
    path('s-resto1/2', views.SensorHumidityView.as_view()),
    path('s-resto1/3', views.SensorWindSpeedView.as_view()),
    path('actuator/actuator7', views.actuator7view.as_view()),
    
    # Deteksi Hasil Penjualan Berfluktuasi
    path('s-resto2/1', views.SensorFinanceView.as_view()),
    path('s-resto2/2', views.SensorSatisfactionView.as_view()),
    path('s-resto2/3', views.SensorNN3View.as_view()),
    path('actuator/actuator8', views.actuator8view.as_view()),
    
    # Deteksi Jumlah Pengunjung Restoran
    path('s-resto3/1', views.SensorNN4View.as_view()),
    path('s-resto3/2', views.SensorNN5View.as_view()),
    path('s-resto3/3', views.SensorNN6View.as_view()),
    path('actuator/actuator9', views.actuator9view.as_view()),

    path('actuator/actuatorsubsystem1', views.actuatorsubsystem1view.as_view()),
    path('actuator/actuatorsubsystem2', views.actuatorsubsystem2view.as_view()),
    path('actuator/actuatorsubsystem3', views.actuatorsubsystem3view.as_view()),
    path('actuator/actuatorsystem', views.actuatorsystemview.as_view())
]