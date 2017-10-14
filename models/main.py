import numpy as np
#from s import *

#Define the function creating a Blender's voxel
import bpy

def make_voxel(loc=(0,0,0), dim=(1,1,1)):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    v = bpy.context.active_object
    v.dimensions = dim
    return v

def get_voxel_coordinates(i,j,k):
	return (i + 1/2, j + 1/2, k + 1/2)


def draw_voxel_model():
	for i in range(N):
		for j in range(M):
			for k in range(K):
				if V[i,j,k] == 1:
					make_voxel(loc=get_voxel_coordinates(i,j,k))

#Draw voxels in Blender
draw_voxel_model(V, N, M, K)

#In Blender:
#bpy.ops.object.delete()
#import sys
#sys.path.append('D:\\_SCIENCE\projects\models')
#import main

#3 - Обзор:
	#1. Какие виды спутниковых изображений есть
	#2. Как их можно получить

#4 - Think how to convert MM -> VM

#5 - git (GitHub) - make account, start using it
