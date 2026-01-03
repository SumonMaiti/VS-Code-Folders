
 class BinarySearch{
    void bSearch(int[] a,int key){
        int high=a.length-1,low=0,mid;
        while (low<high) {
            mid=(low+high)/2;
            if(key==a[mid]){
                System.out.println("Found the element in position " + (mid+1));
                break;
            }
            else if (key>a[mid]) {
                low=mid+1;
                
            }
            else
                high=mid-1;
        }
    }

}
 class SwapTwoNumbers {
    static void swapFunction(int a,int b){
        // a=a+b;
        // b=a-b;
        // a=a-b;
        int temp;
        temp=a;
        a=b;
        b=temp;
        System.out.println("Value of a = "+a+"Value of b="+b);
    }
    
}
 class ArmstrongNumber {

    static void armstrongMethod(int n){
        int dig=0,sum=0,temp=n;
        while (n>0) {
         dig++;
         n/=10;   
        }
        n=temp;
        while (n>0) {
            int rem=n%10;
            sum+=Math.pow(rem, dig);
            n/=10;
        }
        if (sum==temp) {
            
            System.out.println("Armstrong Number");
        }
        else
                System.out.println("Not a Armstrong Number");
    }
}
class Palindrome{
   static void checkPalindrome(String s){
        int i=0,j=s.length()-1;
        int flag=1;
        while (i<j) {
            if(s.charAt(i)!=s.charAt(j))
                    flag=0;
                i++;j--;
        }
        if (flag==1) {
            System.out.println("The number is a palindrome");
            
        }
        else
            System.out.println("The number is not a palindrome");
        
    }
}
class StarPattern{
    static void starPrint(){
        for(int i=1;i<=4;i++){
            for(int j=1;j<=i;j++){
                System.out.print("* ");
            }
            System.out.println();
        }
        for(int i=4;i>=1;i--){
            for(int j=i;j>=1;j--){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
public class InterviewPrep {
    public static void main(String[] args) {
        // BinarySearch ob=new BinarySearch();
        // int[] a={1,2,3,4,5,6,7,8,9};
        // System.out.println("hi");
        // ob.bSearch(a,7);

        //SwapTwoNumbers.swapFunction(23, 12);
       // ArmstrongNumber.armstrongMethod(1634);
       //Palindrome.checkPalindrome("2992");
       StarPattern.starPrint();
    }
    
}