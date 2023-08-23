#include <iostream>
using namespace std;

int main()
{
    cout << "======= Calculadora =======" << endl << endl;

    while (true) 
    {
        int a, b;

        cout << "Digite o primeiro numero: ";
        cin >> a;

        cout << "Digite o segundo numero: ";
        cin >> b;

        cout << "Resultados:" << endl;
        cout << a << " + " << b << " = " << a + b << endl;
        cout << a << " - " << b << " = " << a - b << endl;
        cout << a << " * " << b << " = " << a * b << endl;

        if (b != 0)
        {
            cout << a << " / " << b << " = " << static_cast<double>(a) / b << endl;
        }
        else
        {
            cout << "Divisao por zero. Numero invalido." << endl;
        }

        char opcao;
        cout << "Deseja realizar outro calculo? (S/N): ";
        cin >> opcao;

        if (opcao != 'S' && opcao != 's')
        {
            cout << "Saindo da calculadora." << endl;
            break;
        }

        cout << endl;
    }

    return 0;
}
