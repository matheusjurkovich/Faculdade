#include <iostream>
using namespace std;

int main()
{
    int a, b;

    while (true) 
    {
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
        cout << a << " / " << b << " = " << a / b << endl;
    }
    else
    {
        cout << "Divisao por zero. Numero invalido." << endl;
    }
	}

    return 0;
}
