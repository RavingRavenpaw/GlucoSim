import os
import sys
import platform
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.pyplot import *

#Diabetes/Body Energy Simulation Project

#My docs
#http://diatribe.org/issues/55/thinking-like-a-pancreas
#http://www.ncbi.nlm.nih.gov/pubmed/16441980
#http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3714432/
#http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3248697/
#https://www.diabeteshealth.com/insulin-to-carbohydrate-ratios/
#http://www.austincc.edu/apreview/EmphasisItems/Glucose_regulation.html
#file:///C:/Users/chrom/Downloads/FSI_insulin.pdfNN
#http://www.fsijournal.org/article/S0379-0738(00)00298-X/abstract
#
#https://www.drugs.com/pro/glucagon.html
#https://www.drugs.com/pro/novolog-injection.html


#Mayer Docs
#http://www.jstor.org/stable/1736097?seq=1#page_scan_tab_contents
#http://www.ncbi.nlm.nih.gov/books/NBK21190/
#http://diabetes.diabetesjournals.org/content/diabetes/49/12/2094.full.pdf
#http://www.jci.org/articles/view/106445


''' IMPLEMENTATION & PROGRAM INFO
So basically, I need to implement a few things:
    1. Primary Energy System/Respiration
    Body uses ingested glucose from food and stores some of it as glycogen
    in the liver.
    
    1.5  Glycogenolysis & Glycogenesis
    Liver releases glycogen and converts it to glucose or absorbs glucose and synthesizes glycogen.
    Glycogenolysis
    
    2. Auxiliary Energy System/Ketosis
    Body breaks down stored fat.
    Doing too much of this will lead to ketoacidosis if you are a diabetic. You are starving.
    
    3. Myolysis
    Body breaks down muscle tissue. Doing too much of this will lead to severe atrophy of the muscles.
    You are starving to death.
    
    4.Hormones
    Effect how energy is used. Probably will include hormoneslike epinephirine, norepinephrine
    and cortisol. I probably spelled the first two wrong but w/e.
'''

''' PATIENT INFO
    ----------------------
    Sex: Female
    Weight: 156lb / 70.76kg
    Height: 5' 11"
    Body fat percentage: 28%
    Weight from fat: 43.68lb / 19.813kg / 19,813g
    Essential fat: 4%
    Weight from essential fat: 6.24lb / 2.830kg / 2,830g
    Nonesssential fat: 16,983g
    Blood volume = 46.175dL or 4,617.5mL
'''

''' SCIENTIFIC BASIS OF VARIABLE VALUES

    These variables are based off of:
    For things that need to be replenished or synthesized constantly, they are
    based on an average non-diabetic fasting blood sugar.
    
    For things that are relatively stable in terms of use (like fat), they areNNN
    average amount or percent present in a person.
    
    The weight of 156lb is average for an american human female.
    Glucose assumes 275g of carb is ingested every day.
    This is average for a human.
    
    Glycogen assumes about 100g of glycogen is stored in the liver.
    This is average for a human.
    
    Insulin assumes about 15 μU/mL of insulin is present in the blood.
    This is average for a fasting human.
    
    Glucagon assumes about 1.2 mg/mL of glucagon is present in the blood.
    This is average for a fasting human.
    
    Fat assumes about 28% of body weight is fat and 4% is essential fat.
    This is average for a human female.
'''

''' UNITS & OTHER STATS
    --------------------
    1 IU insulin = 34.7 μg pure crystalline insulin
    1 IU glucagon = 1mg glucagon?


    BIC = Blood insulin concentration
    BGC = blood glucagon concentration

    Insulin concentration: μU/mL
    Glucagon concentration: pU/mL

    Fasting BIC: 15 - 40μU/mL = 8 - 15μU/mL
    Fasting BGC: 90 - 140pg/mL / 150pg/mL

    Mealtime BIC: ~80μU/mL?
    Mealtime BGC: ?

    Urgent low (~20mg/dL) BIC: ?
    Urgent low BGC: 500pg/mL
'''

#VARIABLE INITIALIZATION
global glucose_blood_level
glucose_blood_level = 100.0
#Glucose level/concentration of the blood in mg/dL

global glucose_blood
glucose_blood = 4617.5
#Glucose present in the blood in mg

global glycogen_liver
glycogen_liver = 100000
#Glycogen stored in the liver in mg

global glycogen_muscles
glycogen_muscles = 500000
#Glycogen stored in the muscles in mg

global insulin_blood
insulin_blood = 15.0
#Insulin present in the blood in μU/mL

global glucagon_blood
glucagon_blood = 20.00
#Glucagon present in the blood in in pg/mL

global carb_insulin_ratio
carb_insulin_ratio = 15000
#Amount of mg of carbohydrate that one unit of insulin will metabolize/cover

global glycogenolysis_ratio
glycogenolysis_ratio = 1
#Grams of glycogen that one unit/one pg of glucagon will release
#NOT FACTUAL, FOR SIMULATION TESTING PURPOSES ONLY

global glycogenesis_ratio
glycogenesis_ratio = 1
#Grams of glycogen that one gram of glucose will synthesize
#NOT FACTUAL, FOR SIMULATION TESTING PURPOSES ONLY

global glycogen_to_glucose_ratio
glycogen_to_glucose_ratio = 1
#Grams of glucose released from one gram of glycogen
#NOT FACTUAL, FOR SIMULATION TESTING PURPOSES ONLY

global fat_nonessential
fat_nonessential = 16983.0
#Nonessential (burnable) fat stored in adipose tissue in grams

global fat_essential
fat_essential = 2830.0
#Essential (non-burnable) fat stored in adipose tissue in grams

global fat_total
fat_total = 19813.0
#Total fat in adipose tissue in grams

global metabolic_rate
metabolic_rate = 3
#Number used to represent metabolic activity of the body
#NOT FACTUAL, FOR SIMULATION OF METABOLIC ACTIVITY
#TO ENHANCE REALISM OF SIMULATION ONLY

global blood_volume
blood_volume = 46.175
#Volume of blood in dL


#Lists for keeping past data on blood glucose level and insulin
#and glucagon concentrations.
global bgData
bgData = []

global bgDataX
bgDataX = []
global bgDataY
bgDataY = []

global bgNormDataX
bgNormDataX = []
global bgNormDataY
bgNormDataY = []
global bgHighDataX
bgHighDataX = []
global bgHighDataY
bgHighDataY = []
global bgLowDataX
bgLowDataX = []
global bgLowDataY
bgLowDataY = []
global insulinDataX
insulinDataX = []
global insulinDataY
insulinDataY = []
global glucagonDataX
glucagonDataX = []
global glucagonDataY
glucagonDataY = []

global currentTime
currentTime = 0

global timeData

timeData = []

#Initialize graph
plt.style.use('ggplot')
fig = plt.figure()
fig, (bgPlot, (insulinPlot, glucagonPlot)) = plt.subplots(nrows=2, ncols=2)
#fig.tight_layout()

bgPlot = fig.add_subplot(212)
bgPlot.plot(bgDataX, bgDataY, 'k-')
#plt.plot(str((bgNormData.keys())).replace("dict_keys", ""), 'ko')
bgPlot.plot(bgNormDataX, bgNormDataY, 'ko')
bgPlot.plot(bgLowDataX, bgLowDataY, 'ro')
bgPlot.plot(bgHighDataX, bgHighDataY, 'yo')
axes = plt.gca()
axes.set_ylim([0, 400])
plt.title('Blood Glucose')
plt.xlabel('Time')
plt.ylabel('Blood Glucose (mg/dL)')

insulinPlot = fig.add_subplot(222)
insulinPlot.plot(insulinDataX, insulinDataY, 'ko')
insulinPlot.plot(insulinDataX, insulinDataY, 'g-')
axes = plt.gca()
axes.set_ylim(0, 30000)
plt.title('Blood Insulin')
plt.xlabel('Time')
plt.ylabel('Blood Insulin Concentration (U/mL)')
  
glucagonPlot = fig.add_subplot(221)
glucagonPlot.plot(glucagonDataX, glucagonDataY, 'ko')
glucagonPlot.plot(glucagonDataX, glucagonDataY, 'b-')
axes = plt.gca()
axes.set_ylim(0, 800)
plt.title('Blood Glucagon')
plt.xlabel('Time')
plt.ylabel('Blood Glucagon Concentration (pU/dL)')
    
fig.show()

def calculateSimNumbers():
    global glucose_blood_level
    global glucose_blood
    global insulin_blood
    global glucagon_blood
    global glycogen_liver
    global glycogen_muscles
    global carb_insulin_ratio
    global glycogenolysis_ratio
    global glycogenesis_ratio
    global glycogen_to_glucose_ratio
    global fat_total
    global fat_essential
    global fat_nonessential
    global metabolic_rate
    global blood_volume

    global bgRateOfChange
    global ROC_arrows

    global bgData
    global bgDataX
    global bgDataY
    global bgNormDataX
    global bgNormDataY
    global bgHighDataX
    global bgHighDataY
    global bgLowDataX
    global bgLowDataY
    global insulinDataX
    global insulinDataY
    global glucagonDataX
    global glucagonDataY

    global currentTime
    
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

    bgDataX.append(currentTime)
    bgDataY.append(glucose_blood_level)

    if glucose_blood_level >= 80 and glucose_blood_level <= 180:
        #bgNormDataDict[currentTime] = glucose_blood_level
        bgNormDataX.append(currentTime)
        bgNormDataY.append(glucose_blood_level)

    if glucose_blood_level > 180:
         #bgHighDataDict[currentTime] = glucose_blood_level
         bgHighDataX.append(currentTime)
         bgHighDataY.append(glucose_blood_level)
    if glucose_blood_level < 80:
        #bgLowDataDict[currentTime] = glucose_blood_level
        bgLowDataX.append(currentTime)
        bgLowDataY.append(glucose_blood_level)


    if len(bgData) >=3:
        bgRateOfChange = ((bgData[-1] - bgData[-2]) + (bgData[-2] - bgData[-3]))/2
        #Steady
        if bgRateOfChange < 1 and bgRateOfChange > -1:
            #ROC_arrows = "→"
            ROC_arrows = "-> steady"

        #Rising
        if bgRateOfChange >= 1 and bgRateOfChange < 2:
            #ROC_arrows = "↗"
            ROC_arrows = "/^ slowly rising"
        if bgRateOfChange >= 2 and bgRateOfChange > 3:
            #ROC_arrows = "↑"
            ROC_arrows = "^|^ rising"
        if bgRateOfChange >= 3:
            #ROC_arrows = "⇈"
            ROC_arrows = "^|^ ^|^ rapidly rising"

        #Falling
        if bgRateOfChange <= -1 and bgRateOfChange > -2:
            #ROC_arrows = "↘"
            ROC_arrows = "\\v slowly falling"
        if bgRateOfChange <= -2 and bgRateOfChange > -3:
            #ROC_arrows = "↓"
            ROC_arrows = "v|v falling"
        if bgRateOfChange <= -3:
            #ROC_arrows = "⇊"
            ROC_arrows = "v|v v|v RAPIDLY FALLING /!\\"
    else:
        bgRateOfChange = 'N/A'
        ROC_arrows = ""
    
    glucagonDataX.append(currentTime)
    glucagonDataY.append(glucagon_blood)

    insulinDataX.append(currentTime)
    insulinDataY.append(insulin_blood)

    updateDisplay()

def updateDisplay():
    global glucose_blood_level
    global glucose_blood
    global insulin_blood
    global glucagon_blood
    global glycogen_liver
    global glycogen_muscles
    global carb_insulin_ratio
    global glycogenolysis_ratio
    global glycogenesis_ratio
    global glycogen_to_glucose_ratio
    global fat_total
    global fat_essential
    global fat_nonessential
    global metabolic_rate
    global blood_volume

    global bgRateOfChange

    global bgDataX
    global bgDataY
    global bgNormDataX
    global bgNormDataY
    global bgHighDataX
    global bgHighDataY
    global bgLowDataX
    global bgLowDataY
    global insulinDataX
    global insulinDataY
    global glucagonDataX
    global glucagonDataY

    global ROC_arrows

    if platform.system() == "Windows":
        os.system('cls')

    else:
        os.system("clear")

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
    
    #fig.clear()
    #fig.update()
    #plt.close("all")
    fig.show()

    command()

def command():
    global glucose_blood_level
    global glucose_blood
    global insulin_blood
    global glucagon_blood
    global glycogen_liver
    global glycogen_muscles
    global carb_insulin_ratio
    global glycogenolysis_ratio
    global glycogenesis_ratio
    global glycogen_to_glucose_ratio
    global fat_total
    global fat_essential
    global fat_nonessential
    global metabolic_rate
    global blood_volume


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

    if command == "exit":
        if input("Are you sure you want to exit? (y/n)") == "y":
            sys.exit()
        else:
            command()

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
        print("")
        os.system('pause')
    
    calculateSimNumbers()

#Initialize simulation
calculateSimNumbers()