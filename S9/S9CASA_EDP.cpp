#include <iostream>
#include <fstream>
#include <cmath>
#include <stdlib.h>

using namespace std;

int main()
{
  const short L = 1;
  const double V = 0.0001;
  const short M = 100;
  double dx = (double)L / M;

  double dy = (double)L / M;
  double dt = 0.2 * pow(dx, 2) / V;
  double t_final = 2500.0;
  double T_pasado[M][M];
  double T_presente[M][M];

  ofstream MyFile("difusion.txt");

  for (int i = 0; i < M; i++)
  {
    for (int j = 0; j < M; j++)
    {
      if (20 <= i && i <= 40 && 40 <= j && j <= 60)
      {
        T_pasado[i][j] = 100;
      }
      else
      {
        T_pasado[i][j] = 50;
      }
    }
  }

  MyFile << 0 << " ";
  for (int i = 0; i < M; i++)
  {
    for (int j = 0; j < M; j++)
    {

      MyFile << " " << T_pasado[i][j];
    }
  }
  MyFile
      << "\n";

  double counter = dt;
  int steps = 1;
  while (counter <= t_final)
  {

    for (int j = 0; j < M; j++)
    {
      T_presente[0][j] = 50;
      T_presente[M - 1][j] = 50;
    }

    for (int i = 0; i < M; i++)
    {
      T_presente[i][0] = 50;
      T_presente[i][M - 1] = 50;
    }

    for (int i = 1; i < M - 1; i++)
    {
      for (int j = 1; j < M - 1; j++)
      {
        T_presente[i][j] = dt * V * ((T_pasado[i + 1][j] - 2.0 * T_pasado[i][j] + T_pasado[i - 1][j]) / pow(dx, 2) + (T_pasado[i][j + 1] - 2.0 * T_pasado[i][j] + T_pasado[i][j - 1]) / pow(dy, 2)) + T_pasado[i][j];
      }
    }

    if (steps == 500 || steps == 5000 || steps == 12500)
    {
      MyFile << counter << " ";
    }

    for (int i = 0; i < M; i++)
    {
      for (int j = 0; j < M; j++)
      {
        if (steps == 500 || steps == 5000 || steps == 12500)
        {
          MyFile << " " << T_presente[i][j];
        }
        T_pasado[i][j] = T_presente[i][j];
      }
    }

    if (steps == 500 || steps == 5000 || steps == 12500)
    {
      MyFile
          << "\n";
    }

    counter += dt;
    steps += 1;
  }

  MyFile.close();
}
