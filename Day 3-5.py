# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:56:40 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def plantree (x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,46)
    mc.setBlocks(x,y,z,x,y+4,z,17)


x,y,z=mc.player.getTilePos()
for i in range(3):
    plantree(x+4*i,y,z)
    plantree(x,y,z+4*i)
    plantree(x+4,y,z+4*i)
    plantree(x+8,y,z+4*i)