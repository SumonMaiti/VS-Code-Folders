/**
 * Student1
 */
abstract class Student1 { // to create an abstract method or atribute the class must be abstract

    String name="Sumon",stream="ECE";
    abstract String wife_name;
    abstract public void study();

}

class Student2 extends Student1{
    String wife_name="hhhhhh";
    public void study(){
        System.out.println("Studying at college");
    }
}


public class Abstract_class {
    public static void main(String[] args) {
        Student2 ob1=new Student2();
        System.out.println(ob1.name);
    }
}
