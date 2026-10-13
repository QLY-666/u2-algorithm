package sy3;//todo 因为country是stastic变量，所以任何方法对country修改的结果是一样的，即三个person都是共用一个country
//todo 如果不用stastic，那就相当于p1 =中国，而p2 p3没有分配到，即为NULL，需要自己添加像是p2 =。。。。
//todo p3没有country但能赋值是因为语法糖
//todo p2/3这样只有两个参数但能赋值到中国是因为java会自己找country

class Person {
    //姓名
    String name;
    //年龄
    int age;
    //国籍
    //String country;
    static String country;

    public Person(){}

    public Person(String name,int age) {
        this.name = name;
        this.age = age;
    }

    public Person(String name,int age,String country) {
        this.name = name;
        this.age = age;
        this.country = country;
    }

    public void show() {
        System.out.println("姓名："+name+",年龄："+age+",国籍："+country);
    }
}

class PersonDemo {
    public static void main(String[] args) {
        //创建对象1
        Person p1 = new Person("王者",16,"中国");
        p1.show();

        //创建对象2
        Person p2 = new Person("普京",52);
        p2.show();

        //创建对象3
        Person p3 = new Person("拜登",70);
        p3.show();

        p3.country = "中国";
        p3.show();

        p1.show();
        p2.show();
    }
}