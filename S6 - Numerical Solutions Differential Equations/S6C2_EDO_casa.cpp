#include <iostream>
#include <fstream>
#include <cmath>
#include <stdlib.h>

using namespace std;

double funcion(double anterior)
{
  return -(anterior);
}

double solucionAnalitica(double t)
{
  return exp(-t);
}

int main()
{

  // Método de Euler
  const int M = 1000;
  double arr_terms_Euler[M];
  double anterior = 1;
  const double h = 0.01;
  double t = 0;

  ofstream MyFile("euler_array.txt");

  MyFile << 0 << " " << 1 << "\n";
  arr_terms_Euler[0] = 1;

  for (int i = 0; i < M; i++)
  {
    double y_n = anterior + h * funcion(anterior);
    t = t + h;

    MyFile << t << " " << y_n << "\n";
    arr_terms_Euler[i + 1] = y_n;
    anterior = y_n;
  };
  MyFile.close();

  // Método Runge-Kutta de 4to orden
  t = 0;
  anterior = 1;
  double arr_terms_Runge[M];

  MyFile.open("runge_array.txt");
  MyFile << 0 << " " << 1 << "\n";
  arr_terms_Runge[0] = 1;

  for (int i = 0; i < M; i++)
  {

    double k1 = h * funcion(anterior);

    double k2 = h * funcion(anterior + k1 / 2);

    double k3 = h * funcion(anterior + k2 / 2);

    double k4 = h * funcion(anterior + k3);

    double y_n = anterior + (k1 + 2 * k2 + 3 * k3 + k4) / 6;
    t = t + h;

    MyFile << t << " " << y_n << "\n";
    arr_terms_Runge[i + 1] = y_n;

    anterior = y_n;
  };
  MyFile.close();

  // Exploramiento error:
  // Para t = h
  cout << "Para t = h"
       << "\n";
  cout << "Método euler: " << abs(arr_terms_Euler[1] - solucionAnalitica(h)) << "\n";
  cout << "Método Runge-Kutta: " << abs(arr_terms_Runge[1] - solucionAnalitica(h)) << "\n\n";

  // Para t = 900*h
  cout << "Para t = 900*h"
       << "\n";
  cout << "Método euler: " << abs(arr_terms_Euler[900] - solucionAnalitica(900 * h)) << "\n";
  cout << "Método Runge-Kutta: " << abs(arr_terms_Runge[900] - solucionAnalitica(900 * h)) << "\n";
}
