//静态代码块只在类初始化时执行，所以创建s2对象时不会执行静态代码块，
// 而构造代码块和构造方法在每次创建对象时都会执行1次，所以两次都有

//1.静态代码块：在方法外，类初始化时执行，即创建第一个对象时执行，但创建第二个对象（同类）不会执行
//2.构造代码块和构造方法都是只在创建对象时执行，后续调用方法都不会执行，因为本质是给对象初始化的赋值

package sy5;

class Student {
    static {
        System.out.println("sy5.Student 静态代码块");
    }

    {
        System.out.println("sy5.Student 构造代码块");
    }

    public Student() {
        System.out.println("sy5.Student 构造方法");
    }
}

class StudentDemo {
    static {
        System.out.println("计科21，我们的大家庭");
    }

    public static void main(String[] args) {
        System.out.println("我是main方法");

        Student s1 = new Student();

        //s2不会执行输出"sy5.Student 静态代码块"
        Student s2 = new Student();
    }
}