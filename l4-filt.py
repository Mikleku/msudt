import random
import math
from PIL import Image, ImageDraw
mode = int(input('mode:'))  
image = Image.open("1.jpg") 
imageHSL= image.convert("HSV")
draw = ImageDraw.Draw(image)   
drawHSL = ImageDraw.Draw(imageHSL) 
width = image.size[0]  
height = image.size[1]  
pix = image.load()
pixHSL=imageHSL.load()

f=[[-1,-1,-1],
   [-1,9,-1],
   [-1,-1,-1]]
k=1;
  
#lighter
if (mode == 5):
    #inc=int(input("value:"))
    for i in range(1,width-1):
        for j in range(1,height-1):
            a = pixHSL[i, j][0]
            b = pixHSL[i, j][1]
            c = pixHSL[i, j][2]
            s=0
            for e in range (9):
                s+=pixHSL[ i + e // 3 - 1, j + e % 3 - 1][2] * f[e // 3][e % 3]
            
            drawHSL.point((i, j), (a,b,int(s*k)))


#lighter
if (mode == 0):
    inc=int(input("value:"))
    for i in range(width):
        for j in range(height):
            a = pixHSL[i, j][0]
            b = pixHSL[i, j][1]
            c = pixHSL[i, j][2]
            drawHSL.point((i, j), (a,b,c+inc))

#log
if (mode == 1):
    m=0;
    maxf=0
    minf=255
    for i in range(width):
        for j in range(height):
            a = pixHSL[i, j][0]
            b = pixHSL[i, j][1]
            c = pixHSL[i, j][2]
            m += c
            if (c>maxf):
                maxf=c
            if (c<minf):
                minf=c
    m = m /  (width * height)
    range1 = max(2,maxf-m)
    range2 = max(2,m-minf)
    alpha1=255 /  math.log(range1)
    alpha2=255 /  math.log(range2)

    for i in range(width):
        for j in range(height):
            a = pixHSL[i, j][0]
            b = pixHSL[i, j][1]
            c = pixHSL[i, j][2]
            
            bb = c - m;
            
            if (bb >= 1):
                dat = m + round(alpha1 * math.log(bb))
            if (bb <= -1):
                dat = m - round(alpha2 * math.log(abs(bb)))
            if (bb > -1 and bb < 1):
                dat = bb                 
            drawHSL.point((i, j), (a,b, round(dat)))
             
 

#negative
if (mode == 3):
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			draw.point((i, j), (255 - a, 255 - b, 255 - c))

#gray
if (mode == 2):
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			draw.point((i, j), (S, S, S))

image.save("ans.jpg", "JPEG")
imageHSL= imageHSL.convert("RGB")
imageHSL.save("ans1.jpg", "JPEG")
del draw
del drawHSL
