package java_codes;

public class Subsets
{
    public static void makeSubs(int n, int i,String ans)
    {
        if(i>n)
        {
            System.out.println(ans);
            return;
        }
        makeSubs(n,i+1,ans+Integer.toString(i));
        makeSubs(n,i+1,ans);
    }
    public static void main(String[] args)
    {
        makeSubs(3,1,"");
    }
     

}
