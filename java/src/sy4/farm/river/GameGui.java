package sy4.farm.river;
public class GameGui {
    public void menu() {
        /* 显示菜单 */
        System.out.println("==================Please choose operation============");
        System.out.println("\t==========1:Cross the river alone===========");
        System.out.println("\t==========2:Cross the river with wolf=========");
        System.out.println("\t==========3:Cross the river with sheep============");
        System.out.println("\t==========4:Cross the river with cabbage==========");
        System.out.println("\t==========0:Quit===============");
        System.out.println("===================================================");
        System.out.println("Input the number(0~4):");
    }

    public void showStatus(Farmer farmer, Wolf wolf, Sheep sheep, Cabbage cabbage) {
        /* 输出农夫、各种动物、物品的状态（生存、位置） */
        farmer.showStatus();
        wolf.showStatus();
        sheep.showStatus();
        cabbage.showStatus();
    }
}