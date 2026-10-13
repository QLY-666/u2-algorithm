package sy2;

public class DataTypesChange
{
    public static void main(String args[])
    {
        byte a=8;
        char b='a';     //'a'的Unicode码对应的十进制数是97
        int c=12;
        long d=145L;
        float e=8.29F;
        double f=365.725;
        int g=b+c;      //char型的变量b转换为int型
        long h=d-c;     //int型的变量c转换为long型
        float i=a*e;    //byte型的变量a转换为float型
        double j=i/g-f; //int型的变量g转换为float型，i/g的结果又转换为double型
        System.out.println("g="+g);
        System.out.println("h="+h);
        System.out.println("i="+i);
        System.out.println("j="+j);
    }
}
