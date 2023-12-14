#include <iostream>
#include <fstream>
#include <cmath>
#include <stdlib.h>

using namespace std;

const short c = 300;
const short l = 2;
const double dx = 0.02;
const int M = 100;

double rozamiento(double a, short c, double t, short l)
{
  return a * cos(3.0 * c * t * M_PI / (l));
}

void diferencias_finitas(double dt, double t_final, string name_file)
{
  double u_pasado[100];
  double u_presente[100];
  double u_futuro[100];

  ofstream MyFile(name_file);

  for (int i = 0; i < M; i++)
  {
    if (i <= 50)
    {
      u_pasado[i] = i * dx;
      MyFile << 0 << " " << i * dx << "\n";
    }
    else
    {
      u_pasado[i] = 2 - i * dx;
      MyFile << 0 << " " << 2 - i * dx << "\n";
    }
  }

  // Primera iteración

  u_presente[0] = 0;
  MyFile << dt << " " << 0 << "\n";

  for (int i = 1; i < M - 1; i++)
  {
    u_presente[i] = u_pasado[i] + (0.5) * pow((c * dt) / dx, 2) * (u_pasado[i + 1] - 2 * u_pasado[i] + u_pasado[i - 1]);
    MyFile << dt << " " << u_presente[i] << "\n";
  }
  u_presente[M - 1] = 0;
  MyFile << dt << " " << 0 << "\n";

  double counter = 2 * dt;
  while (counter <= t_final)
  {
    u_futuro[0] = 0;
    MyFile << counter << " " << 0 << "\n";
    for (int i = 1; i < M - 1; i++)
    {
      u_futuro[i] = 2 * u_presente[i] - u_pasado[i] + pow(c * dt / dx, 2) * (u_presente[i + 1] - 2 * u_presente[i] + u_presente[i - 1]);
      MyFile << counter << " " << u_futuro[i] << "\n";
    }
    u_futuro[M - 1] = 0;
    MyFile << counter << " " << 0 << "\n";

    copy(u_presente, u_presente + M, u_pasado);

    copy(u_futuro, u_futuro + M, u_presente);

    counter += dt;
  }

  MyFile.close();
}

void diferencias_finitas_con_rozamiento(double dt, double t_final, string name_file)
{
  double u3_pasado[100];
  double u3_presente[100];
  double u3_futuro[100];

  int a = 1;

  ofstream MyFile(name_file);

  for (int i = 0; i < M; i++)
  {
    if (i <= 50)
    {
      u3_pasado[i] = i * dx;
      MyFile << 0 << " " << i * dx << "\n";
    }
    else
    {
      u3_pasado[i] = 2 - i * dx;
      MyFile << 0 << " " << 2 - i * dx << "\n";
    }
  }

  // Primera iteración

  u3_presente[0] = 0;
  MyFile << dt << " " << 0 << "\n";

  for (int i = 1; i < M - 1; i++)
  {
    u3_presente[i] = u3_pasado[i] + (0.5) * pow((c * dt) / dx, 2) * (u3_pasado[i + 1] - 2 * u3_pasado[i] + u3_pasado[i - 1]);
    MyFile << dt << " " << u3_presente[i] << "\n";
  }

  u3_presente[M - 1] = rozamiento(a, c, dt, l);
  MyFile << dt << " " << u3_presente[M - 1] << "\n";

  double counter = 2 * dt;
  while (counter <= t_final)
  {
    u3_futuro[0] = 0;
    MyFile << counter << " " << 0 << "\n";
    for (int i = 1; i < M - 1; i++)
    {
      u3_futuro[i] = 2 * u3_presente[i] - u3_pasado[i] + pow(c * dt / dx, 2) * (u3_presente[i + 1] - 2 * u3_presente[i] + u3_presente[i - 1]);
      MyFile << counter << " " << u3_futuro[i] << "\n";
    }
    //
    u3_futuro[M - 1] = rozamiento(a, c, counter, l);
    MyFile << counter << " " << u3_futuro[M - 1] << "\n";

    copy(u3_presente, u3_presente + M, u3_pasado);

    copy(u3_futuro, u3_futuro + M, u3_presente);

    counter += dt;
  }

  MyFile.close();
}

int main()
{

  double dt = 0.5 * dx / c;

  double t_final = 0.1;

  diferencias_finitas(dt, t_final, "ecuacion_de_onda_1.txt");

  // Cambiando a dt=3*dx/c

  dt = 3 * dx / c;

  diferencias_finitas(dt, t_final, "ecuacion_de_onda_2.txt");

  // Condiciones de frontera: fija en x = 0 y forzada en x=L

  // dt = 0.5*dx/c;
  dt = 0.5 * dx / c;

  diferencias_finitas_con_rozamiento(dt, t_final, "ecuacion_de_onda_3.txt");
}
