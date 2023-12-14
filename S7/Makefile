all: euler_method.png runge-Kutta_method.png analitical_graph.png leap-Frog_method.png euler_method_amortiguado.png

euler_method.png: euler_array.txt PLOTS_S7C2_EDO2.py
	python PLOTS_S7C2_EDO2.py

runge-Kutta_method.png: euler_array.txt runge_array.txt PLOTS_S7C2_EDO2.py
	python PLOTS_S7C2_EDO2.py

leap-Frog_method.png: euler_array.txt runge_array.txt leapFrog_array.txt PLOTS_S7C2_EDO2.py
	python PLOTSs_S7C2_EDO2.py

analitical_graph.png: euler_array.txt runge_array.txt leapFrog_array.txt PLOTS_S7C2_EDO2.py
	python PLOTS_S7C2_EDO2.py

euler_method_amortiguado.png: euler_array.txt runge_array.txt leapFrog_array.txt euler_amortiguado_array.txt PLOTS_S7C2_EDO2.py
	python PLOTS_S7C2_EDO2.py

euler_array.txt: a.out
	./a.out

runge_array.txt: a.out
	./a.out

leapFrog_array.txt: a.out
	./a.out

euler_amortiguado_array.txt: a.out
	./a.out

a.out: S7C2_EDO2.cpp
	g++ S7C2_EDO2.cpp
