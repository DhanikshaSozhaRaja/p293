from controller import Robot

robot=Robot()

timestep=320
flag=0

rpc=robot.getDevice("RPC")
rpf=robot.getDevice("RPF")
rmc=robot.getDevice("RMC")
rmf=robot.getDevice("RMF")
rac=robot.getDevice("RAC")
raf=robot.getDevice("RAF")
lpc=robot.getDevice("LPC")
lpf=robot.getDevice("LPF")
lmc=robot.getDevice("LMC")
lmf=robot.getDevice("LMF")
lac=robot.getDevice("LAC")
laf=robot.getDevice("LAF")

while(robot.step(timestep)!=-1):
    pass