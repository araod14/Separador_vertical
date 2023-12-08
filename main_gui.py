from tkinter import *
import math


def veloper(k,densliq,densgas):
    vg=k*((densliq-densgas)/densgas)**0.5
    return vg  

def emparejador(valorpar):
    if round(valorpar) % 2== 0:
        valorpar=round(valorpar)
        return valorpar
    else:
        valorpar=round(valorpar+1)
    return valorpar
"""
#ingreso de informacion
densgas=3.699 #Densidad del gas - Lb/pie3 (libra por pie cubico)
densliq=45.630 #Densidad del liquido -
viscogas=0.013 #Viscocidad del gas -cP (Centi poise)
viscoliq=0.125#Viscocidad del liquido -cP (Centi poise)
z=0.85 #Factor de compresibilidad Z
flustandgas=80 # Flujo estandar del gas - MMPCED
flustandliq=80 #Flujo del liquido bbl/d
presop=random.randint(600,700) #Presion de operacion - PSIG
temop=random.randint(50,70) #Temperatura de operacion - °C
"""

def run():
	#ingreso de informacion
    densgas = float(entrydengas.get()) #Densidad del gas - Lb/pie3 (libra por pie cubico)
    densliq = float(entrydenliq.get()) #Densidad del liquido -
    viscogas = float(entryvisgas.get()) #Viscocidad del gas -cP (Centi poise)
    viscoliq = float(entryvisliq.get())#Viscocidad del liquido -cP (Centi poise)
    z = float(entryfact.get())
    flustandgas = float(entryflujgas.get()) # Flujo estandar del gas - MMPCED
    flustandliq = float(entryflujliq.get()) #Flujo del liquido bbl/d
    presop = float(entrypreop.get()) #Presion de operacion - PSIG
    temop = float(entrytemp.get()) #Temperatura de operacion - °C

	#convertir los flujos estandar a reales
    flujgas=(14.7*flustandgas*z*11.57407*(temop+460))/((presop+14.7)*(77+460))
    flujliq=flustandliq/20517.6917

	#eterminar velocidad critica
    relamas=flujliq*densliq/flustandgas*densgas*11.67407
    if (relamas<0.1):
	    vg=veloper(0.35,densliq,densgas)
    elif (relamas<1 and relamas>0.1):
	    vg=0.25
    else:
        vg=0.20

	#determinacion de area y diametro
    dipulg=(math.ceil(((4*flujgas/vg)/3.1416)**0.5))*12
    di=dipulg/12

	#altura entre tangente y hbbl, volumen de retencion
    htanbbl=9        #altura
    tiemope=30*60    #tiempo de operacion 30 minutos

	#altura bbl a bl, igual a h3
    h1=flujliq*300/(3.141596*((di)**2)/4)
    h1=math.ceil(h1*12)  #altura

	#altura bajo alto
    h2=flujliq*tiemope/(3.141596*((di)**2)/4)
    h2=math.ceil(h2*12)

	#calculo de boquillas

	#Boquilla de entrada
    dpc=math.ceil(((144*4*(flujgas+flujliq))/(3.141596*(60/((((1-(flujliq/(flujliq+flujgas)))*densgas)+((flujliq/(flujliq+flujgas))*densliq))**0.5))))**0.5)
    dpc=emparejador(dpc) #estan en pulgadas

    dlc=math.ceil(((4*flujliq)/(3.141596*0.25))**0.5)
    dlc=emparejador(dlc) #Boquilla de liquido

    dgasc=((144*4*flujgas)/(3.141596*(60/(densgas**0.5))))**0.5
    dgasc=emparejador(dgasc) #boquilla de gas

	#altura entre naal y boquilla
    hnalboq=dpc

	#alltura entre boquilla y malla
    hpr=0.5*dipulg
    if (hpr>24):
    	hboqmall=math.ceil(hpr)
    else:
    	hboqmall=24
	#alltura entre malla y tan
    hprt=0.15*dipulg
    if (hprt>16):
    	hmalltan=math.ceil(hprt)
    else:
    	hmalltan=16

    hmall=6
    leff=hmall+hboqmall+hmalltan+dipulg+(h1*2)+h2+htanbbl
    rel=leff/dipulg
	
	#Iteracion
    while rel<2.5: 
    	tiemope=tiemope+60
    	h2=flujliq*tiemope/(3.141596*((di)**2)/4)
    	h2=math.ceil(h2*12)
    	leff=hmall+hboqmall+hmalltan+dipulg+(h1*2)+h2+htanbbl
    	rel=leff/dipulg

    tiemopem=tiemope/60    

    labeldpgas.config(text="Dp="+str(dgasc))
    labelltiempo.config(text="Tiempo de \n residencia:" + str(tiemopem))
    labeldi.config(text=("D="+str(dipulg)))
    labelld.config(text="L/D="+str(rel))
    labellar.config(text="L="+str(leff))
    labeldboqe.config(text="Dp="+str(dpc))
    labelnaal.config(text=str(h1))
    labelnal.config(text=str(h2))
    labelnbl.config(text=str(h1))
    labelnbbl.config(text=str(htanbbl))
    labeldi.config(text="D="+str(dipulg))
    labeldpliq.config(text="Dp="+str(dlc))

    labelmalltan.config(text="16")
    labelboqmall.config(text="24")
    labelmall.config(text="6")
    labelnaalboq.config(text=str(dpc))
  
  
if __name__ == '__main__':
	# GUI
    ventana=Tk()
    ventana.title("Calculo dimensiones Separador Vertical segun norma PDVSA")
    ventana.geometry("800x550")
    ventana.config(bg="white")

    frame=Frame()
    frame.pack(anchor="s")
    frame.config(width="780", height="530", bg="white")

    #Titulo
    titulo=Label(frame, text="Separador Vertical segun norma PDVSA")
    titulo.config(bg="white",fg="red",fon=("arial black",20))
    titulo.place(x=80,y=15)

    #diagrama separador
    diagrama=PhotoImage(file="Disep.png")
    labeldiagrama=Label(frame, image=diagrama)
    labeldiagrama.place(x=450, y=80)

    #Entradas
    labeldengas=Label(frame, text="Densidad del gas, (Lb/Pie3)")
    labeldengas.place(x=10, y=80)
    labeldengas.config(bg="white",fon=("arial",11))
    entrydengas=Entry(frame)
    entrydengas.pack()
    entrydengas.config(width="6", bg="grey", fon=("arial",11))
    entrydengas.place(x=390, y=80)

    labeldenliq=Label(frame, text="Densidad del liquido, (Lb/Pie3)")
    labeldenliq.place(x=10, y=110)
    labeldenliq.config(bg="white",fon=("arial",11))
    entrydenliq=Entry(frame)
    entrydenliq.pack()
    entrydenliq.config(width="6", bg="grey", fon=("arial",11))
    entrydenliq.place(x=390, y=110)

    labelvisgas=Label(frame, text="Viscocidad del Gas, (cP)")
    labelvisgas.place(x=10, y=140)
    labelvisgas.config(bg="white",fon=("arial",11))
    entryvisgas=Entry(frame)
    entryvisgas.pack()
    entryvisgas.config(width="6", bg="grey", fon=("arial",11))
    entryvisgas.place(x=390, y=140)

    labelvisliq=Label(frame, text="Viscocidad del liquido, (cP)")
    labelvisliq.place(x=10, y=170)
    labelvisliq.config(bg="white",fon=("arial",11))
    entryvisliq=Entry(frame)
    entryvisliq.pack()
    entryvisliq.config(width="6", bg="grey", fon=("arial",11))
    entryvisliq.place(x=390, y=170)

    labelfact=Label(frame, text="Factor de compresibilidad Z")
    labelfact.place(x=10, y=230)
    labelfact.config(bg="white",fon=("arial",11))
    entryfact=Entry(frame)
    entryfact.pack()
    entryfact.config(width="6", bg="grey", fon=("arial",11))
    entryfact.place(x=390, y=230)

    labelflujgas=Label(frame, text="Flujo Volumetrico de Gas, (MMPCED)")
    labelflujgas.place(x=10, y=260)
    labelflujgas.config(bg="white",fon=("arial",11))
    entryflujgas=Entry(frame)
    entryflujgas.pack()
    entryflujgas.config(width="6", bg="grey", fon=("arial",11))
    entryflujgas.place(x=390, y=260)

    labelflujliq=Label(frame, text="Flujo Volumetrico de Liquido, (BPD)")
    labelflujliq.place(x=10, y=290)
    labelflujliq.config(bg="white",fon=("arial",11))
    entryflujliq=Entry(frame)
    entryflujliq.pack()
    entryflujliq.config(width="6", bg="grey", fon=("arial",11))
    entryflujliq.place(x=390, y=290)

    labelpreop=Label(frame, text="Presion de Operacion, (PSIG)")
    labelpreop.place(x=10, y=320)
    labelpreop.config(bg="white",fon=("arial",11))
    entrypreop=Entry(frame)
    entrypreop.pack()
    entrypreop.config(width="6", bg="grey", fon=("arial",11))
    entrypreop.place(x=390, y=320)

    labeltemp=Label(frame, text="Temperarura de Operacion, (F)")
    labeltemp.place(x=10, y=350)
    labeltemp.config(bg="white",fon=("arial",11))
    entrytemp=Entry(frame)
    entrytemp.pack()
    entrytemp.config(width="6", bg="grey", fon=("arial",11))
    entrytemp.place(x=390, y=350)

    #Boton correr
    boton01=Button(frame, text="Calcular", command=run)
    boton01.pack()
    boton01.config(fon=("arial",11))
    boton01.place(x=330,y=470)

    #Etiquetas de resultados
    labeldpgas=Label(frame)
    labeldpgas.config(bg="white",fon=("arial",11))
    labeldpgas.place(x=640,y=100)

    labelmalltan=Label(frame)
    labelmalltan.config(bg="white",fon=("arial",11))
    labelmalltan.place(x=520,y=187)

    labelboqmall=Label(frame)
    labelboqmall.config(bg="white",fon=("arial",11))
    labelboqmall.place(x=520,y=245)

    labelmall=Label(frame)
    labelmall.config(bg="white",fon=("arial",11))
    labelmall.place(x=690,y=215)

    labeldboqe=Label(frame)
    labeldboqe.config(bg="white",fon=("arial",11))
    labeldboqe.place(x=473,y=279)

    labelnaalboq=Label(frame)
    labelnaalboq.config(bg="white",fon=("arial",11))
    labelnaalboq.place(x=520,y=309)

    labellar=Label(frame)
    labellar.config(bg="white",fon=("arial",11))
    labellar.place(x=690,y=279)

    labelltiempo=Label(frame)
    labelltiempo.config(bg="white",fon=("arial",11))
    labelltiempo.place(x=449,y=102)

    labelnaal=Label(frame)
    labelnaal.config(bg="white",fon=("arial",9))
    labelnaal.place(x=685,y=340)

    labelnal=Label(frame)
    labelnal.config(bg="white",fon=("arial",9))
    labelnal.place(x=685,y=372)

    labelnbl=Label(frame)
    labelnbl.config(bg="white",fon=("arial",9))
    labelnbl.place(x=685,y=392)

    labelnbbl=Label(frame,)
    labelnbbl.config(bg="white",fon=("arial",9))
    labelnbbl.place(x=685,y=412)

    labelenaal=Label(frame, text="NAAL")
    labelenaal.config(bg="white",fon=("arial",8))
    labelenaal.place(x=635,y=340)

    labelenal=Label(frame, text="NAL")
    labelenal.config(bg="white",fon=("arial",9))
    labelenal.place(x=635,y=372)

    labelenbl=Label(frame, text="NBL")
    labelenbl.config(bg="white",fon=("arial",9))
    labelenbl.place(x=635,y=392)

    labelenbbl=Label(frame, text="NBBL")
    labelenbbl.config(bg="white",fon=("arial",9))
    labelenbbl.place(x=635,y=412)

    labeldi=Label(frame)
    labeldi.config(bg="white",fon=("arial",11))
    labeldi.place(x=594,y=510)

    labeldpliq=Label(frame)
    labeldpliq.config(bg="white",fon=("arial",11))
    labeldpliq.place(x=644,y=480)

    labelld=Label(frame)
    labelld.config(bg="white",fon=("arial",11))
    labelld.place(x=474,y=420)

    #Menu
    menubar=Menu(ventana)
    ventana.config(menu=menubar)

    filemenu=Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Archivo", menu=filemenu)
    filemenu.add_command(label="Nuevo")
    filemenu.add_separator()
    filemenu.add_command(label="Guardar")
    filemenu.add_command(label="Cerrar")

    editmenu=Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Editar", menu=editmenu)
    editmenu.add_command(label="Copiar")
    editmenu.add_command(label="Cortar")
    editmenu.add_command(label="Pegar")

    acercamenu=Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Acerca", menu=acercamenu)
    acercamenu.add_command(label="Ayuda")
    acercamenu.add_separator()
    acercamenu.add_command(label="Acerca de")

    ventana.mainloop() 