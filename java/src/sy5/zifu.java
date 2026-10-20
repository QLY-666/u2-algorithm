//因为父类子类里的方法都是与类名同名，所以都是构造方法，所以在执行Zi z = new Zi()时，
// 会先执行输出构造方法里的代码，即输出“zi”,并且子类隐含包含了super(),即先执行父类的构造方法Fu，
// 即先输出fu,再输出zi，而show中的三个println分别表示输出局部变量num=30,当前对象的成员变量num=20,
// 和父类的成员变量num=10

//1.构造方法（方法和类同名）：会在创建对象时直接执行这个方法
//2.this代表当前类的对象的成员变量
//3.super代表父类的成员变量
//4.成员变量：就是类里面在代码块，方法，构造器外的变量
//5.子类会隐藏super（空参数情况）,即系统会先使父类初始化，确保子类在父类的基础上
//6.构造代码块和构造方法都是只在创建对象时执行，后续调用方法都不会执行，因为本质是给对象初始化的赋值

package sy5;

class Fu{
    public int num = 10;
    public Fu(){
        System.out.println("fu");
    }
}
class Zi extends Fu{
    public int num = 20;
    public Zi(){
        System.out.println("zi");
    }
    public void show(){
        int num = 30;

        //局部变量
        System.out.println(num);

        //当前类的对象的成员变量
        System.out.println(this.num);

        //父类的成员变量
        System.out.println(super.num);
    }
}
class zifu {
    public static void main(String[] args) {

        //创建对象z时就已经先后执行了父类子类的构造方法，即先后输出fu和zi
        Zi z = new Zi();
        z.show();
    }
}