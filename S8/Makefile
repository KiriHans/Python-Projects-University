all: ecuacion_de_onda_tiempo_0.png ecuacion_de_onda_tiempo_3.33333e-05.png ecuacion_de_onda_tiempo_0.0252333.png ecuacion_de_onda_tiempo_0.0585667.png ecuacion_de_onda_tiempo_0.0810333.png ecuacion_de_onda_tiempo_0.1.png ecuacion_de_onda_2_tiempo_0.0002.png ecuacion_de_onda_2_tiempo_0.0452.png ecuacion_de_onda_2_tiempo_0.png ecuacion_de_onda_3_tiempo_0.1.png ecuacion_de_onda_3_tiempo_0.0252333.png ecuacion_de_onda_3_tiempo_0.0585667.png ecuacion_de_onda_3_tiempo_0.0810333.png ecuacion_de_onda_3_tiempo_0.png ecuacion_de_onda_3_tiempo_3.33333e-05.png

ecuacion_de_onda_tiempo_0.png: ecuacion_de_onda_1.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py

ecuacion_de_onda_tiempo_3.33333e-05.png: ecuacion_de_onda_1.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py

ecuacion_de_onda_tiempo_0.0252333.png: ecuacion_de_onda_1.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py

ecuacion_de_onda_tiempo_0.0585667.png: ecuacion_de_onda_1.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py

ecuacion_de_onda_tiempo_0.0810333.png: ecuacion_de_onda_1.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py

ecuacion_de_onda_tiempo_0.1.png: ecuacion_de_onda_1.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py


ecuacion_de_onda_2_tiempo_0.0002.png: ecuacion_de_onda_2.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py

ecuacion_de_onda_2_tiempo_0.0452.png: ecuacion_de_onda_2.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py

ecuacion_de_onda_2_tiempo_0.png: ecuacion_de_onda_2.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py


ecuacion_de_onda_3_tiempo_0.1.png: ecuacion_de_onda_3.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py

ecuacion_de_onda_3_tiempo_0.0252333.png: ecuacion_de_onda_3.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py

ecuacion_de_onda_3_tiempo_0.0585667.png: ecuacion_de_onda_3.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py

ecuacion_de_onda_3_tiempo_0.0810333.png: ecuacion_de_onda_3.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py

ecuacion_de_onda_3_tiempo_0.png: ecuacion_de_onda_3.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py

ecuacion_de_onda_3_tiempo_3.33333e-05.png: ecuacion_de_onda_3.txt PLOTS_S9C1_EDP.py
	python PLOTS_S9C1_EDP.py

ecuacion_de_onda_1.txt: a.out
	./a.out

ecuacion_de_onda_2.txt: a.out
	./a.out

ecuacion_de_onda_3.txt: a.out
	./a.out

a.out: S9C1_EDP.cpp
	g++ S9C1_EDP.cpp
