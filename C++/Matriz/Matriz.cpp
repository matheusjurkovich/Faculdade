#include <iostream>
using namespace std;

const int ROWS = 3;
const int COLS = 3;

int main() {
	//Matrizes sempre tem que ter a quantidade de colunas e linhas
    int A[ROWS][COLS] = {{10, 30, 50}, {5, 15, 25}, {2, 5, 9}};
    int B[ROWS][COLS] = {{5, 35, 70}, {1, 25, 30}, {1, 4, 7}};
    int C[ROWS][COLS];
    int menorA = A[0][0];
    int maiorB = B[0][0];

    // Exibir matriz A e encontrar o menor valor
    cout << "*==Matriz A==*" << endl;
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            cout << A[i][j] << " ";
            if (A[i][j] < menorA) {
                menorA = A[i][j];
            }
        }
        cout << endl;
    }

    // Exibir matriz B e encontrar o maior valor
    cout << endl;
    cout << "*==Matriz B==*" << endl;
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            cout << B[i][j] << " ";
            if (B[i][j] > maiorB) {
                maiorB = B[i][j];
            }
        }
        cout << endl;
    }

    // Exibir o menor valor de A e o maior valor de B
    cout << endl;
    cout << "Menor valor de A: " << menorA << endl;
    cout << "Maior valor de B: " << maiorB << endl;
    cout << endl;

    // Calcular a matriz C com os valores máximos entre A e B
    cout << "*==Matriz C==*" << endl;
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            if (A[i][j] > B[i][j]) {
                C[i][j] = A[i][j];
            } else {
                C[i][j] = B[i][j];
            }
            cout << C[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
