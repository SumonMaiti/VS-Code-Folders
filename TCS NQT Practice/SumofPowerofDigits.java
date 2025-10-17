import java.util.Scanner;
class Test {
    static int sum=0,i=0,j=0;
    static void method(int n){
            while (n>0) {
                i=n%10;
                sum+=Math.pow(i, j);
                j=i;
                n/=10;
            }
            System.out.println("sum= "+sum);
    } 
}
public class SumofPowerofDigits{ 
    public static void main(String[] args){
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter a number : ");
        int n1=sc.nextInt();
        Test.method(n1);
        
    }

}
