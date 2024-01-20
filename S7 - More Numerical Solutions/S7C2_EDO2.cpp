#include <iostream>
#include <fstream>
#include <cmath>
#include <stdlib.h>

using namespace std;

double funcion(double anterior, double s)
{
  return -s*anterior;
}

double osciladorAmortiguado(double x, double v, double s, double b)
{
  
  return -s*x - b*v;
}



int main()
{

  // Método de Euler
  const int M = 1000;
  const double m = 0.2;
  const double k = 50;
  const double h = 0.001;
  const double s = k/m;


  double anteriorX = 0.1;
  double anteriorV = 0;
  double t = 0;

  ofstream MyFile("euler_array.txt");

  MyFile << 0 << " " << 0 << " " << 0.1 << "\n";


  for (int i = 0; i < M; i++)
  {
	double x_n = anteriorX + h * (anteriorV);
    double v_n = anteriorV + h * funcion(anteriorX, s);
    t = t + h;

    MyFile << t << " " << x_n << " " << v_n << "\n";
    
    anteriorX = x_n;
	anteriorV = v_n;
  };
  MyFile.close();

  // Método Runge-Kutta de 4to orden
  t = 0;
  
  double arr_terms_Runge[M];
  anteriorX = 0.1;
  anteriorV = 0;

  MyFile.open("runge_array.txt");
  MyFile << 0 << " " << 0 << " " << 0.1 << "\n";
  

  for (int i = 0; i < M; i++)
  {

    double k1 = h * (anteriorV);
	double l1 = h * funcion(anteriorX, s);
    double k2 = h * (anteriorV + k1 / 2);
	double l2 = h * funcion(anteriorX + l1 / 2, s);
    double k3 = h * (anteriorV + k2 / 2);
	double l3 = h * funcion(anteriorX + l2 / 2,s);
    double k4 = h * (anteriorV + k3);
	double l4 = h * funcion(anteriorX + l3, s);
    double x_n = anteriorX + (k1 + 2 * k2 + 3 * k3 + k4) / 6;
    double v_n = anteriorV + (l1 + 2 * l2 + 3 * l3 + l4) / 6;
    t = t + h;

    MyFile << t << "  " << x_n << " " << v_n << "\n";
    

    anteriorX = x_n;
	anteriorV = v_n;
  };
  MyFile.close();

  // Método Leap Frog

  t = 0;
  
 
  double anteriorY = 0.1;
  anteriorV = 0;
  double v_1_2 = anteriorV + (h * funcion(anteriorY, s))/2;


  MyFile.open("leapFrog_array.txt");
  MyFile << 0 << " " << 0 << " " << 0.1 << "\n";
  for(int i = 0; i < M; i++){
	double y_n = anteriorY + h*(v_1_2);
    double v_n = v_1_2 + h*funcion(y_n, s);
	t = t + h;

	MyFile << t << "  " << y_n << " " << v_n << "\n";
	
	anteriorY = y_n;
	v_1_2 = v_n;
  };
  MyFile.close();
  
  // Método Euler para un oscilador amortiguado

  const double b = 0.08;

  anteriorX = 0.1;
  anteriorV = 0;
  t = 0;

  MyFile.open("euler_amortiguado_array.txt");

  MyFile << 0 << " " << 0 << " " << 0.1 << "\n";
  

  for (int i = 0; i < M; i++)
  {
	double x_n = anteriorX + h * (anteriorV);
    double v_n = anteriorV + h * osciladorAmortiguado(anteriorX, anteriorV, s, b);
    t = t + h;

    MyFile << t << " " << x_n << " " << v_n << "\n";
    
    anteriorX = x_n;
	anteriorV = v_n;
  };
  MyFile.close();
  
}
