import time
 
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
         
    def __exit__(self, type, value, traceback):
        print (" {:.3f} ".format(time.time() - self._startTime))
        
v=300
h=300
for vRis in range (2,50):
    hRis=vRis
    #vRis=int(input("height"))
    #hRis=int(input("width"))
    A=[[0]*v]*h
    ic=0;
    idd=0
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
          
            while mr<=m2 and nr>1:
                for id in range(m):
                    for jd in range(n):
                        s=0
                        for ii in range(m):
                            if ii>=idd:
                                ir=int((idd+(ii-idd)%mr)%m)
                            else:
                                ir=int((idd+(mr-(idd-ii)%mr))%m)
                            for jj in range(n):
                                if jj>=jd:
                                    jr=int((jd+(jj-jd)%nr)%n)
                                else:
                                    jr=int((jd+(nr-(jd-jj)%nr))%n)

                                if A[ii][jj]<A[ir][jr]:
                                    s+=A[ir][jr]-A[ii][jj]
                                        
                                if  A[ii][jj]>A[ir][jr] :
                                    s+=A[ii][jj]-A[ir][jr]
                                ic+=1   

                    ww=s
                    if ww<wmin :
                                mrmin=mr
                                nrmin=nr
                                idmin=idd
                                jdmin=jd
                                wmin=ww
                mr+=1
                nr-=1
                                   
                                   
