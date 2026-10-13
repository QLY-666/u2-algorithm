package sy3;

class Student {
    String name;
    int age;
    public void Study() {
      System.out.println(name+"在学习");
    }
    public void exam() {
      System.out.println(name+"在考试");
    }
}

public class StudentTest {
    public static void main (String[] args) {
        Student s = new Student();
        s.age = 18;
        s.name = "小明";
        System.out.println("学生信息："+s.name + "," + "年龄：" + s.age);
        s.Study();
        s.exam();
    }
}
