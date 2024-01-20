all: euler_method.png runge-Kutta_method.png analitical_graph.png comparacion_euler_analitica.png comparacion_Runge-Kutta_analitica.png

euler_method.png: euler_array.txt PLOTS_S6C2_EDO_casa.py
	python PLOTS_S6C2_EDO_casa.py

runge-Kutta_method.png: euler_array.txt runge_array.txt PLOTS_S6C2_EDO_casa.py
	python PLOTS_S6C2_EDO_casa.py

analitical_graph.png: euler_array.txt runge_array.txt PLOTS_S6C2_EDO_casa.py
	python PLOTS_S6C2_EDO_casa.py

comparacion_euler_analitica.png: euler_array.txt runge_array.txt PLOTS_S6C2_EDO_casa.py
	python PLOTS_S6C2_EDO_casa.py

comparacion_Runge-Kutta_analitica.png: euler_array.txt runge_array.txt PLOTS_S6C2_EDO_casa.py
	python PLOTS_S6C2_EDO_casa.py

euler_array.txt: a.out
	./a.out

runge_array.txt: a.out
	./a.out

a.out: S6C2_EDO_casa.cpp
	g++ S6C2_EDO_casa.cpp
