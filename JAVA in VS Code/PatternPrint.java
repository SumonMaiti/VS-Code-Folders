import java.util.*;
/**
 * Print
 */
class Print {

    Print(int range){
        int a=65;
        for(int i=1;i<=range;i++){
            System.out.printf("%c%d",a,a-64  );
            if(i!=range){
                System.out.print(", ");
            }

            a++;
            if(a>90)
            a-=26;
        }
    }
}
public class PatternPrint {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the range : ");
        int range= sc.nextInt();
        Print obj= new Print(range);
    }

}
