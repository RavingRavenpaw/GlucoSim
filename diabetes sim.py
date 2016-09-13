import os

#Diabetes/Body Energy Simulation Project
#
#Most of this is going to be either psuedocode, or just information.
#I'll start actual programming and organizing more things into variables
#when I get what I need figured out.

#http://diatribe.org/issues/55/thinking-like-a-pancreas

''' IMPLEMENTATION & PROGRAM INFO
So basically, I need to implement a few things:
    1. Primary Energy System/Respiration
    Body uses ingested glucose from food and stores some of it as glycogen
    in the liver.
    
    1.5  Glycogenolysis & Gluconeogenesis
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
    Weight: 156lb
    Body fat percentage: 10%
    Weight from fat: 15.6lb / 7.076kg / 7067g 
    
    

    Initialize the patient's virtual "body."
    
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
    
    Fat assumes about 10% of body weight is fat.
    This is average for a human female.
    
    
    OTHER STATS
    --------------------
    1 IU insulin = 34.7 μg pure crystalline insulin
    1 IU glucagon = 1mg glucagon
'''

#VARIABLE INITIALIZATION
global glucose_blood
glucose_blood = 100.0
#How much glucose is present in the blood in mg/dL

global glycogen_liver
glycogen_liver = 100.0
#How much glycogen is stored in the liver in grams

global glycogen_muscles
glycogen_muscles = 500.0
#How much glycogen is stored in the muscles in grams

global insulin_blood
insulin_blood = 15.0
#How much insulin is present in the blood in μU/mL

global glucagon_blood
glucagon_blood = 1.2
#How much glucagon is present in the blood in in mg/mL

global fat
fat = 7067
#How much fat is stored in adipose tissue in grams

global metabolic_rate
metabolic_rate = 0.25
#Number used to represent metabolic activity of the body
        
def sim():
    global glucose_blood
    global insulin_blood
    global glucagon_blood
    global glycogen_liver
    global glycogen_muscles
    global fat
    global metabolic_rate

    os.system('cls')

    glucose_blood = (glucose_blood - insulin_blood + (glucagon_blood*12.5) - (metabolic_rate))
    print ("Blood glucose: " + str(glucose_blood) + "mg/dL")
    print ("Hepatic glycogen: " + str(glycogen_liver) + "g")
    print ("Muscular glycogen: " + str(glycogen_muscles) + "g")
    print ("Blood insulin: " + str(insulin_blood) + "uU/mL")
    print ("Blood glucagon: " + str(glucagon_blood) + "mg/mL")
    print ("Fat: " + str(fat) + "g")
    print ("Metabolic activity level: " + str(metabolic_rate))
    print ("")
    if glucose_blood < 0.0:
        glucose_blood = 0.0

    command = str(input())

    if command == "set bg":
        glucose_blood = float(input("New blood glucose: "))

    if command == "set insulin":
        insulin_blood = float(input("New insulin level: "))

    if command == "set glucagon":
        glucagon_blood = float(input("New glucagon level: "))

    if command == "set glycogen_liver":
        glycogen_liver = float(input("New hapatic glycogen level: "))

    if command == "set glycogen_muscles":
        glycogen_muscles = float(input("New muscular glycogen level: "))
    sim()
sim()