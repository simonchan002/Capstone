from fairino import Robot
import time
# A connection is established with the robot controller. A successful connection returns a robot object
robot = Robot.RPC('192.168.58.2')
desc_pos7 = [236.794,-475.119, 65.379, -176.938, 2.535, -179.829]
# desc_pos8 = [236.794,-575.119, 165.379, -176.938, 2.535, -179.829]
# desc_pos9 = [236.794,-475.119, 265.379, -176.938, 2.535, -179.829]
tool = 0 #Tool number
user = 0 #Workpiece number
ret = robot.MoveCart(desc_pos7, tool, user)
print("Point-to-point motion in Cartesian space: ", ret)
# ret = robot.MoveCart(desc_pos8, tool, user, vel=30)
# print("Point-to-point motion in Cartesian space: ", ret)
# ret = robot.MoveCart(desc_pos9, tool, user,)
# print("Point-to-point motion in Cartesian space: ", ret)