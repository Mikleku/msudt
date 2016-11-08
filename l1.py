import time
import xlwt
from datetime import datetime
 
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
         
    def __exit__(self, type, value, traceback):
        print ("{:.3f}".format(time.time() - self._startTime))
        
font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.colour_index = 3
font0.bold = True

style0 = xlwt.XFStyle()
style0.font = font0

style1 = xlwt.XFStyle()
style1.num_format_str = 'D-MMM-YY'

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

for vRis in range(10,200):
    hRis=vRis
    print(hRis*vRis)
    #print(vRis*hRis)
    v=300
    h=300
    #vRis=int(input("height"))
    #hRis=int(input("width"))
    A=[[0]*v]*h
    ic=0;
    m=vRis;n=hRis;vRis2=vRis/2;hRis2=hRis/2;
    for i in range(m):
        ir=i%vRis2
        for j in range(n):
            jr=j%hRis2
            A[i][j]=int(ir+jr)
    #        print(A[i][j], end=" ")
    #    print("\n")
            
    n2=n/2; m2=m/2;pr=0; prmax=m/2+n/2;wmin=255*n*m;ww=0;s=0;
    mrmin=0;nrmin=0;idmin=0;jdmin=0;

    with Profiler() as p:
        for pr in range(4,int(prmax)):
            mr=2
            nr=pr-mr
            if nr>n2:
                nr=n2
                mr=pr-nr
            diff1=1
            while mr<=m2 and nr>1:
                for i in range(m):
                    ir=int(i%mr)
                    for j in range(n):
                        jr=int(j%nr)
                        ic=ic+1
                        exitFlag = False
                        if(A[i][j]!=A[ir][jr]):
                           exitFlag=True
                           break
                    if exitFlag:
                           break
                if not exitFlag:
                           diff=0
                           break
                else:
                           mr+=1
                           nr-=1
