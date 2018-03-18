import mpmath as mp

mp.dps = 2000

def func(x,n):
	out = 1
	for i in range(n):
		a = x/(2*i+1)
		out *= mp.sinc(a)
	return out

for i in range(1,8):
	mp.nprint(mp.quadosc(lambda x: func(x,i), [-mp.inf, mp.inf],omega=1) - mp.pi,1000)