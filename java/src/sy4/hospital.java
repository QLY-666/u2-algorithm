package sy4;
import java.util.Date;

    class Patient {
    private String name;
    private String sex;
    private String address;
    private int birthyear;
    private int birthmonth;

    //无参构造方法
    public  Patient() {

    }
    //含参构造方法
    public Patient(String name,String sex,int birthyear,int birthmonth,String address) {
        this.name = name;
        this.sex = sex;
        this.birthmonth =  birthmonth;
        this.birthyear = birthyear;
        if (address == null) {
            this.address = "";
        } else {
            this.address = address;
        }
    }

    //set-get 方法
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getSex() { return sex; }
    public void setSex(String sex) { this.sex = sex; }

    public int getBirthYear() { return birthyear; }
    public void setBirthYear(int birthYear) { this.birthyear = birthyear; }

    public int getBirthMonth() { return birthmonth; }
    public void setBirthMonth(int birthmonth) { this.birthmonth = birthmonth; }

    public String getAddress() { return address; }
    public void setAddress(String address) {
        if (address == null) {
        this.address = "";
    } else {
            this.address = address;
        }
    }
}

    class Doctor {
    private String name;
    private String sex;
    private String title;
    private int birthYear;
    private int birthMonth;
    private String education;

        //无参构造方法
    public Doctor() {

    }

    //含参构造方法
    public Doctor(String name, String sex, String title, int birthYear, int birthMonth, String education) {
        this.name = name;
        this.sex = sex;
        this.title = title;
        this.birthYear = birthYear;
        this.birthMonth = birthMonth;
        this.education = education;
    }

    // set-get 方法
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getSex() { return sex; }
    public void setSex(String sex) { this.sex = sex; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public int getBirthYear() { return birthYear; }
    public void setBirthYear(int birthYear) { this.birthYear = birthYear; }

    public int getBirthMonth() { return birthMonth; }
    public void setBirthMonth(int birthMonth) { this.birthMonth = birthMonth; }

    public String getEducation() { return education; }
    public void setEducation(String education) { this.education = education; }
}

    class Register {
    private Patient patient;
    private Doctor doctor;
    private Date registerDate;
    double registerFee;

    public void RegisterPatient(Patient patient,Doctor doctor,double registerFee) {
        this.patient = patient;
        this.doctor = doctor;
        this.registerDate = new Date();
        this.registerFee = registerFee;
    }
}

    public class hospital {
        public static void main(String[] args) {
            Patient p = new Patient("张三", "男", 2000, 5, null);
            Doctor d = new Doctor("李医生", "女", "主任医师", 1975, 8, "博士");
            Register r = new Register();
            r.RegisterPatient(p, d, 50.0);
            System.out.println("病人：" + p.getName() + "，住址：" + p.getAddress());
            System.out.println("医生：" + d.getName() + "，职称：" + d.getTitle());
            System.out.println("挂号费：" + r.registerFee);
        }
    }