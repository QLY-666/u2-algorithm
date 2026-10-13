package sy3;

class Student2 {
    String name; // 姓名
    int age;     // 年龄


    public Student2() {
    }

    public Student2(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void study2() {
        System.out.println(name + "正在学习。");
    }

    public void exam2() {
        System.out.println(name + "正在考试。");
    }
}

public class StudentTest2 {
    public static void main(String[] args) {
        //无参构造
        Student2 s1 = new Student2();
        s1.name = "张三";
        s1.age = 19;
        System.out.println("方式一：无参构造，直接赋值");
        System.out.println("姓名：" + s1.name + "，年龄：" + s1.age);
        s1.study2();
        s1.exam2();
        System.out.println();

        //含参构造
        Student2 s2 = new Student2("李四", 20);
        System.out.println("方式二：有参构造，函数的参数赋值");
        System.out.println("姓名：" + s2.name + "，年龄：" + s2.age);
        s2.study2();
        s2.exam2();
    }
}