package sy2;

public class RelationAndLogicOperation
{
    public static void main(String args[])
    {
        int a=5,b=3;
        boolean c=a<b;
        System.out.println(a+"＜"+b+"="+c);
        boolean d=(b!=0&&a/b>5);
        System.out.println(b+"!=0&&"+a+"/"+b+">5="+d);
        boolean e=(b!=0&&a/b<5);
        System.out.println(b+"!=0&&"+a+"/"+b+"<5="+e);
    }
}
