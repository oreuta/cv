import numpy as np
import bpy
from math import sqrt

def buildVM(N, M, K, Lx, Ly, Lz, F, *parameters):
    dx, dy, dz = Lx/N, Ly/M, Lz/K
    xmin = -Lx/2
    ymin = -Ly/2
    zmin = -Lz/2

    VM = np.zeros( (N, M, K), dtype=int)

    for i in range(N):
        for j in range(M):
            for k in range(K):
                x = xmin + dx/2 + i*dx
                y = ymin + dy/2 + j*dy
                z = zmin + dz/2 + k*dz

                if F(x,y,z,parameters):
                    VM[i,j,k] = 1
    return VM

def sphere(x,y,z,params):
    R = params[0]
    return x*x + y*y + z*z - R*R <= 0

def torus(x,y,z,params):
    r = params[0]
    R = params[1]
    return pow(x*x+y*y+z*z+R*R-r*r,2) - 4*R*R*(x*x+y*y) <= 0

def make_voxel(loc=(0,0,0), dim=(1,1,1)):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    v = bpy.context.active_object
    v.dimensions = dim
    return v

def get_voxel_coordinates(i,j,k):
    return (i + 1/2, j + 1/2, k + 1/2)

def draw_voxel_model(V, N, M, K):
    for i in range(N):
        for j in range(M):
            for k in range(K):
                if V[i,j,k] == 1:
                    make_voxel(loc=get_voxel_coordinates(i,j,k))

#Draw voxels in Blender
N = M = K = 8

VMCross = np.zeros( (3, 3, 3), dtype=int)
VMCross[0,1,1] = 1
VMCross[1,0,1] = 1
VMCross[1,1,0] = 1
VMCross[1,1,1] = 1
VMCross[1,1,2] = 1
VMCross[1,2,1] = 1
VMCross[2,1,1] = 1

VMTorus = buildVM(N, M, K, 2,2,2, torus, 1, 0.1)
VMSphere = buildVM(N,M,K, 2,2,2, sphere, 1)

#draw_voxel_model(VMCross, 3,3,3)

draw_voxel_model(VMSphere, N, M, K)
#draw_voxel_model(VMTorus, N, M, K)
