/**
 * InnerGetSet
 */
 class InnerGetSet {

    private int x; // we can't access value of private atributes
    int getValueX(){// we use get and set method to access or modify private attributes
        return x;
    }
    void setValueX(int setvalue){
        this.x=setvalue;
    }
}

public class GetSet {
    
    public static void main(String[] args) {
        InnerGetSet ob=new InnerGetSet();
        ob.setValueX(20);
        System.out.println(ob.getValueX());

    }
}
