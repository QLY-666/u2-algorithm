//子类在初始化时，第一行代码必须是调用父类的构造方法。
//如果你自己不写，编译器就会自动帮你加上一句空参数的 super();。父类如果没有空构造，子类就会报错
//要写 super(side, side)，且里面有两个 side：是因为父类的构造方法要两个参数，
//且正方形只有一个边长（side），所以只能把同一个 side 传两次，分别对应父类的宽和高。
//含参的构造方法系统不会自己生成super(),需要自己写super(参数)

//简单来说就是要先用super使父类初始化，也就是先执行父类的构造方法，才能去使用后面的成员变量，方法等，
//不含参系统就会在子类的构造方法里自带super()，而含参的父类就必须要在子类加super(参数)

package sy5;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

class Rectangle {
    double width, height;

    Rectangle(double w, double h) {
        width = w;
        height = h;
    }

    double getArea() {
        return width * height;
    }

    double getPerimeter() {
        return 2 * (width + height);
    }
}

class Square extends Rectangle {
    Square(double side) {
        super(side, side);
    }

    @Override
    double getArea() {
        return width * width;
    }

    @Override
    double getPerimeter() {
        return 4 * width;
    }
}

public class Qiumianji {
    static {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

        System.out.println("当前时间：" + now.format(formatter));
    }

    public static void main(String[] args) {
        Rectangle[] arr = {
                new Rectangle(3, 4),
                new Rectangle(5, 2),
                new Square(3),
                new Square(2.5)
        };

        System.out.println("第1个面积：" + arr[0].getArea());
        System.out.println("第2个面积：" + arr[1].getArea());
        System.out.println("第3个面积：" + arr[2].getArea());
        System.out.println("第4个面积：" + arr[3].getArea());
        }
    }
