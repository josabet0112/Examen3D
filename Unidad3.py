import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt
import msvcrt
import sys

#____Coordenadas iniciales
xg=[]
yg=[]
zg=[]

#Cordenadas centrales
xc=80
yc=30
zc=30

#Plano y linea de sistema
x=[0,-40,40,0,-40,0]
y=[0,0,0,0,-20,-10]
z=[-10,10,10,-10,15,0]

for i in range(len(x)):
    xg.append(x[i]+xc)
    yg.append(y[i]+yc)
    zg.append(z[i]+zc)

#__Plotear el sistema 
#def plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
def plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
    plt.axis([0,150,100,0])
    plt.axis('on')
    plt.grid(False)
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='r')#plano
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='r')
    plt.plot([xg[2],xg[3]],[yg[2],yg[3]],color='r')
    plt.plot([xg[4],xg[5]],[yg[4],yg[5]],color='b')#Line

    if hitcolor=='g':# Do not touch hit point
        plt.scatter(xg[5],yg[5],s=20,color=hitcolor)
    else:
        plt.scatter(xhg,yhg,s=20,color=hitcolor)

    plt.show()

def hitpoint(x,y,z):
    #___distance point 4 to 5
    a=x[5]-x[4]
    b=y[5]-y[4]
    c=z[5]-z[4]
    Q45=sqrt(a*a+b*b+c*c) 
    # unit vector components point 4 to 5
    lx=a/Q45 
    ly=b/Q45
    lz=c/Q45
    #___distance point 0 to 3
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    Q03=sqrt(a*a+b*b+c*c) 
    # unit vector components point 0 to 3
    ux=a/Q03 #———unit vector 0 to 3
    uy=b/Q03
    uz=c/Q03
    #___distance point 0 to 1
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    Q01=sqrt(a*a+b*b+c*c)
    # unit vector components point 0 to 1
    vx=a/Q01 #———unit vector 0 to 1
    vy=b/Q01
    vz=c/Q01
    #___normal vector unit
    nx=uy*vz-uz*vy 
    ny=uz*vx-ux*vz
    nz=ux*vy-uy*vx
    #_____vector components 0 t0 4
    vx1b=x[4]-x[0]
    vy1b=y[4]-y[0]
    vz1b=z[4]-z[0]
    #__perpenticular distance 4 to plane
    Qn=(vx1b*nx+vy1b*ny+vz1b*nz)

    #___cos of angle p
    cosp=lx*nx+ly*ny+lz*nz

    #___distance 4 to hit point
    Qh=abs(Qn/cosp)

    #__Hit point coordinates
    xh=x[3]+Qh*lx
    yh=y[3]+Qh*ly
    zh=z[3]+Qh*lz

    #___global hit point coodinates
    xhg=xh+xc
    yhg=yh+yc
    zhg=zh+zc
    #____checar si la linea de 4 A 5 queda fuera de los valores del rectangulo
    #__Component of vector V0h
    a=xh-x[0]
    b=yh-y[0]
    c=zh-z[0]
    #dot products
    up=a*ux+b*uy+c*uz
    vp=a*vx+b*vy+c*vz
    #Si no estamos saliendo del plano del objeto rectangulo 
    hitcolor='r'
    if up<0:
        hitcolor='b'
    if up>Q03:
        hitcolor='b'
    if vp<0:
        hitcolor='b'
    if vp>Q01:
        hitcolor='r'
    
    #___Si el punto de 4 a 5 no alcanza el hit point
    a=x[5]-x[4]
    b=y[5]-y[4]
    c=z[5]-z[4]
    Q45=sqrt(a*a+b*b+c*c)
    if Q45 < Qh:
        hitcolor='g'
    return xh,yh,xhg,yhg,hitcolor 





def rotRx(xc, yc, zc, xp, yp, zp, Rx):
    a = [xp, yp, zp]
    b = [1, 0, 0]
    xpp = np.inner(a, b)
    b = [0, cos(Rx), -sin(Rx)]
    ypp = np.inner(a, b)
    b = [0, sin(Rx), cos(Rx)]
    zpp = np.inner(a, b)
    [xg, yg, zg] = [xpp+xc, ypp+yc, zpp+zc]
    return[xg, yg, zg]


def rotRy(xc, yc, zc, xp, yp, zp, Ry):
    a = [xp, yp, zp]
    b = [cos(Ry), 0, sin(Ry)]
    xpp = np.inner(a, b)
    b = [0, 1, 0]
    ypp = np.inner(a, b)
    b = [-sin(Ry), 0, cos(Ry)]
    zpp = np.inner(a, b)
    [xg, yg, zg] = [xpp+xc, ypp+yc, zpp+zc]
    return[xg, yg, zg]


def rotRz(xc, yc, zc, xp, yp, zp, Rz):
    a = [xp, yp, zp]
    b = [cos(Rz), -sin(Rz), 0]
    xpp = np.inner(a, b)
    b = [sin(Rz), cos(Rz), 0]
    ypp = np.inner(a, b)
    b = [0, 0, 1]
    zpp = np.inner(a, b)
    [xg, yg, zg] = [xpp+xc, ypp+yc, zpp+zc]
    return[xg, yg, zg]




def plotPlaneLinex(xc,yc,zc,Rx):
    for i in range(len(y)):
        [xg[i],yg[i],zg[i]]=rotRx(xc,yc,zc,x[i],y[i],z[i],Rx)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)
    plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor)

def plotPlaneLiney(xc,yc,zc,Ry):
    for i in range(len(y)):
        [xg[i],yg[i],zg[i]]=rotRy(xc,yc,zc,x[i],y[i],z[i],Ry)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)
    plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor)

def plotPlaneLinez(xc,yc,zc,Rz):
    for i in range(len(y)):
        [xg[i],yg[i],zg[i]]=rotRz(xc,yc,zc,x[i],y[i],z[i],Rz)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    xh,yh,xhg,yhg,hitcolor=hitpoint(x,y,z)
    plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor)
    

####_____pedir al usaurio que eje desea trabajar y plotear el PlaneLine
while True:
    axis=input("Teclea el eje que deseas visualizar 'x,y,z' o pulsa w para salir ?:")
    if axis=='x':#plotear el eje X
        Rx=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinex(xc,yc,zc,Rx)#LLamamos a la funcion de ploteo
    if axis=='y':
        Ry=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLiney(xc,yc,zc,Ry)#LLamamos a la funcion de ploteo
    if axis=='z':
        Rz=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinez(xc,yc,zc,Rz)#LLamamos a la funcion de ploteo
    if axis== 'w':
        break