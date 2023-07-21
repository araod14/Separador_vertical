import math
import random


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


def run():
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

	print("""
	Es un separador Vertical con malla, la entrada es simple con codo de 90°
	Cada distancia esta en pulgadas y el tiempo de residencia en minutos
	Esta basado en el manual de diseño de separadores norma PDVSA MDP-02-S-03
			 _______________
			(	        )_
			|		__  Boquilla de 
			|		|   salida de gas:""",dgasc,"""	
		Malla	#################    
			|		|		          Tiempo de
			|		|   Diametro del          residencia:""",tiemopem,""" minutos 			
			|		|   recipiente:""",dipulg,"""	    	
			_|		|   Altura del            Relacion L/D:""",rel,"""
	Boquilla de   _			|   recipiente:""",leff,"""
	entrada:""",dpc,""" 	|		|
			|		|   Altura HHL:""",h1,"""
			|		|   Altura HL:""",h2,"""
			|		|   Altura LL:""",h1,"""
			|		|_  Altura LLL:""",htanbbl,"""
			|		__  Boquilla de
			(_______________)   salida liquido:""",dlc,"""

		Todas las distancias se muestran en pulgadas
	Temperatura de operacion=""",temop,"""
	Presion de operacion=""",presop,"""	
	""")   
  
if __name__ == '__main__':
	run()