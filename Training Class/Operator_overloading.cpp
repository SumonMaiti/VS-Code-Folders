#include<iostream>
using namespace std;
class Complex{
    
    double real,imag;
    public:
    Complex(){

    }
    Complex(double r,double i){
        this->imag=i;
        this->real=r;
    }
    void display(){
        if(imag>0){
            cout<<"\nThe complex number = "<<this->real<<"+"<<this->imag<<"j";
        }
        else{
            cout<<"\nThe complex number = "<<this->real<<this->imag<<"j";
        }
    }
    Complex operator+(Complex c){//only zero or one parameter can be used
        Complex ob3;
        ob3.real=real+c.real;
        ob3.imag=imag+c.imag;
        return ob3;
    }
};

int main(int argc, char const *argv[])
{
    Complex c1(3.4,2.9),c2(5.5,-6.2);
    c1.display();
    c2.display();
    Complex c3=c1+c2;
    cout<<"\nAfter addition the complex number... ";
    c3.display();
    return 0;
}
