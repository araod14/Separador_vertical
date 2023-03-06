# Design of a vertical separator

Given the following liquid and gas values, 
this script will design the dimensions and alarm levels of 
a vertical separator according to the **PDVSA MDP-02-S-03 standard**

## Information input
-densgas=3.699 			**Gas density - Lb/ft3** \newline
-densliq=45.630 		**Liquid Density - Lb/ft3**\newline
-viscogas=0.013 		**Gas viscosity -cP (Centi poise)**\newline
-viscoliq=0.125			**Liquid Viscosity -cP (Centi poise)**\newline
-z=0.85 						**Gas Z Factor**\newline
-flustandgas=80 			**Standard Gas Flow - MMPCED**\newline
-flustandliq=80 			**Liquid Flow bbl/d**\newline
-presop=600 				**Pressure - PSIG**\newline
-temop=50 					**Temperature - °C**\newline

## Output

Es un separador Vertical con malla, la entrada es simple con codo de 90°
	Cada distancia esta en pulgadas y el tiempo de residencia en minutos
	Esta basado en el manual de diseño de separadores norma PDVSA MDP-02-S-03
			           _______________
			          (     	        )_
			          |		            __  Boquilla de 
			          |		            |   salida de gas: 10 	
		Malla	      #################    
			          |		            |		          Tiempo de
			          |		            |   Diametro del          residencia: 182.0  minutos 			
			          |		            |   recipiente: 60 	    	
			         _|		            |   Altura del            Relacion L/D: 2.5 
	Boquilla de  _			          |   recipiente: 150 
	entrada: 10  	|		            |
			          |		            |   Altura HHL: 1 
			          |		            |   Altura HL: 27 
			          |		            |   Altura LL: 1 
			          |		            |_  Altura LLL: 9 
			          |		            __  Boquilla de
			          (_______________)   salida liquido: 2 

		Todas las distancias se muestran en pulgadas
	Temperatura de operacion= 57 
	Presion de operacion= 649 
	""")   
