import numpy as np

def new_VM(N, M, K, Lx, Ly, Lz, F, *a):
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

                if F(x,y,z,a):
                    VM[i,j,k] = 1
    return VM

def sphere(x,y,z,R):
    return x*x + y*y + z*z <= R[0]*R[0]

m = new_VM(5,5,5, 5,5,5, sphere, 5)
