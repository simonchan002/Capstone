from fairino import Robot
import time
# A connection is established with the robot controller. A successful connection returns a robot object
robot = Robot.RPC('192.168.58.2')
# desc_pos7 = [65.257, -380.686, 300, -180, 0, 0]
# desc_pos8 = [236.794,-575.119, 165.379, -176.938, 2.535, -179.829]
# desc_pos9 = [236.794,-475.119, 265.379, -176.938, 2.535, -179.829]
# tool = 0 #Tool number
# user = 0 #Workpiece number
# ret = robot.MoveCart(desc_pos7, tool, user, vel = 46)
# print("Point-to-point motion in Cartesian space: ", ret)
# ret = robot.MoveCart(desc_pos8, tool, user, vel=30)
# print("Point-to-point motion in Cartesian space: ", ret)
# ret = robot.MoveCart(desc_pos9, tool, user,)
# print("Point-to-point motion in Cartesian space: ", ret)


def PTP(x, y, z, speed):
    tool = 0
    user = 0
    desired_pos = [x, y, z, -180, 0, 0]
    ret = robot.MoveCart(desired_pos, tool, user, vel = speed)
    print("Point-to-point motion in Cartesian space: ", ret)


def ModbusRegWrite(param1, param2, param3, data, param4, param5):
    # Implementation needed - placeholder for Modbus communication
    pass


#total is defined as the total number of trays to scoop from in total

def pick(tray, current, total):
    speed = 45

    scoop_high_z = 300
    scoop_lower_z = 40

    # initial coordinates for the each tray (x1,y1 = tray 1 position)
    x1 = -700 
    y1 = 240
    x2 = -450
    y2 = 240
    x3 = 450
    y3 = 240

    if tray == 1:
        PTP(x1, y1, scoop_high_z, speed)
        time.sleep(1)  # WaitMs(100) converted to seconds
        PTP(x1, y1, scoop_lower_z, speed)
        # ModbusRegWrite(6, 128, 1, [8176], 1, 0)

    elif tray == 2:
        PTP(x2, y2, scoop_high_z, speed)
        time.sleep(1)  # WaitMs(100) converted to seconds
        PTP(x2, y2, scoop_lower_z, speed)
        # ModbusRegWrite(6, 128, 1, [8176], 1, 0)

    elif tray == 3:
        PTP(x3, y3, scoop_high_z, speed)
        time.sleep(1)  # WaitMs(100) converted to seconds
        PTP(x3, y3, scoop_lower_z, speed)
        # ModbusRegWrite(6, 128, 1, [8176], 1, 0)

    else: 
        PTP(x1, y1, scoop_high_z, speed)
        time.sleep(1)  # WaitMs(100) converted to seconds
        PTP(x1, y1, scoop_lower_z, speed)
        # ModbusRegWrite(6, 128, 1, [8176], 1, 0)

        PTP(x2, y2, scoop_high_z, speed)
        time.sleep(1)  # WaitMs(100) converted to seconds
        PTP(x2, y2, scoop_lower_z, speed)
        # ModbusRegWrite(6, 128, 1, [8176], 1, 0)

        PTP(x3, y3, scoop_high_z, speed)
        time.sleep(1)  # WaitMs(100) converted to seconds
        PTP(x3, y3, scoop_lower_z, speed)
        # ModbusRegWrite(6, 128, 1, [8176], 1, 0)



    picks = 1
    while picks <= total:
        if tray == 1:
            #move scooper to the right for the next scoop iteration
            x1 = x1 + 75 
            PTP(x1, y1, scoop_high_z, speed)
            time.sleep(1)  # WaitMs(100) converted to seconds
            PTP(x1, y1, scoop_lower_z, speed)
            # ModbusRegWrite(6, 128, 1, [8176], 1, 0)

        elif tray == 2:
            x2 = x2 + 75
            PTP(x2, y2, scoop_high_z, speed)
            time.sleep(1)  # WaitMs(100) converted to seconds
            PTP(x2, y2, scoop_lower_z, speed)
            # ModbusRegWrite(6, 128, 1, [8176], 1, 0)

        elif tray == 3:
            x3 = x3 + 75 
            PTP(x3, y3, scoop_high_z, speed)
            time.sleep(1)  # WaitMs(100) converted to seconds
            PTP(x3, y3, scoop_lower_z, speed)
            # ModbusRegWrite(6, 128, 1, [8176], 1, 0)
        picks += 1

    

# Example usage
if __name__ == "__main__":
    pick(3, 1, 3)