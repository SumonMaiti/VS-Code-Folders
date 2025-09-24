#include<iostream>
using namespace std;

class Customer // data member and member functions are encapsulated within a class;
{
    private:
        string name;
        int acc_no;
        int balance;
        int* pointer=new int; // Pointer declared and dynamically memory is created.

    public:
        
        static int number;// -> in static variable value can't be 
        //assigned while declaring . value must be assigned o/s class.

        Customer(Customer &temp){ // This is copy constructor. Here temp is a refernce variable of object.
            this->name=temp.name;
            this->acc_no=temp.acc_no;
            this->balance=temp.balance;
            number++;
        }

        Customer(){// Default constructor
            cout<<"in non parametarized constructor"<<endl;
            name="PNB customer";
            acc_no=000000;
            balance=00;
            *pointer=200; // data in memory where the pointer is pointing is assigned.
            number++;
        }

    /*  Customer(string name,int acc_no,int balance){//  parametarized constructor(3 parameter)
            cout<<"in 3 parametarized constructor\n";
            this->name=name;
            this->acc_no=acc_no;
            this->balance=balance;
            number++;
        }
    */

    inline Customer(string n,int acc,int bal) : name(n),acc_no(acc),balance(bal){
        // this is an example of inline constructor with 3 parameter. 
        // if we don't write inline, then also the code will work.
        number++;
    }

        Customer(string name,int acc_no){   // Parametarized constructor(2 parameter)
            cout<<"in 2 parameterized constructor";
            this->name=name;
            this->acc_no=acc_no;
            this->balance=200;
            number++;
        }

        ~Customer(){// this is an destructor.
            // destructor is used to release dynamically created memory. Or close any file.
            cout<<"Destructor called and pointer is deleted"<<endl;
            delete pointer;
        }

        void show(){
            
            cout<<"Name = "<<this->name<<endl;
            cout<<"Account Number= "<<this->acc_no<<endl;
            cout<<"Balance = "<<this->balance<<endl;
            cout<<"Number of object= "<<number<<endl;
            cout<<"Pointer value= "<<*pointer<<endl;
        }
   
};

int Customer::number=0; //*-> static member variable of the class
// --> data type written is mandatory.
// -> static variable is property of class not object.

int main(int argc, char const *argv[])
{
    //Customer c1;
    //c1.show();

   // Customer c2("Sumon Maiti",98003,300);
    //c2.show();

    //Customer *c1=new Customer("Sumon Maiti",98003,300);
   // c1->show();
    //delete c1;

    Customer c2;
    //Customer c3(c2); // data of c2 copied in c3 object.
   // Customer c3=c2; // data of c2 copied in c3 object.
    c2.show();
   // c3.show();
   
    return 0;
}
