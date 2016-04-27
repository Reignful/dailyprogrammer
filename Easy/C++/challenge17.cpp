#include <iostream>
#include <string>

using namespace std;

void print();

int main() {
    print();
    return 0;
}

void print() {
    int height = 0, multi = 1;
    char star = '@';
    cout << "Enter a height: ";
    cin >> height;

    for (int i = 0; i < height; i++) {
        for (int j = 0; j < multi; j++) {
            cout << star;
        }
        multi *= 2;
        cout << endl;
    }
}
