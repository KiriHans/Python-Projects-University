#include <iostream>
#include <fstream>
#include <cmath>
#include <stdlib.h>
#include <time.h>

using namespace std;

const float carFuel = 3.14;

float miFuncion(float mivarflotante, int mivarentera){
  return pow(mivarflotante,mivarentera);
}


void imparYMenorA800(int array[300]){
  ofstream MyFile("datos2.txt");
  for(int i = 0; i < 300; i++){
    if(array[i] % 2 == 1){
      MyFile << array[i] << "\n";
    };
    if(array[i] > 800){
      MyFile.close();
      break;
    };
  };
  MyFile.close();
}

const float a = 2.0;
const int b = 10;


int main(){
  cout << "La primera tiene un valor de " << a << " y la segunda variable tiene un valor de " << b << "\n";
  
  float c = b/a;
  cout << "El resultado es " << c << "\n";
  
  srand (time(NULL));

  int arr_int[300];
  for(int i = 0; i < 300; i++){
    arr_int[i] = rand()%901;
  };
 
  for(int i = 0; i < 300; i++){
    cout << "El elemento " << i << " es: " << arr_int[i] << "\n";
  };

  cout << "El quinto elemento del array es " << arr_int[5] << "\n";
 
  long longitud = sizeof(arr_int);
  cout << "La longitud del arreglo es " << longitud << " bytes" << "\n";
  

  float valorFuncion =  miFuncion(17.5, 5);
  cout << "El valor de la funcion es: " << valorFuncion << "\n";
  
  imparYMenorA800(arr_int);

  ofstream MyFile("datos1.txt");
  for(int i = 0; i < 300; i++){
    MyFile << arr_int[i] << "\n";
  }
  MyFile.close();

  return 0;
}



