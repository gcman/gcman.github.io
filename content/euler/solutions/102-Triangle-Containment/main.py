# Written by Gautam Manohar

count = 0
with open("triangles.txt","r") as f:
	for line in f:
		p1,p2,p3,p4,p5,p6 = map(int,line.split(","))
		if abs((p1-p5)*(p4-p2) - (p1-p3)*(p6-p2))/2 == (abs(p1*p4-p3*p2)+abs(p1*p6-p2*p5)+abs(p3*p6-p4*p5))/2:
			count += 1
print(count)