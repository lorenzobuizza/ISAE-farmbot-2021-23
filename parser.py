#Antoine

with open('plan.txt') as f:
	lines = f.read()
	f.close()
    

index = lines.find("step")
lines = lines[index:]
#return -1 if string does not exist

# spliting the big string into a list using a 
# separator the return to line
list = lines.split("\n")
#print(list)

length = len(list)

for i in range(length):
	list[i] = list[i][11:]
	
list = list[:length-10]

length = len(list)


with open('sequence.txt', 'w') as f:
    
    # counter variable used to count the cmds
    #i have to pay attention for the place of point
    # take before 3 spaces and then see if it is a space then delete more
    
    for i in range(length):
        
        if list[i].find("MOVE ROBOT") != (-1) :
            
            tmp_str =list[i]
            tmp_str = tmp_str[len(tmp_str)-3:]
            if tmp_str[0]==' ':
                tmp_str = tmp_str[1:]
            letter = tmp_str[0]
            if letter == 'A':
                
                point = tmp_str[1:]
                tmp_line = "self.id = bot.move_absolute(x ="\
                    + letter+ "[" + point + "]"+"[0], y=" + letter+"[" \
                        + point + "][1], z="+letter+ "[" + point + "][2])"\
                        + "\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' +"\n"
                f.write(tmp_line)
                
                
        elif list[i].find("TAKE-IMAGE") != -1:
            #tmp_line = "self.id = bot.take_photo()\n"\
            #+'print("TAKE_PHOTO REQUEST ID: " + self.id)'+"\n"
            #f.write(tmp_line)
            print("a")
            
            
        elif list[i].find("DISMOUNT-SEED-INJECTOR") != -1:
            
            tmp_line = "self.id = bot.move_absolute(x=B[3][0]+150, y=B[3][1], z=B[3][2])"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            
            tmp_line = "self.id = bot.move_absolute(x=B[3][0], y=B[3][1], z=B[3][2],speed = 50)"\
            +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            
            tmp_line = "self.id = bot.move_absolute(x=B[3][0], y=B[3][1], z=B[3][2]+200)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            
            
        elif list[i].find("MOUNT-SEED-INJECTOR") != -1:
            
            tmp_line = "self.id = bot.move_absolute(x=B[3][0], y=B[3][1], z=B[3][2] + 100) \n"\
                +'print("MOVE_ABS REQUEST ID: " + self.id)'  +"\n"		 
            f.write(tmp_line)
            
            
            tmp_line ="self.id = bot.move_absolute(x=B[3][0], y=B[3][1], z=B[3][2],speed=50)\n"\
                +'print("MOVE_ABS REQUEST ID: " + self.id)' +"\n"
            f.write(tmp_line)
            
            tmp_line = "self.id = bot.move_absolute(x=B[3][0]+150, y=B[3][1], z=B[3][2],speed=50)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' +"\n"
            f.write(tmp_line)
            
            tmp_line = "self.id = bot.move_absolute(x=B[3][0]+150, y=B[3][1], z=B[3][2]+200)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' +"\n"
            f.write(tmp_line)
            
            
        elif list[i].find("GRAB-SEED") != -1:
            
            tmp_line = "self.id = bot.move_absolute(x=B[5][0], y=B[5][1], z=B[5][2]+200)" \
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            
            
            tmp_line = "self.id = bot.move_absolute(x=B[5][0], y=B[5][1], z=B[5][2]+25)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            
            tmp_line = "self.id = bot.write_pin(9,1)"\
                +"\n"+'print("TOGGLE VACUUM: " + self.id)'+"\n"
            f.write(tmp_line)
            
            tmp_line = "self.id = bot.move_absolute(x=B[5][0], y=B[5][1], z=B[5][2],speed = 50)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            
            tmp_line = "self.id = bot.move_absolute(x=B[5][0], y=B[5][1], z=B[5][2]+200)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' + "\n"
            f.write(tmp_line)
            
            
        elif list[i].find("INJECT-SEED") != -1:
            
            tmp_str =list[i]
            finder = tmp_str.find("A")
            if tmp_str[finder+2]==' ':
                point = tmp_str[finder+1]
            else:
                point = tmp_str[finder+1]
                point = point +tmp_str[finder+2]
            
            tmp_line = "self.id = bot.move_absolute(x=A["+point+"][0], y=A["+point+"][1], z=A["+point+"][2])"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' +"\n"
            f.write(tmp_line)
    
            tmp_line = "self.id = bot.move_absolute(x=A["+point+"][0], y=A["+point+"][1], z=A["+point+"][2]-190)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' + "\n"
            f.write(tmp_line)
            
            tmp_line = "self.id = bot.write_pin(9,0)"\
                +"\n"+ 'print("TOGGLE VACUUM: " + self.id)'+"\n"
            f.write(tmp_line)
            
            tmp_line = "self.id = bot.move_absolute(x=A["+point+"][0], y=A["+point+"][1], z=A["+point+"][2])"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' + "\n"
            f.write(tmp_line)
            
            
        elif list[i].find("DISMOUNT-WEEDER") != -1:
            tmp_line = "self.id = bot.move_absolute(x=B[2][0]+150, y=B[2][1], z=B[2][2])"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            
            tmp_line = "self.id = bot.move_absolute(x=B[2][0], y=B[2][1], z=B[2][2],speed = 50)"\
            +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            tmp_line ="self.id = bot.move_absolute(x=B[2][0], y=B[2][1], z=B[2][2]+200)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            
            
        elif list[i].find("MOUNT-WEEDER") != -1:
            tmp_line ="self.id = bot.move_absolute(x=B[2][0], y=B[2][1], z=B[2][2] + 100)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.move_absolute(x=B[2][0], y=B[2][1], z=B[2][2],speed = 50)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.move_absolute(x=B[2][0]+150, y=B[2][1], z=B[2][2],speed = 50)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' + "\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.move_absolute(x=B[2][0]+150, y=B[2][1], z=B[2][2]+200)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+ "\n"
            f.write(tmp_line)
            
            
        elif list[i].find("ELIMINATE-WEED") != -1:
            
            tmp_str =list[i]
            finder = tmp_str.find("WEED")
            if tmp_str[finder+7]==' ':
                point = tmp_str[finder+6]
            else:
                point = tmp_str[finder+6]
                point = point + tmp_str[finder+7]
            
            tmp_line = "self.id = bot.move_absolute(x=A["+point+"][0], y=A["+point+"][1], z=A["+point+"][2])"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' +"\n"
            f.write(tmp_line)
            
            tmp_line = "self.id = bot.move_absolute(x=A["+point+"][0], y=A["+point+"][1], z=A["+point+"][2]-190)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' + "\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.move_absolute(x=A["+point+"][0], y=A["+point+"][1], z=A["+point+"][2])"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' + "\n"
            f.write(tmp_line)
            
        elif list[i].find("DISMOUNT-SOILSENSOR") != -1:
            tmp_line = "self.id = bot.move_absolute(x=B[0][0]+150, y=B[0][1], z=B[0][2])"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.move_absolute(x=B[0][0], y=B[0][1], z=B[0][2],speed = 50)"\
            +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            tmp_line ="self.id = bot.move_absolute(x=B[0][0], y=B[0][1], z=B[0][2]+200)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            
        elif list[i].find("MOUNT-SOILSENSOR") != -1:
            tmp_line ="self.id = bot.move_absolute(x=B[0][0], y=B[0][1], z=B[0][2] + 100)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            
            tmp_line = "self.id = bot.move_absolute(x=B[0][0], y=B[0][1], z=B[0][2],speed=50)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.move_absolute(x=B[0][0]+150, y=B[0][1], z=B[0][2],speed = 50)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' + "\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.move_absolute(x=B[0][0]+150, y=B[0][1], z=B[0][2]+200)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+ "\n"
            f.write(tmp_line)
            
        elif list[i].find("DISMOUNT-WATERNOZZLE") != -1:
            tmp_line = "self.id = bot.move_absolute(x=B[1][0]+150, y=B[1][1], z=B[1][2])"\
                 +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.move_absolute(x=B[1][0], y=B[1][1], z=B[1][2],speed = 50)"\
             +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.move_absolute(x=B[1][0], y=B[1][1], z=B[1][2]+200)"\
                 +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
        
            
        elif list[i].find("MOUNT-WATERNOZZLE") != -1:
            tmp_line = "self.id = bot.move_absolute(x=B[1][0], y=B[1][1], z=B[1][2] + 100)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.move_absolute(x=B[1][0], y=B[1][1], z=B[1][2],speed=50)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+"\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.move_absolute(x=B[1][0]+150, y=B[1][1], z=B[1][2],speed = 50)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' + "\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.move_absolute(x=B[1][0]+150, y=B[1][1], z=B[1][2]+200)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)'+ "\n"
            f.write(tmp_line)
            
            
        elif list[i].find("TAKE-DATA") != -1:
            tmp_str =list[i]
            finder = tmp_str.find("WATER")
            if tmp_str[finder+10]==' ':
                point = tmp_str[finder+9]
            else:
                point = tmp_str[finder+9]
                point = point+tmp_str[finder+10]
            
            tmp_line = "self.id = bot.move_absolute(x=A["+point+"][0], y=A["+point+"][1], z=A["+point+"][2])"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' +"\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.move_absolute(x=A["+point+"][0], y=A["+point+"][1], z=A["+point+"][2]-190)"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' +"\n"
            f.write(tmp_line)
            tmp_line = 'self.id = bot.read_pin(59,pin_mode="analog")'\
                +"\n"+'print("READING SOIL SENSOR REQUEST ID: " + self.id)' + "\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.move_absolute(x=A["+point+"][0], y=A["+point+"][1], z=A["+point+"][2])"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' + "\n"
            f.write(tmp_line)
            
        # using the space after "WATER " to differentiate it from MOUNT-WATERNOZZLE WATERINGNOZZLE
        elif list[i].find("IRRIGATE") != -1:
            tmp_str =list[i]
            if tmp_str[13]==' ':
                point = tmp_str[12]
            else:
                point = tmp_str[12]
                point = point +tmp_str[13]
            
            tmp_line = "self.id = bot.move_absolute(x=A["+point+"][0], y=A["+point+"][1], z=A["+point+"][2])"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' +"\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.write_pin(8,1)"\
                +"\n"+"self.id = bot.move_absolute(x=A["+point+"][0], y=A["+point+"][1]+30, z=A["+point+"][2])"\
                +"\n"+"self.id = bot.move_absolute(x=A["+point+"][0], y=A["+point+"][1]-30, z=A["+point+"][2])"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' +"\n"\
                +"self.id = bot.move_absolute(x=A["+point+"][0], y=A["+point+"][1], z=A["+point+"][2])"\
                +"\n"+'print("MOVE_ABS REQUEST ID: " + self.id)' +"\n"
            f.write(tmp_line)
            tmp_line = "self.id = bot.write_pin(8,0)"+"\n"+'print("Finishing irrigating " + self.id)' +"\n"
            f.write(tmp_line)
            
            
            
            
    
    f.close()
    
    

