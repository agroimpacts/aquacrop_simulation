# Source: Sitian modified from https://pypi.org/project/aquacrop/
# specifically:
#https://colab.research.google.com/github/thomasdkelly/aquacrop/blob/master/tutorials/AquaCrop_OSPy_Notebook_1.ipynb
# Current aquacrop version: 0.2 (Released on Jun 14, 2021)

from aquacrop.classes import *
from aquacrop.core import *
import os
import pandas as pd
#project_path = "E://DropBox//Agroimpacts//AquaCrop"
project_path = "F://AquaCrop_F"
out_path = "14663_Nov15"
weather_path = "14663_Weather"
# list
result = []
for i in range(1,14664,1):
    print("running on " + str(i))

    filepath = os.path.join(project_path,weather_path,"station_"+ str(i) +"_weather.csv")
    #filepath= os.path.join(project_path,"Weather","station_weather.csv")
    weather_data = pd.read_csv(filepath)
    weather_data["Date"] = pd.to_datetime(weather_data["Date"])

    sandy_loam = SoilClass(soilType='Clay') # 'SandyLoam'
    maize = CropClass('Maize', PlantingDate='11/15')
    InitWC = InitWCClass(value=['FC']) # 0.2 or dynamic (Noemi's soilmoisture)/percent of rainfall

    model = AquaCropModel(SimStartTime=f'{2000}/11/15',
                          SimEndTime=f'{2014}/05/30',
                          wdf=weather_data,
                          Soil=sandy_loam,
                          Crop=maize,
                          InitWC=InitWC)

    # initilize model
    model.initialize()
    # run model till termination
    model.step(till_termination=True)

    #print(model.Outputs.Final)
    model.Outputs.Final.to_csv(os.path.join(project_path, out_path,"out_final"+str(i)+".csv"))
    model.Outputs.Growth.to_csv(os.path.join(project_path, out_path,"out_growth"+str(i)+".csv"))
    model.Outputs.Flux.to_csv(os.path.join(project_path, out_path,"out_flux"+str(i)+".csv"))
    model.Outputs.Water.to_csv(os.path.join(project_path, out_path,"out_water"+str(i)+".csv"))
