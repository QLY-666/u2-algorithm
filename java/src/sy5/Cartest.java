package sy5;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

class Vehicle {
    int wheels;
    double weight;

    public void display() {
        System.out.println("车轮数：" + wheels + " 车重：" + weight);
    }
}

class Car extends Vehicle{
    int loader;

    public void display() {
        super.display();
        System.out.println("限载人数：" + loader);
    }
}

class Trunk extends Car{
    double payload;

    public void display() {
        super.display();
        System.out.println("限载重量：" + payload);
    }
}

public class Cartest {
    static {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

        System.out.println("当前时间：" + now.format(formatter));
    }

    public static void main(String args[]){
        Vehicle v = new Vehicle();
        v.wheels=4;
        v.weight=1.5;
        System.out.println("汽车：");
        v.display();
        System.out.println("");

        Car c = new Car();
        c.wheels=4;
        c.weight=2.0;
        c.loader =5;
        System.out.println("小汽车：");
        c.display();
        System.out.println("");

        Trunk t = new Trunk();
        t.wheels=10;
        t.weight=15;
        t.loader=2;
        t.payload=30.0;
        System.out.println("卡车：");
        t.display();
    }
}