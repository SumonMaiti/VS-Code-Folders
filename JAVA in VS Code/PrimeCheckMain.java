import java.util.*;
class PrimeCheck
{
	int check(int n)
	{
		for(int i=2;i<=Math.sqrt(n);i++)
		{
			if(n%i==0)
				return 0;
		}
		return 1;
	}
}
public class PrimeCheckMain
{
	public static void main(String args[])
	{
			Scanner sc=new Scanner(System.in);
			System.out.println("Enter range: ");
			int n=sc.nextInt();
			PrimeCheck p1=new PrimeCheck();
			System.out.println("Prime numbers between 1 to "+n+" ");
			for(int i=2;i<=n;i++)
			{	
				int v=p1.check(i);
				if(v==1)
					System.out.print(i+"  ");
			}
	}
}
