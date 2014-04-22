#!/usr/bin/python
def fix( p,q,n):
	global sud,stack1
	global top,hi
	for i in range(q,9):
		if(sud[p][i]==n):
			return 1

	for i in range(q,9):
		z=0
		if(sud[p][i]!=0):
			continue
		for j in range(9):
			if(sud[j][i]==n):
				z=1
				break
		if (p<3 and i<3):
			s,t,u,v = 0,2,0,2
		elif (p<3 and (i<6 and i>2)):
			s,t,u,v = 0,2,3,5
		elif (p<3 and (i<9 and i>5)):
			s,t,u,v = 0,2,6,8
		elif ((p>2 and p<6) and i<3):
			s,t,u,v = 3,5,0,2
		elif ((p>2 and p<6) and (i>2 and i<6)):
			s,t,u,v = 3,5,3,5
		elif ((p>2 and p<6) and (i<9 and i>5)):
			s,t,u,v = 3,5,6,8
		elif((p>5 and p<9)  and i<3):
			s,t,u,v = 6,8,0,2
		elif((p>5 and p<9) and (i>2 and i<6)):
			s,t,u,v = 6,8,3,5
		else:
			s,t,u,v = 6,8,6,8
		for x in range(s,(t+1)):
			for y in range(u,(v+1)):
				if(sud[x][y]==n):
					z=1
					break
		if(z==0):
			push(p,i,n)
			return 1
	return 0


def push(i, j, n):
	global sud,stack1
	global top,hi
	hi += 1
	top += 1;
	stack1[top][0]=i
	stack1[top][1]=j
	stack1[top][2]=n
	sud[i][j]=n
	return 0


def display():
	global sud,stack1
	global top,hi
	for i in range(9):
		for j in range(9):
			print (sud[i][j]),
		print


if __name__ == "__main__":
	top=-1
	hi=0
	sud = [[0,0,0,0,0,0,0,0,0] for y in range(9)]
	stack1 = [[None,None,None] for z in range(1000)]
	while True:
		a = raw_input("Do you want to enter the and postion in SUDOKU then enter y")
		if (a == 'y' or a == 'Y'):
			b = int(input("enyer the position of x"))
			c = int(input("enter the position of y"))
			d = int(input("enter the value"))
			sud[b][c]=d
		else:
			break
	for i in range(10):
		p,q=0,0
		while(p<9):
			check=fix(p,q,i)
			if(check==1):
				p += 1
				q=0
			else:
				p=stack1[top][0]
				q=stack1[top][1]
				i=stack1[top][2]
				top=top-1
				sud[p][q]=0
				q += 1
				hi -= 1
	display()
	for f in range(9):
		if 0 in sud[f]:
			print "baised output for baised input"



