/**
 * Base
 */
class Base {
    int x;
}
class DemoClass extends Base{
    int y;
}



public class Inheritence {
    public static void main(String[] args) {
        DemoClass obDemo=new DemoClass();
        Base obBase=new Base();

        obBase.x=98;
        System.out.println("the value of atribute x in base class is "+obBase.x);  

        obDemo.x=55555;
        System.out.println("the value of atribute x in base class is "+obDemo.x); 
        
        System.out.println("the value of atribute x in base class is "+obBase.x);  

        obDemo.y=78;
        System.out.println("the value of atribute y in democlass is "+obDemo.y);   

    }
}
