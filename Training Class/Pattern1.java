/*
         * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
 */

public class Pattern1 {
    public static void main(String[] args) {
        for(int i=1;i<=5;i++){
            for(int j=1;j<=5-i;j++)
                System.out.printf("  ");
            for(int k=1;k<=i*2-1;k++)
                System.out.printf("* ");
        System.out.printf("\n");
        }

        for(int i=4;i>=1;i--){
            for(int k=0;k<=4-i;k++)
                System.out.printf("  ");
            for(int j=1;j<=2*i-1;j++)
                System.out.printf("* ");
            
        System.out.printf("\n");
        }
    }    
}
