#Diabetes/Body Energy Simulation Project
#
#Most of this is going to be either psuedocode, or just information.
#I'll start actual programming and organizing more things into variables
#when I get what I need figured out.


'''
So basically, I need to implement a few things:
    1. Primary Energy System/Glycolysis - Body uses ingested glucose from food.
    
    1.5 Liver Glycolysis - Body uses glycogen from the liver.
    
    2. Auxiliary Energy System/Ketosis - Body breaks down stored fat.
    Doing too much of this will lead to ketoacidosis. You are starving.
    
    3. Muscle breakdown (myosis?) - Body breaks down muscle tissue. Doing too
    much of this will lead to severe atrophy of the muscles.
    You are starving to death.
    
    4.Hormones - Effect how energy is used. Probably will include hormones
    like epinephirine, norepinephrine and cortisol. I probably spelled the
    first two wrong but w/e.
'''

def startSim():
    #PATIENT INFO
    #----------------------
    #Sex: Female
    #Weight: 156lb
    #Body fat percentage: 10%
    #Weight from fat: 15.6lb
    #Body fat in grams: 7076g
    #
    #
    #
    #
    #Initialize the patient's virtual "body."
    #
    #These variables are based off of:
    #For things that need to be replenished constantly (like glucose), the
    #reccomended daily intake value.
    #
    #For things that are relatively stable in terms of use (like fat), the
    #average amount or percent present in a person
    #
    #The weight of 156lb is average for an american human female.
    #Glucose assumes 275g of carb is ingested every day.
    #This is average for a human.
    #
    #Glycogen assumes about 100g of glycogen is stored in the liver.
    #This is average for a human.
    #
    #Insulin assumes about 10g of insulin is stored in the pancreas.
    #This is estimated.
    #
    #Glucagon assumes about 10g of glucagon is stored in the pancreas.
    #This is estimated.
    #
    #Fat assumes about 10% of body weight is fat.
    #This is average for a human female.
    
    glucose = 275
    glycogen = 100
    insulin = 10
    glucagon = 10
    fat = 7067
    
    