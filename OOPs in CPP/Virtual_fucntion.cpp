#include <iostream>
using namespace std;

class Base {
public:
   virtual void show() { // Virtual function
        cout << "Base class show function" << endl;
    }
};

class Derived : public Base {
public:
    void show() override { // Overriding the virtual function
        cout << "Derived class show function" << endl;
    }
};

int main() {
   // Base* ptr; // Pointer to base class
    //Derived d;
   // ptr = &d;
   Base* ptr=new Derived();
    
    ptr->show(); // Calls Derived class show() due to virtual function
    return 0;
}
