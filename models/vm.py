import numpy as np

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

def sphere(x,y,z,R):
    return x*x + y*y + z*z <= R[0]*R[0]


VMSphere = buildVM(8,8,8, 2,2,2, sphere, 1)

VMCross = np.zeros( (3, 3, 3), dtype=int)
VMCross[0,1,1] = 1
VMCross[1,0,1] = 1
VMCross[1,1,0] = 1
VMCross[1,1,1] = 1
VMCross[1,1,2] = 1
VMCross[1,2,1] = 1
VMCross[2,1,1] = 1

