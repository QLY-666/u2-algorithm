package sy6;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

//内部类：在类里面创建类

public class Outer {
    class Inner{
        public void hello() {
            System.out.println("Hello World!");
        }
    }

    //useinner先创建了inner对象并调用了hello方法
    public void UseInner() {
        new Inner().hello();
    }

    static {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        System.out.println("班级：计科252 学号：2500502222 姓名：李维熙");
        System.out.println("当前时间：" + now.format(formatter));
    }

    public static void main(String[] args) {

        //这里创建了outer对象和inner对象，所以可用inner的方法
        Outer.Inner hi =new Outer().new Inner();
        //法2：也可以直接new outer().UseInner(),就是创建outer对象同时调用它的方法
        hi.hello();
    }
}
