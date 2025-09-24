/**
 * constructor
 */
/**
 * test
 */

class Test {
    
    Test(int x){ // this is a constructor 
        System.out.println("value in constructor x is "+x);
    }
    // void meth(int a){

    //     System.out.println("this is in the meth method");
    //     System.out.println("the value of a is ; "+a);
        

    // }
    
}
public class constructor {
    static void staticMethod(){// no need to create an object for this method
        System.out.println("This is a static method");
    }
//     static{
//         System.out.println("this is a static block");
//     }
    public static void main(String[] args) {
        System.out.println("this is in the main method ");
        constructor.staticMethod();
        Test t1= new Test(5);
        //t1.meth(15);

       
		
    }
}
