package sy2;

public class RenShuTongJi
{
    public static void main(String args[])
    {
        String[] keshi = {"内科","外科","妇科","儿科","口腔科","骨科"};
        int[] patients ={60,27,42,63,19,31};
        System.out.println("科室名：人数");
        for(int i=0;i<keshi.length;i++){
            System.out.println(keshi[i]+":"+patients[i]);
        }
        int max=0;
        for(int i=1;i<keshi.length;i++){
            if(patients[i]>patients[max]) max = i;
        }
        System.out.print("最多人的科室是："+keshi[max]);


    }
}