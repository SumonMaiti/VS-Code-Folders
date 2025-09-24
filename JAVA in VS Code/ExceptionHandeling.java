class InnerExceptionHandeling {

    public static void doStaff(){
        System.out.println("in do staff");
        System.out.println(10/0);

    }
    public static void doMoreStaff(){
        System.out.println("In do more staff");
        doStaff();
    }
}
public class ExceptionHandeling {
    
    public static void main(String[] args) {
        InnerExceptionHandeling.doMoreStaff();
    }
}
