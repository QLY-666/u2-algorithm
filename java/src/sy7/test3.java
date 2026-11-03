package sy7;
import java.util.Random;
import java.math.BigInteger;

//1.BigInteger类：用于数字超过一般范围，如long都存不下的数字，要导入类
//2.BigInteger sum=BigInteger.ZERO：将对象设置常量0，如果用"0"就要每次都创建对象，所以一般用常量
//3.BigInteger.valueOf(i)：把int类型的i转为BigInteger，因为用到的方法都是BigInteger类里的
//add	    a.add(b)	    加法
//subtract	a.subtract(b)	减法
//multiply	a.multiply(b)	乘法
//divide	a.divide(b)	    除法（整除）
//mod	    a.mod(b)	    取余
//pow	    a.pow(3)	    幂
//abs	    a.abs()	        绝对值
//negate	a.negate()	    取反
//compareTo	a.compareTo(b)	比较，返回 -1/0/1
//max / min	a.max(b)	    较大/较小
//gcd	    a.gcd(b)	    最大公约数
//toString	a.toString()	转字符串

//5.math类是系统自带的
//abs	    Math.abs(-5)	绝对值	5
//max	    Math.max(3, 7)	较大值	7
//min	    Math.min(3, 7)	较小值	3
//pow	    Math.pow(2, 10)	幂（返回 double）1024.0
//sqrt	    Math.sqrt(16)	平方根	4.0
//cbrt	    Math.cbrt(27)	立方根	3.0
//round	    Math.round(3.6)	四舍五入（返回 long）	4
//ceil	    Math.ceil(3.1)	向上取整	4.0
//floor	    Math.floor(3.9)	向下取整	3.0
//random	Math.random()	随机数 [0,1)	0.xxx

//6.random，要new，对比math里的random返回类型更多（math里的只有double），且可以自己定义范围
//nextInt()	        r.nextInt()	       任意 int（有正有负）
//nextInt(bound)	r.nextInt(100)	   [0, 100) 的整数
//nextDouble()	    r.nextDouble()	   [0.0, 1.0) 的小数
//nextBoolean()	    r.nextBoolean()	   true / false
//nextLong()	    r.nextLong()	   任意 long
//nextFloat()	    r.nextFloat()	   [0.0, 1.0) 的 float
//nextGaussian()	r.nextGaussian()   正态分布

public class test3 {
    public static void main(String[] args) {
       int n = 20;
       BigInteger sum = BigInteger.ZERO;
       BigInteger t = BigInteger.ONE;
       for(int i = 1;i <= n;i++) {
           t = t.multiply(BigInteger.valueOf(i));
           sum = sum.add(t);
       }
       System.out.println("1+2!+3!+…+20!的值为："+sum);

       System.out.println("5的平方根为："+Math.sqrt(5));

       Random count = new Random();
       System.out.println("从1～100中随机产生6个不同的整数为：");

       for(int i = 0;i <= 5;i++) {
           System.out.println(count.nextInt(100)+1);
       }
    }
}