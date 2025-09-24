import java.util.Scanner;
 class Teststudent{
     int rollNo;
     String name;
     String stream;
     String college;

  
    public Teststudent(int rollNo, String name, String stream, String college) {
        this.rollNo = rollNo;
        this.name = name;
        this.stream = stream;
        this.college = college;
    }

    
    public int getRollNo() {
        return rollNo;
    }

    public String getName() {
        return name;
    }

    public String getStream() {
        
        return stream;
    }

    public String getCollege() {
        return college;
    }
}

public class MainUsingThis {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);        
        Teststudent s1 = new Teststudent(87, "Sumon", "ECE","AoT");
        System.out.println(s1.getName());
        System.out.println(s1.getRollNo());
        System.out.println(s1.getStream());
        System.out.println(s1.getCollege());
}
}