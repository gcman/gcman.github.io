import numpy as np
import mpmath as mp
from math import sqrt

mp.dps = 100

tetrahedron = [[-1,-1,1],[-1,1,-1],[1,-1,-1],[1,1,1]]
rand_tet = list(np.random.rand(4,3))

def nullspace(A, atol=1e-13, rtol=0):
	A = np.atleast_2d(A)
	u, s, vh = np.linalg.svd(A)
	tol = max(atol, rtol * s[0])
	nnz = (s >= tol).sum()
	ns = vh[nnz:].conj().T
	return np.array([k[0] for k in ns])

def gen_cross(v):
	n = len(v)
	m = np.array([[v[i][j] for j in range(n+1)] for i in range(n)])
	return nullspace(m)

def insphere(v):
	n = len(v) - 1
	faces = []
	normals = []
	for i in range(n+1):
		faces.append(v + [v[n-i]])
		del faces[i][n-i]
	if n % 2 == 0:
		faces = list(reversed(faces))
	faces = np.array(faces)
	for f in faces:
		c = gen_cross([f[i] - f[0] for i in range(1,n)])
		unnormed = c * np.vdot(c, f[n] - f[0])
		normals.append((-1)**(n%2) * unnormed / np.linalg.norm(unnormed))
	A = np.array([[k[i] for i in range(n)] + [sum([k[i]**2 for i in range(n)])] for k in normals])
	B = np.array([sum([v[i][j]*normals[i][j] for j in range(n)]) for i in range(n+1)])
	return np.linalg.solve(A,B)

def circumsphere(v):
	n = len(v) - 1
	A = 2 * np.array([[v[0][j] - v[i][j] for j in range(n)] for i in range(1,n+1)])
	B = np.array([sum([v[0][j]**2 - v[i][j]**2 for j in range(n)]) for i in range(1,n+1)])
	sols = np.linalg.solve(A,B)
	R = sqrt(sum([(v[0][i] - sols[i])**2 for i in range(n)]))
	return np.append(sols, R)

def ratio(v): # Find the ratio of inradius and circumradius
	return mp.mpmathify(circumsphere(v)[-1])/mp.mpmathify(insphere(v)[-1])

with open("data.txt","w") as f:
	for d in range(2,101):
		inradius = 0
		circumradius = 0
		for i in range(1,10000):
			rand_tet = list(np.random.rand(d+1,d))
			inradius += mp.mpmathify(insphere(rand_tet)[-1])
			circumradius += mp.mpmathify(circumsphere(rand_tet)[-1])
			print(d, inradius, circumradius, circumradius/inradius)
		f.write(" ".join(map(str, [inradius, circumradius, circumradius/inradius])))