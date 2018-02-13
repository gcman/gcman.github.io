import numpy as np
import mpmath as mp
from math import sqrt

mp.dps = 100

tetrahedron = np.array([[1,0,-1/sqrt(2)],[-1,0,-1/sqrt(2)],[0,1,1/sqrt(2)],[0,-1,1/sqrt(2)]])
rand_tet = np.random.rand(4,3)

def basis(n,i):
	a = np.zeros(n)
	a[i] = 1.0
	return a

def gen_cross(v):
	n = len(v)
	m = np.array([[v[i][j] for j in range(n+1)] for i in range(n)] + [[basis(n+1,i) for i in range(n+1)]], dtype=object)
	return np.linalg.det(m)

def insphere(v):
	n = len(v) - 1
	faces = [[v[i] for i in range(n+1) if i != j] + [v[j]] for j in range(n+1)]
	normals = []
	for f in faces:
		c = gen_cross([f[i] - f[0] for i in range(1,n)])
		unnormed = c * np.vdot(c, f[n+1] - f[0])
		normals.append(-unnormed / np.linalg.norm(unnormed))
	A = np.array([[[k[i][j] for k in normals] + [sum([v**2 for v in [k[i][j] for k in normals]])] for j in range(n)] for i in range(n+1)])
	B = np.array([sum([v[i][j]*normals[i][j] for j in range(n)]) for i in range(n+1)])
	return np.linalg.solve(A,B)

def circumsphere(v):
	n = len(v) - 1
	A = 2 * np.array([[v[0][j] - v[i+1][j] for j in range(n)] for i in range(n)])
	B = np.array([[v[0][j]**2 - v[i+1][j]**2 for j in range(n)] for i in range(n)])
	sols = np.linalg.solve(A,B)
	R = sqrt(sum([(v[0][j] - sols[j][0])**2 for j in range(n)]))
	return np.append(sols,[R])

def ratio(v): # Find the ratio of inradius and circumradius
	return mp.mpmathify(circumsphere(v)[3])/mp.mpmathify(insphere(v)[3])

print(ratio(tetrahedron))