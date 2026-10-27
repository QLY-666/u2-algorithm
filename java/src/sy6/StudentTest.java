package sy6;
import java.util.Scanner;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

//抽象类和抽象方法：
//抽象类：1.只要类里面有抽象方法，就必须是抽象类
//2.抽象类不能用于创建对象像animal a=int animal;只能创建子类如ani a = int cat;
//抽象方法：就是方法体内空白，如abstract int ax() {}


abstract class Student {
    String name;
    String[] courses;
    double[] scores;

    public Student(String name, String[] courses, double[] scores) {
        this.name = name;
        this.courses = courses;
        this.scores = scores;
    }

    public double average() {
        double sum = 0;
        for (double s : scores) {
            sum += s;
        }
        return sum / scores.length;
    }

    public abstract String getType();
    public abstract String getLevel(double score);

    @Override
    public String toString() {
        return name + "（" + getType() + "）平均分：" + average()
                + "，等级：" + getLevel(average());
    }
}

class Undergraduate extends Student {
    public Undergraduate(String name, String[] courses, double[] scores) {
        super(name, courses, scores);
    }

    @Override
    public String getType() {
        return "本科生";
    }

    @Override
    public String getLevel(double score) {
        if(score >= 80) return "优秀";
        if (score >= 70) return "良好";
        if (score >= 60) return "一般";
        if (score >= 50) return "及格";
        return "不及格";

    }
}

class Postgraduate extends Student {
    public Postgraduate(String name, String[] courses, double[] scores) {
        super(name, courses, scores);
    }

    @Override
    public String getType() {
        return "研究生";
    }

    @Override
    public String getLevel(double score) {
        if(score >= 90) return "优秀";
        if (score >= 80) return "良好";
        if (score >= 70) return "一般";
        if (score >= 60) return "及格";
        return "不及格";

    }
}


public class StudentTest {
    static {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        System.out.println("班级：计科252 学号：2500502222 姓名：李维熙");
        System.out.println("当前时间：" + now.format(formatter));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Student[] stus = new Student[4];
        for (int i = 0; i < stus.length; i++) {
            System.out.print("姓名：");
            String name = sc.next();
            System.out.print("类别（1本科生 2研究生）：");
            int t = sc.nextInt();
            String[] courses = new String[3];
            double[] scores = new double[3];
            for (int j = 0; j < 3; j++) {
                System.out.print("课程" + (j + 1) + "名称：");
                courses[j] = sc.next();
                System.out.print("成绩：");
                scores[j] = sc.nextDouble();
            }
            stus[i] = (t == 1)
                    ? new Undergraduate(name, courses, scores)
                    : new Postgraduate(name, courses, scores);
        }
        for (Student s : stus) {
            System.out.println(s);
        }
    }
}
