all: aleatorios.png aleatorios_con_impares.png

aleatorios.png: datos1.txt S6CASA_repasoC.py
	python S6CASA_repasoC.py

aleatorios_con_impares.png: datos1.txt datos2.txt S6CASA_repasoC.py
	python S6CASA_repasoC.py

datos1.txt datos2.txt: a.out
	./a.out

a.out: S6CASA_repasoC.cpp
	g++ -o S6CASA_repasoC.cpp


