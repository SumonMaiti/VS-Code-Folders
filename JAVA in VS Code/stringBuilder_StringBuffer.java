public class stringBuilder_StringBuffer {
    public static void main(String[] args){
        String name1="sumon";
        String name2=name1;// the name1 and name2 is pointing the same location.

        StringBuilder name3=new StringBuilder("tonyStringBuilder");
//for each loop can't be applicable for string,stringBuilder,stringBuffer we have to convert in ..
// character array using toCharArray() method.
        //char[] charArray=name2.toCharArray();
        System.out.println(name1);//when the name1 is changed it creates a new string in a new memory
        System.out.println(name2);

      //  name3.reverse();
        // for (char a : charArray){
        //     System.out.println(a);
        // }
        //System.out.println(name3);
        
      // System.out.println(name3.substring(1,5)); 
       name3.insert(0,'u');
       System.out.println(name3);
    }


}
