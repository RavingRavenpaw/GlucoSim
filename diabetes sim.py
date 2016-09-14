import os
import sys
import platform

#Diabetes/Body Energy Simulation Project
#
#Most of this is going to be either psuedocode, or just information.
#I'll start actual programming and organizing more things into variables
#when I get what I need figured out.

#http://diatribe.org/issues/55/thinking-like-a-pancreas
#http://www.ncbi.nlm.nih.gov/pubmed/16441980

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
    Body fat percentage: 28%
    Weight from fat: 43.68lb / 19.813kg / 19,813g
    Essential fat: 4%
    Weight from essential fat: 6.24lb / 2.830kg / 2,830g
    Nonesssential fat: 16,983g
    Blood volume = 46.175dL
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

''' OTHER STATS
    --------------------
    1 IU insulin = 34.7 μg pure crystalline insulin
    1 IU glucagon = 1mg glucagon
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
glucagon_blood = 1.2
#Glucagon present in the blood in in mg/mL

global carb_insulin_ratio
carb_insulin_ratio = 6000
#Amount of mg of carbohydrate that one unit of insulin will metabolize/cover

global glycogenolysis_ratio
glycogenolysis_ratio = 2
#Grams of glycogen that one unit/one mg of glucagon will release

global glycogenesis_ratio
glycogenesis_ratio = 4
#Grams of glucose that can synthesize one gram of glycogen

global glycogen_to_glucose_ratio
glycogen_to_glucose_ratio = 2
#Grams of glucose released from one gram of glycogen

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
metabolic_rate = 0.25
#Number used to represent metabolic activity of the body

global blood_volume
blood_volume = 46.175
#Volume of blood in dL


global current_OS
current_OS = platform.system()

def sim():
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

    if current_OS == "Windows":
        os.system('cls')

    else:
        os.system("clear")

    #glucose_blood_level = (glucose_blood_level - insulin_blood + (glucagon_blood*12.5) - (metabolic_rate))
    glucose_blood_level = ((glucose_blood - (carb_insulin_ratio*insulin_blood) + (glycogenolysis_ratio*glucagon_blood*glycogen_to_glucose_ratio))/blood_volume)
    glycogen_liver += (glucagon_blood*glycogenolysis_ratio)
    insulin_blood = insulin_blood - insulin_blood
    glucagon_blood = glucagon_blood - glucagon_blood

    if glucose_blood_level < 0.0:
        glucose_blood_level = 0.0
    print ("Diabetes/Body Energy Simulation Project")
    print ("2015 - 2016, created by John Kozlosky")
    print ("")
    print ("Blood glucose level: " + str(glucose_blood_level) + "mg/dL")
    print ("Blood glucose: " + str(glucose_blood) + "mg")
    print ("Glycogen: " + str(glycogen_liver) + "mg hepatic, " + str(glycogen_muscles) + "mg muscular")
    print ("Blood insulin: " + str(insulin_blood) + "uU/mL")
    print ("Blood glucagon: " + str(glucagon_blood) + "mg/mL")
    print ("Fat: " + str(fat_total) + "g total, " + str(fat_nonessential) + "g nonessential, " + str(fat_essential) + "g essential")
    print ("Metabolic activity level: " + str(metabolic_rate))
    print ("")

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
            sim()

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
    sim()
sim()