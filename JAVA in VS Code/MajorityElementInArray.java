public class MajorityElementInArray {
    public static void main(String[] args) {
        int arr[]={2,2,24,6,5,1,7,4,1};//wrong o/p in : {2,3,5,3,4,3,5,5,8,2,2,2,1,1,5,2,5,4}
        int ele1=-1,ele2=-1;
        int count1=0,count2=0;
        int result[]=new int[2];
        for (int  ele : arr) {
            if (ele1==ele) {
                count1++;
            }
            else if (ele2==ele) {
                count2++;
            }
            else if (count1==0) {
                ele1=ele;
                count1++;
            }
            else if (count2==0 ) {
                ele2=ele;
                count2++;
            }
            
            else{
                count1--;count2--;
            }
        }
        result[0]=ele1;result[1]=ele2;
        count1=0;count2=0;
        for (int ele : arr) {
            if (ele==ele1) {
                count1++;
            }
        }
        for (int ele : arr) {
            if (ele==ele2) {
                count2++;
            }
        }
        if (count2>count1) {
            result[1]=ele1;result[0]=ele2;
        }
        for (int i : result) {
            System.out.println(i);
        }
        
    }
}
