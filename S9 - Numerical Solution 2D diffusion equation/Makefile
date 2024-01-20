all: ecuacion_de_calor_0.png ecuacion_de_calor_1.png ecuacion_de_calor_2.png ecuacion_de_calor_3.png 

ecuacion_de_calor_0.png: difusion.txt PLOTS_S9CASA_EDP.py
	python PLOTS_S9CASA_EDP.py

ecuacion_de_calor_1.png: difusion.txt PLOTS_S9CASA_EDP.py
	python PLOTS_S9CASA_EDP.py

ecuacion_de_calor_2.png: difusion.txt PLOTS_S9CASA_EDP.py
	python PLOTS_S9CASA_EDP.py

ecuacion_de_calor_3.png: difusion.txt PLOTS_S9CASA_EDP.py
	python PLOTS_S9CASA_EDP.py

difusion.txt: a.out
	./a.out

a.out: S9CASA_EDP.cpp
	g++ S9CASA_EDP.cpp
