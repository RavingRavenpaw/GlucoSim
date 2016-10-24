import os
import sys
import platform
#import numpy as np
#from datetime import datetime
#from bokeh.charts import Line, output_file, show
from bokeh.io import output_file, show
from bokeh.layouts import layout, widgetbox
from bokeh.plotting import figure
from bokeh.models.widgets import Paragraph

#Diabetes/Body Energy Simulation Project

def sim():
    #VARIABLE INITIALIZATION

    glucose_blood_level = 100.0
    #Glucose level/concentration of the blood in mg/dL

    glucose_blood = 4617.5
    #Glucose present in the blood in mg


    glycogen_liver = 100000
    #Glycogen stored in the liver in mg

    glycogen_muscles = 500000
    #Glycogen stored in the muscles in mg

    insulin_blood = 15.0
    #Insulin present in the blood in μU/mL

    glucagon_blood = 20.00
    #Glucagon present in the blood in in pg/mL

    carb_insulin_ratio = 15000
    #Amount of mg of carbohydrate that one unit of insulin will metabolize/cover

    glycogenolysis_ratio = 1
    #Grams of glycogen that one unit/one pg of glucagon will release
    #NOT FACTUAL, FOR SIMULATION TESTING PURPOSES ONLY

    glycogenesis_ratio = 1
    #Grams of glycogen that one gram of glucose will synthesize
    #NOT FACTUAL, FOR SIMULATION TESTING PURPOSES ONLY

    glycogen_to_glucose_ratio = 1
    #Grams of glucose released from one gram of glycogen
    #NOT FACTUAL, FOR SIMULATION TESTING PURPOSES ONLY

    fat_nonessential = 16983.0
    #Nonessential (burnable) fat stored in adipose tissue in grams

    fat_essential = 2830.0
    #Essential (non-burnable) fat stored in adipose tissue in grams

    fat_total = 19813.0
    #Total fat in adipose tissue in grams

    metabolic_rate = 3
    #Number used to represent metabolic activity of the body
    #NOT FACTUAL, FOR SIMULATION OF METABOLIC ACTIVITY
    #TO ENHANCE REALISM OF SIMULATION ONLY

    blood_volume = 46.175
    #Volume of blood in dL

    bgDataX = []

    bgDataY = []

    bgNormDataX = []
    bgNormDataY = []
    bgHighDataX = []
    bgHighDataY = []
    bgLowDataX = []
    bgLowDataY = []

    currentTime = 0

    bgData = []
    bgNormData = {}
    bgLowData = {}
    bgHighData = {}
    insulinDataX = []
    insulinDataY = []
    glucagonDataX = []
    glucagonDataY = []

    timeData = []
    #Lists for keeping past data on blood glucose level and insulin
    #and glucagon concentrations.

    currentTime = 0

    ROC_predictionX = []
    ROC_predictionY = []



    #Loop the program forever.
    while(1==1):

        #CALCULATE NUMBERS


        currentTime+=1
        #currentTime = str(datetime.now())
        #currentTime = currentTime.replace("-", "")
        #currentTime = currentTime.replace(":", "")
        #currentTime = currentTime.replace(".", "")
        #currentTime = currentTime.replace(" ", "")

        #glucose_blood_level = (glucose_blood_level - insulin_blood + (glucagon_blood*12.5) - (metabolic_rate))
        #- (carb_insulin_ratio*insulin_blood) + (glycogenolysis_ratio*glucagon_blood*glycogen_to_glucose_ratio))
        if glycogen_liver > 0:
            #Release glycogen & convert to glucose
            glycogen_liver -= (glucagon_blood*glycogenolysis_ratio)
            glucose_blood += (glucagon_blood*glycogenolysis_ratio*glycogen_to_glucose_ratio)

        if glycogen_liver < 100000:
            #Absorb glucose & convert to glycogen
            glycogen_liver += ((insulin_blood/1000000)*carb_insulin_ratio*glycogenesis_ratio)
            glucose_blood -= ((insulin_blood/1000000*blood_volume/10)*carb_insulin_ratio)
    
        glucose_blood -= metabolic_rate*10
        glucose_blood_level = (glucose_blood/blood_volume)
        #glycogen_liver -+ (insulin_blood*
        #insulin_blood = insulin_blood - insulin_blood
        #glucagon_blood = glucagon_blood - glucagon_blood
        if glucose_blood_level < 0.0:
            glucose_blood_level = 0.0

        bgData.append(glucose_blood_level)

        insulinDataX.append(currentTime)
        insulinDataY.append(insulin_blood)

        glucagonDataX.append(currentTime)
        glucagonDataY.append(glucagon_blood)

        bgDataX.append(currentTime)
        bgDataY.append(glucose_blood_level)

        #nan = float('nan')

        if glucose_blood_level >= 80 and glucose_blood_level <= 180:
            #bgNormDataDict[currentTime] = glucose_blood_level
            bgNormDataX.append(currentTime)
            bgNormDataY.append(glucose_blood_level)
            #bgHighDataX.append(nan)
            #bgHighDataX.append(nan)
            #bgLowDataX.append(nan)
            #bgLowDataY.append(nan)

        if glucose_blood_level > 180:
            #bgHighDataDict[currentTime] = glucose_blood_level
            bgHighDataX.append(currentTime)
            bgHighDataY.append(glucose_blood_level)
            #bgNormDataX.append(nan)
            #bgNormDataX.append(nan)
            #bgLowDataX.append(nan)
            #bgLowDataY.append(nan)

        if glucose_blood_level < 80:
            #bgLowDataDict[currentTime] = glucose_blood_level
            bgLowDataX.append(currentTime)
            bgLowDataY.append(glucose_blood_level)
            #bgHighDataX.append(nan)
            #bgHighDataX.append(nan)
            #bgNormDataX.append(nan)
            #bgNormDataY.append(nan)


        if len(bgData) >=3:
            bgRateOfChange = ((bgData[-1] - bgData[-2]) + (bgData[-2] - bgData[-3]))/2
            #Steady

            #ROC Prediction
            ROC_predictionX = []
            ROC_predictionY = []
            iterations = 1
            for x in range (0,6):
                ROC_predictionX.append(currentTime + iterations)
                ROC_predictionY.append(glucose_blood_level + (bgRateOfChange*iterations))
                iterations += 1

            if bgRateOfChange < 1 and bgRateOfChange > -1:
                ROC_arrows_WB = "→"
                ROC_arrows = "-> steady"

            #Rising
            if bgRateOfChange >= 1 and bgRateOfChange < 2:
                ROC_arrows_WB = "↗"
                ROC_arrows = "/^ slowly rising"
            if bgRateOfChange >= 2 and bgRateOfChange > 3:
                ROC_arrows_WB = "↑"
                ROC_arrows = "^|^ rising"
            if bgRateOfChange >= 3:
                ROC_arrows_WB = "⇈"
                ROC_arrows = "^|^ ^|^ rapidly rising"

            #Falling
            if bgRateOfChange <= -1 and bgRateOfChange > -2:
                ROC_arrows_WB = "↘"
                ROC_arrows = "\\v slowly falling"
            if bgRateOfChange <= -2 and bgRateOfChange > -3:
                ROC_arrows_WB = "↓"
                ROC_arrows = "v|v falling"
            if bgRateOfChange <= -3:
                ROC_arrows_WB = "⇊  RAPIDLY FALLING!"
                ROC_arrows = "v|v v|v RAPIDLY FALLING /!\\"
        else:
            bgRateOfChange = 0
            ROC_arrows_WB = "N/A"
            ROC_arrows = "N/A"
            
        
        ROC_widget = Paragraph(text=ROC_arrows_WB, width=50, height=25)

        #CODE FOR ROC PREDICTION
        ROC_predictionX = []
        ROC_predictionY = []
        x = 0
        for x in range (0, 6):
            x+=1
            ROC_predictionX.append(currentTime + 1)
            ROC_predictionY.append(glucose_blood_level + bgRateOfChange)



        #UPDATE DISPLAY

        #Clear the terminal window
        if platform.system() == "Windows":
            os.system('cls')

        else:
            os.system("clear")
    
        #Print basic textual UI to the terminal window
        print ("Diabetes/Body Energy Simulation Project")
        print ("2015 - 2016, created by John Kozlosky")
        print ("")
        print ("Blood glucose level: " + str(round(glucose_blood_level, 2)) + "mg/dL " + ROC_arrows)
        print ("Blood glucose: " + str(round((glucose_blood/1000), 2)) + "g")
        print ("Glycogen: " + str(round((glycogen_liver/1000), 2)) + "g hepatic, " + str(round(glycogen_muscles, 2)/1000) + "g muscular")
        print ("Blood insulin: " + str(round(insulin_blood, 2)) + "uU/mL")
        print ("Blood glucagon: " + str(round(glucagon_blood, 2)) + "pg/mL")
        #print ("Fat: " + str(round(fat_total)) + "g total, " + str(round(fat_nonessential)) + "g nonessential, " + str(round(fat_essential)) + "g essential")
        print ("Metabolic activity level: " + str(round(metabolic_rate, 4)))
        print ("")

        #Make graphs using bokeh
        if len(bgDataX) >= 100:
            #bgGraph = Line(bgData[0, 100], title="Blood Glucose", legend="top_left", xlabel = 'Time', ylabel='Blood Glucose (mg/dL)')
            bgGraph = figure()#x_axis_type="datetime")
<<<<<<< HEAD
            bgGraph.line(bgDataX[0,100], bgDataY[0,100], color = "black")
            bgGraph.circle(bgDataX[0,100], bgDataY[0,100], fill_color = "white", line_color = "black", size = 8)
            bgGraph.circle(ROC_predictionX[0,6], ROC_predictionY[0,6], fill_color = "white", line_color = "gray", size = 8)
=======
            bgGraph.line(bgDataX[-100:], bgDataY[-100:], color = "black")
            bgGraph.circle(bgDataX[-100:], bgDataY[-100:], fill_color = "white", line_color = "black", size = 8)
>>>>>>> origin/master
            #bgGraph.circle(bgNormDataX[0,100], bgNormDataY[0,100], fill_color = "white", line_color = "black", size = 8)
            #bgGraph.circle(bgHighDataX[0,100], bgNormDataY[0,100], fill_color = "white", line_color = "yellow", size = 8)
            #bgGraph.circle(bgLowDataX[0,100], bgLowDataY[0,100], fill_color = "white", line_color = "red", size = 8)
            bgGraph.title.text = "Blood Glucose"
            bgGraph.xaxis.axis_label = "Time"
            bgGraph.yaxis.axis_label = "Blood Glucose (mg/dL)"
            #bgGraph.yaxis.bounds = (0, 400)

        else:
            #bgGrpah = Line(bgData, title="Blood Glucose", legend="top_left", xlabel = 'Time', ylabel='Blood Glucose (mg/dL)')
            bgGraph = figure()#x_axis_type="datetime")
            bgGraph.line(bgDataX, bgDataY, color = "black")
            bgGraph.circle(bgDataX, bgDataY, fill_color = "white", line_color = "black", size = 8)
            bgGraph.circle(ROC_predictionX, ROC_predictionY, fill_color = "white", line_color = "gray", size = 8)
            #bgGraph.circle(bgNormDataX, bgNormDataY, fill_color = "white", line_color = "black", size = 8)
            #bgGraph.circle(bgHighDataX, bgNormDataY, fill_color = "white", line_color = "yellow", size = 8)
            #bgGraph.circle(bgLowDataX, bgLowDataY, fill_color = "white", line_color = "red", size = 8)
            bgGraph.title.text = "Blood Glucose"
            bgGraph.xaxis.axis_label = "Time"
            bgGraph.yaxis.axis_label = "Blood Glucose (mg/dL)"
            #bgGraph.yaxis.bounds = (0, 400)

        
        if len(insulinDataX) >= 100:
            #insulinGraph = Line(insulinData[0, 100], title = "Insulin concentration", xlabel = "Time", ylabel = "Insulin Concentration (uU/mL)")
            insulinGraph = figure()#x_axis_type="datetime")
            insulinGraph.line(insulinDataX[-100:], insulinDataY[-100:], color = "CadetBlue")
            insulinGraph.circle(insulinDataX[-100:], insulinDataY[-100:], fill_color = "white", line_color = "CadetBlue", size = 8)
            insulinGraph.title.text = "Insulin"
            insuinGraph.xaxis.axis_label = "Time"
            insulinGraph.yaxis.axis_label = "Blood Insulin (μU/mL)"
            #insulinGraph.yaxis.bounds = (0, 400)

        else:
            #insulinGraph = Line(insulinData, title = "Insulin concentration", xlabel = "Time", ylabel = "Insulin Concentration (uU/mL)")
            insulinGraph = figure()#x_axis_type="datetime")
            insulinGraph.line(insulinDataX, insulinDataY, color = "CadetBlue")
            insulinGraph.circle(insulinDataX, insulinDataY, fill_color = "white", line_color = "CadetBlue", size = 8)
            insulinGraph.title.text = "Insulin"
            insulinGraph.xaxis.axis_label = "Time"
            insulinGraph.yaxis.axis_label = "Blood Insulin (μU/mL)"
            #insulinGraph.yaxis.bounds = (0, 400)

        if len(glucagonDataX) >= 100:
            #glucagonGraph = Line(glucagonData[0, 100], title = "Glucagon concentration", xlabel = "Time", ylabel = "Insulin Concentration (uU/mL)")
            glucagonGraph = figure()#x_axis_type="datetime"
            glucagonGraph.line(glucagonDataX[-100:], glucagonDataY[-100:], color = "GoldenRod")
            glucagonGraph.circle(glucagonDataX[-100:], glucagonDataY[-100:], fill_color = "white", line_color = "GoldenRod", size = 8)
            glucagonGraph.title.text = "Glucagon"
            glucagonGraph.xaxis.axis_label = "Time"
            glucagonGraph.yaxis.axis_label = "Blood Glucagon (pg/mL)"
            #glucagonGraph.yaxis.bounds = (0, 700)

        else:
            #glucagonGraph = Line(glucagonData, title = "Insulin concentration", xlabel = "Time", ylabel = "Insulin Concentration (uU/mL)")
            glucagonGraph = figure()#x_axis_type="datetime")
            glucagonGraph.line(glucagonDataX, glucagonDataY, color = "GoldenRod")
            glucagonGraph.circle(glucagonDataX, glucagonDataY, fill_color = "white", line_color = "GoldenRod", size = 8)
            glucagonGraph.title.text = "Glucagon"
            glucagonGraph.xaxis.axis_label = "Time"
            glucagonGraph.yaxis.axis_label = "Blood Glucagon (pg/mL)"
            #glucagonGraph.yaxis.bounds = (0, 700)
        
        #Combine the blood glucose, insulin, and glucagon graphs into a grid
        #grid = gridplot([bgGraph, insulinGraph, glucagonGraph], ncols=2, plot_width=600, plot_height=350)

        grid = layout([
          [bgGraph],
          [insulinGraph, glucagonGraph],
          [widgetbox(ROC_widget)],
        ], sizing_mode='stretch_both')

        #Write the graphs to an HTML file and display the grid containing them
        output_file('infoGraph.html')



        #GET USER COMMAND

        command = str(input(">"))

        if command == "set blood glucose ":
            glucose_blood = float(input("New blood glucose: "))

        if command == "set insulin":
            insulin_blood = float(input("New insulin level: "))

        if command == "set glucagon":
            glucagon_blood = float(input("New glucagon level: "))

        if command == "set glycogen_liver":
            glycogen_liver = float(input("New hapatic glycogen level: "))

        if command == "set glycogen_muscles":
            glycogen_muscles = float(input("New muscular glycogen level: "))

        if command == "set fat_total":
            fat_total = float(input("New total fat: "))

        if command == "set fat_nonessential":
            fat_nonessential = float(input("New nonessential fat: "))

        if command == "set fat_essential":
            fat_essential = float(input("New essential fat: "))

        if command == "set metabolic_rate":
            metabolic_rate = float(input("New metabolic activity level: "))

        if command == "set blood_volume":
            blood_volume = float(input("New blood volume: "))

        if command == "show":
            show(grid)

        if command == "exit":
            if input("Are you sure you want to exit? (y/n)") == "y":
                sys.exit()
            else:
                command()

        if command == "show":
            show(grid)

        if command == "help":
            print("SIMULATION CONTROL")
            print("-----------------------")
            print("set bg - set new value for blood glucose level")
            print("set insulin - set new value for blood insulin level")
            print("set glucagon - set new value for blood glucagon level")
            print("set glycogen_liver - set new value for glycogen in liver")
            print("set glycogen_muscles - set new value for glycogen in muscles")
            print("set metabolic_rate - set metabolic activity level")
            print("")
            print("OTHER")
            print("----------------------")
            print("help - show this menu")
            print("exit - exit the program")
<<<<<<< HEAD
            print("show - display graphs")
=======
            print("show - display the graphs")
>>>>>>> origin/master
            print("")
            os.system('pause')

#Start the program!
sim()