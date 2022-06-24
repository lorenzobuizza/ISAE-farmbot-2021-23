# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 16:11:29 2022

@author: Buizza
"""

from py2pddl import Domain, create_type
from py2pddl import predicate, action, goal, init




class Farmbot (Domain):
    Waypoint = create_type("Waypoint")#wp
    Robot = create_type ("Robot")#r
    Sample = create_type ("Sample")#s
    Seed = create_type ("Seed")#seed
    Weed = create_type ("Weed")#weed
    SeedBin = create_type ("SeedBin")#sb
    Camera = create_type("Camera")#c
    SoilSensor = create_type("SoilSensor")#ss
    SeedInj = create_type("SeedInjector")#sinj
    Weeder = create_type("Weeder")#wdr
    WateringNozzle = create_type("WateringNozzle")#wn
    
    
    
    
    
    #-------------------------------------PRECONDITIONS-------------------------------------
    @predicate (Sample, Waypoint)
    def is_in(self, s, wp):#a sample (a plant) is at a specific waypoint
        "complete"
    
    @predicate (Weed, Waypoint)
    def is_(self, weed, wp): #a weed (which we will remove) is at a specific waypoint
        "complete"
    
    @predicate (Robot, Waypoint)
    def at(self, r, wp): #the robot is at a specific waypoint
        "complete"
    
    @predicate (SoilSensor, Waypoint)
    def soilsensor_at(self, ss, wp): #the soil sensor is at a specific waypoint
        "complete"
    
    @predicate (SeedInj, Waypoint)
    def seedinj_at(self, sinj, wp): #the seed injector is at a specific waypoint
        "complete"
    
    @predicate (Weeder, Waypoint)
    def weeder_at(self, wdr, wp): #the weeder is at a specific waypoint
        "complete"
    
    @predicate (WateringNozzle, Waypoint)
    def waternozzle_at(self, wn, wp): #the water nozzle is at a specific waypoint
        "complete"
    
    @predicate (SeedBin, Waypoint)
    def seedbin_at(self, sb, wp): #the water nozzle is at a specific waypoint
        "complete"
    
    @predicate (Seed, Waypoint)
    def seed_at(self, seed, wp): #the water nozzle is at a specific waypoint
        "complete"
    
    @predicate (Sample)
    def taken_image (self, s): #the image of that specific sample (plant) has been taken
        "complete"
    
    @predicate (Sample)
    def taken_data_before_water(self, s): #the data of that specific sample (plant) has been taken before watering it
        "complete"
    
    @predicate (Sample)
    def taken_data_after_water(self, s): #the data of that specific sample (plant) has been taken after watering it
        "complete"
    
    @predicate (Seed, Waypoint)
    def seedinjected(self, seed, wp): #a specific seed has been injected in a specific waypoint
        "complete"
    
    @predicate (Sample)
    def samplewatered(self, s): #a specific sample has been watered
        "complete"
    
    @predicate (Waypoint)
    def empty_wayp (self, wp): #a waypoint is empty, so we can put a seed
        "complete"
    
    @predicate (Waypoint, Weed)
    def wayp_without_weed (self, wp, weed): #a waypoint, which had a weed, is now without the weed
        "complete"
    
    @predicate (SoilSensor)
    def carrying_SoilSensor (self, ss): #the robot is carrying the soil sensor
        "complete"
    
    @predicate (WateringNozzle)
    def carrying_WateringNozzle (self, wn): #the robot is carryint the watering nozzle
        "complete"
    
    @predicate (Weeder)
    def carrying_Weeder (self, wdr): #the robot is carring the weeder
        "complete"
    
    @predicate (SeedInj)
    def carrying_SeedInj (self, sinj): #the robot is carrying the seed injector
        "complete"
    
    @predicate (Robot)
    def no_tools_mounted (self, r): #the robot is not carrying any tool
        "complete"
    
    @predicate (Robot)
    def carrying_seed(self, r): #the robot is carrying a seed, which will be deposited in the soil
        "complete"
    
    
    
    
    #-----------------------------------------ACTIONS--------------------------------------------------
    @action(Robot, Waypoint, Waypoint)
    def move (self, r, wp1, wp2): #this action moves the robot from a waypoint to another
        precond: list = [self.at(r, wp1)]
        effect: list = [~self.at(r, wp1), self.at(r, wp2)]
        return precond, effect
    
    @action (Robot, Sample, Waypoint, Camera)
    def take_image (self, r, s, wp, c): #this action takes an image of a sample using the camera
        precond: list = [self.at(r, wp), self.is_in(s, wp)]
        effect: list = [self.taken_image(s)]
        return precond, effect
    
    @action(Seed, Waypoint, Robot, SeedInj)
    def grab_seed (self, seed, wp, r, sinj): #this action grabs a seed from the seed bin
        precond: list = [self.seed_at(seed, wp), self.at(r, wp), self.carrying_SeedInj(sinj), ~self.carrying_seed(r)]
        effect: list = [self.carrying_seed(r)]
        return precond, effect
    
    @action(Seed, Waypoint, Robot, SeedInj)
    def inject_seed ( self, seed, wp, r, sinj): #this action injects a seed at a waypoint
        precond: list = [self.empty_wayp (wp), self.at(r, wp), self.carrying_SeedInj(sinj), self.carrying_seed(r)]
        effect: list = [self.seedinjected(seed, wp), ~self.empty_wayp (wp), ~self.carrying_seed(r)]
        return precond, effect
    
    @action(Waypoint, Robot, Weeder, Weed)
    def eliminate_weed ( self, wp, r, wdr, weed): #this actions uses the weeder to eliminate a weed
        precond: list = [self.is_(weed, wp), self.at(r, wp), self.carrying_Weeder(wdr)]
        effect: list = [~self.is_(weed, wp), self.wayp_without_weed(wp, weed)]
        return precond, effect
    
    @action(Sample, Waypoint, Robot, SoilSensor)
    def take_data_before_water (self, s, wp, r, ss): #this action uses the soil sensor to take data of a sample (plant) in a waypoint, before watering it
        precond: list = [self.is_in(s, wp), self.at(r, wp), self.carrying_SoilSensor(ss), ~self.samplewatered(s)]
        effect: list = [self.taken_data_before_water(s)]
        return precond, effect
    
    @action(Sample, Waypoint, Robot, SoilSensor)
    def take_data_after_water (self, s, wp, r, ss): #this action uses the soil sensor to take data of a sample (plant) in a waypoint, before watering it
        precond: list = [self.is_in(s, wp), self.at(r, wp), self.carrying_SoilSensor(ss), self.samplewatered(s)]
        effect: list = [self.taken_data_after_water(s)]
        return precond, effect
    
    @action (Sample, Waypoint, Robot, WateringNozzle)
    def irrigate(self, s, wp, r, wn) : #this action waters a sample (plant) at a specific waypoint
        precond: list = [self.is_in(s, wp), self.at(r, wp), self.carrying_WateringNozzle(wn)]
        effect: list = [self.samplewatered(s)]
        return precond, effect
    
    @action (Waypoint, Robot, SeedInj)
    def mount_seed_injector(self, wp, r, sinj): #action to mount the Seed Injector
        precond: list = [self.seedinj_at(sinj, wp), self.at(r,wp), self.no_tools_mounted(r)]
        effect: list = [self.carrying_SeedInj(sinj), ~self.no_tools_mounted(r)]
        return precond, effect
    
    @action (Waypoint, Robot, SeedInj)
    def dismount_seed_injector(self, wp, r, sinj): #action to dismount the Seed Injector
        precond: list = [self.seedinj_at(sinj, wp), self.at(r,wp), self.carrying_SeedInj(sinj), ~self.no_tools_mounted(r) ,~self.carrying_seed(r)]
        effect: list = [~self.carrying_SeedInj(sinj), self.no_tools_mounted(r)]
        return precond, effect
    
    @action (Waypoint, Robot, Weeder)
    def mount_weeder(self, wp, r, wdr): #action to mount the Weeder
        precond: list = [self.weeder_at(wdr, wp), self.at(r,wp), self.no_tools_mounted(r)]
        effect: list = [self.carrying_Weeder(wdr), ~self.no_tools_mounted(r)]
        return precond, effect
    
    @action (Waypoint, Robot, Weeder)
    def dismount_weeder(self, wp, r, wdr): #action to dismount the Weeder
        precond: list = [self.weeder_at(wdr, wp), self.at(r,wp), self.carrying_Weeder(wdr), ~self.no_tools_mounted(r)]
        effect: list = [~self.carrying_Weeder(wdr), self.no_tools_mounted(r)]
        return precond, effect
    
    @action (Waypoint, Robot, SoilSensor)
    def mount_soilsensor(self, wp, r, ss): #action to mount the Soil Sensor
        precond: list = [self.soilsensor_at(ss, wp), self.at(r,wp), self.no_tools_mounted(r)]
        effect: list = [self.carrying_SoilSensor(ss), ~self.no_tools_mounted(r)]
        return precond, effect
    
    @action (Waypoint, Robot, SoilSensor)
    def dismount_soilsensor(self, wp, r, ss): #action to dismount the Soil Sensor
        precond: list = [self.soilsensor_at(ss, wp), self.at(r,wp), self.carrying_SoilSensor(ss), ~self.no_tools_mounted(r)]
        effect: list = [~self.carrying_SoilSensor(ss), self.no_tools_mounted(r)]
        return precond, effect
    
    @action (Waypoint, Robot, WateringNozzle)
    def mount_waternozzle(self, wp, r, wn): #action to mount the Watering Nozzle
        precond: list = [self.waternozzle_at(wn, wp), self.at(r,wp), self.no_tools_mounted(r)]
        effect: list = [self.carrying_WateringNozzle(wn), ~self.no_tools_mounted(r)]
        return precond, effect
    
    @action (Waypoint, Robot, WateringNozzle)
    def dismount_waternozzle(self, wp, r, wn): #action to dismount the Weeder
        precond: list = [self.waternozzle_at(wn, wp), self.at(r,wp), self.carrying_WateringNozzle(wn), ~self.no_tools_mounted(r)]
        effect: list = [~self.carrying_WateringNozzle(wn), self.no_tools_mounted(r)]
        return precond, effect





class MotionAndPictureProblem(Farmbot):
    def __init__(self):
        super().__init__()
        self.samples = Farmbot.Sample.create_objs(["A", "B", "C", "D", "E", "F", "G","H", "I"]) #we chose to have 9 samples (plants)
        self.seeds = Farmbot.Seed.create_objs(["seed1", "seed2", "seed3"]) #we chose to have 3 seeds
        self.weeds = Farmbot.Weed.create_objs(["weed1", "weed2"]) #we chose there are 2 weeds to remove
        self.robot = Farmbot.Robot.create_objs(["robot"])
        self.camera = Farmbot.Camera.create_objs(["camera"])
        self.seedinj = Farmbot.SeedInj.create_objs(["seedinj"])
        self.wateringnozzle = Farmbot.WateringNozzle.create_objs(["wateringnozzle"])
        self.weeder = Farmbot.Weeder.create_objs(["weeder"])
        self.soilsensor = Farmbot.SoilSensor.create_objs(["soilsensor"])
        self.seedbin = Farmbot.SeedBin.create_objs(["seedbin"])
        
        na = 18
        a = []
        coord_a =[[1000,615],
    	[1000,1315],
    	[1000,2015],
    	[1700,615],
    	[1700,1315],
    	[1700,2015],
    	[2400,615],
    	[2400,1315],
    	[2400,2015],
    	[3100,615],
    	[3100,1315],
    	[3100,2015],
    	[3800,615],
    	[3800,1315],
    	[3800,2015],
    	[4500,615],
    	[4500,1315],
    	[4500,2015]]
        
        nb = 7
        b = []
        coord_b =[[7.6,1361.6],  #soil sensor
	    [7.6,1462.6],            #watering nozzle
    	[7.6,1562.6],            #weeder
    	[7.6,1667.6],            #seeder
    	[7.6,1767.6],            #seed tray
    	[0,1867.6],              #seed bin
        [0,0]]                   #home
        
        for i in range(na):
            points_coord = (coord_a[i][0],coord_a[i][1])
            a.append(points_coord)
            
        for i in range(nb):
            points_coord = (coord_b[i][0],coord_b[i][1])
            b.append(points_coord)
        
        a0 = a[0]
        a1 = a[1] 
        a2 = a[2] 
        a3 = a[3]
        a4= a[4] 
        a5 = a[5] 
        a6 = a[6] 
        a7 = a[7]
        a8 = a[8]
        a9 = a[9]
        a10 = a[10]
        a11 = a[11]
        a12 = a[12]
        a13 = a[13]
        a14 = a[14]
        a15 = a[15]
        a16 = a[16]
        a17 = a[17]
        b0 = b[0] #soil sensor
        b1 = b[1] #watering nozzle
        b2 = b[2] #weeder
        b3 = b[3] #seeder
        b4 = b[4] #seed tray
        b5 = b[5] #seed bin
        b6 = b[6] #home
        
        self.waypoints = Farmbot.Waypoint.create_objs ( ["a0", "a1", "a2","a3", "a4", "a5", "a6", "a7","a8", "a9","a10","a11", "a12", "a13","a14","a15","a16","a17","b0","b1","b2","b3","b4","b5", "b6"])
        
    @init
    def init(self) -> list:
        at = [
            self.at(self.robot["robot"], self.waypoints["b6"]),
            self.soilsensor_at(self.soilsensor["soilsensor"], self.waypoints["b0"]),
            self.seedinj_at(self.seedinj["seedinj"], self.waypoints["b3"]),
            self.weeder_at(self.weeder["weeder"], self.waypoints["b2"]),
            self.waternozzle_at(self.wateringnozzle["wateringnozzle"], self.waypoints["b1"]),
            self.seedbin_at(self.seedbin["seedbin"], self.waypoints["b5"]),
            self.seed_at(self.seeds["seed1"], self.waypoints["b5"]),
            self.seed_at(self.seeds["seed2"], self.waypoints["b5"]),
            self.seed_at(self.seeds["seed3"], self.waypoints["b5"]),
            
            
            self.is_in(self.samples["A"], self.waypoints["a1"]),
            self.is_in(self.samples["B"], self.waypoints["a3"]),
            self.is_in(self.samples["C"], self.waypoints["a4"]),
            self.is_in(self.samples["D"], self.waypoints["a5"]),
            self.is_in(self.samples["E"], self.waypoints["a7"]),
            self.is_in(self.samples["F"], self.waypoints["a8"]),
            self.is_in(self.samples["G"], self.waypoints["a11"]),
            self.is_in(self.samples["H"], self.waypoints["a14"]),
            self.is_in(self.samples["I"], self.waypoints["a15"]),
            
            
            self.is_(self.weeds["weed1"], self.waypoints["a6"]),
            self.is_(self.weeds["weed2"], self.waypoints["a10"]),
            
            
            self.empty_wayp (self.waypoints ["a0"]),
            self.empty_wayp (self.waypoints ["a2"]),
            self.empty_wayp (self.waypoints ["a9"]),
            self.empty_wayp (self.waypoints ["a13"]),
            self.empty_wayp (self.waypoints ["a16"]),
            self.empty_wayp (self.waypoints ["a17"]),
            
            
            self.no_tools_mounted(self.robot["robot"]),
            ~self.carrying_seed(self.robot["robot"]),
        ]
        return at
    
    @goal
    def goal(self) -> list:
        return [
            self.at (self.robot["robot"], self.waypoints["b6"]),
            self.no_tools_mounted(self.robot["robot"]),
            
            self.taken_image(self.samples["A"]),
            self.taken_image(self.samples["B"]),
            self.taken_image(self.samples["C"]),
            self.taken_image(self.samples["D"]),
            self.taken_image(self.samples["E"]),
            self.taken_image(self.samples["F"]),
            self.taken_image(self.samples["G"]),
            self.taken_image(self.samples["H"]),
            self.taken_image(self.samples["I"]),
            
            self.taken_data_before_water(self.samples["A"]),
            self.taken_data_before_water(self.samples["B"]),
            self.taken_data_before_water(self.samples["C"]),
            self.taken_data_before_water(self.samples["D"]),
            self.taken_data_before_water(self.samples["E"]),
            self.taken_data_before_water(self.samples["F"]),
            self.taken_data_before_water(self.samples["G"]),
            self.taken_data_before_water(self.samples["H"]),
            self.taken_data_before_water(self.samples["I"]),
            
            self.samplewatered(self.samples["A"]),
            self.samplewatered(self.samples["B"]),
            self.samplewatered(self.samples["C"]),
            self.samplewatered(self.samples["D"]),
            self.samplewatered(self.samples["E"]),
            self.samplewatered(self.samples["F"]),
            self.samplewatered(self.samples["G"]),
            self.samplewatered(self.samples["H"]),
            self.samplewatered(self.samples["I"]),
            
            self.taken_data_after_water(self.samples["A"]),
            self.taken_data_after_water(self.samples["B"]),
            self.taken_data_after_water(self.samples["C"]),
            self.taken_data_after_water(self.samples["D"]),
            self.taken_data_after_water(self.samples["E"]),
            self.taken_data_after_water(self.samples["F"]),
            self.taken_data_after_water(self.samples["G"]),
            self.taken_data_after_water(self.samples["H"]),
            self.taken_data_after_water(self.samples["I"]),
            
            self.seedinjected(self.seeds["seed1"], self.waypoints["a13"]),
            self.seedinjected(self.seeds["seed2"], self.waypoints["a16"]),
            self.seedinjected(self.seeds["seed3"], self.waypoints["a9"]),
            
            self.wayp_without_weed(self.waypoints["a6"], self.weeds["weed1"]),
            self.wayp_without_weed(self.waypoints["a10"], self.weeds["weed2"]),
        ]
