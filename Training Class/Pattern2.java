/*
*           * 
* *       * *
* * *   * * *
* * * * * * * 
* * *   * * *
* *       * *
*           * 
 */

public class Pattern2 {
    public static void main(String[] args) {
        for(int i=1;i<=4;i++){
            for(int j=1;j<=i;j++)
                System.out.printf("* ");
            for(int k=1;k<(4-i)*2;k++)
                System.out.printf("  ");
            if(i!=4){
                for(int l=1;l<=i;l++)
                    System.out.printf("* ");
            }
            else{
                for(int l=1;l<i;l++)
                    System.out.printf("* ");
            }
        System.out.printf("\n");
        }

        for(int i=3;i>=1;i--){
            for(int k=1;k<=i;k++)
                System.out.printf("* ");
            for(int j=0;j<=(3-i)*2;j++)
                System.out.printf("  ");
            for(int j=1;j<=i;j++)
                System.out.printf("* ");
        System.out.printf("\n");
        }
        
    }    
}
