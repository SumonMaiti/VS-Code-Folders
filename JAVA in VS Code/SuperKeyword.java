class Parent{
    void display(){
        System.out.println("I am in parent class");
    }
}
 class Child extends Parent {
     void display(){
        super.display();//super is used to access the method of parent class
        System.out.println("I am in child class");
    }
    
}
public class SuperKeyword {
    public static void main(String[] args) {
        Child ob1=new Child();
        ob1.display();
    }
    
}
