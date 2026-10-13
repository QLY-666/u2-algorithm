package sy4.farm.river;
import java.util.Scanner;
public class Game {
    Wolf wolf;
    Sheep sheep;
    Cabbage cabbage;
    Farmer farmer;
    GameGui GameGui;

    Game() {
        wolf = new Wolf();
        sheep = new Sheep();
        cabbage = new Cabbage();
        farmer = new Farmer();
        GameGui=new GameGui();
    }

    protected void play(){
        Scanner input = new Scanner(System.in);
        int choice = 0; //用户输入选择
        boolean gameOver=false,//游戏结束标志，默认为false，代表游戏进行中，未结束
                win=false;     //游戏输赢标志，默认为false，代表未赢得游戏。
        while(!gameOver)
        {
            GameGui.menu();
            choice = input.nextInt();
            switch(choice)
            {
                case 0:
                    break;
                case 1:/* 农夫独自过河的处理 */
                    farmer.setcrossRiver(!farmer.getcrossRiver());
                    break;
                case 2:/* 农夫带狼的处理 */
                    if(farmer.gethasCross()==wolf.gethasCross()) {
                        farmer.setcrossRiver(!farmer.getcrossRiver());
                        wolf.setcrossRiver(!wolf.getcrossRiver());
                    }
                    else
                        System.out.println("操作错误，请选择有效操作！");
                    break;
                case 3:/* 农夫带羊的处理 */
                    if(farmer.gethasCross()==sheep.gethasCross()) {
                        farmer.setcrossRiver(!farmer.getcrossRiver());
                        sheep.setcrossRiver(!sheep.getcrossRiver());
                    }
                    else
                        System.out.println("操作错误，请选择有效操作！");
                    break;
                case 4:/* 农夫带白菜的处理 */
                    if(farmer.gethasCross()==cabbage.gethasCross()) {
                        farmer.setcrossRiver(!farmer.getcrossRiver());
                        cabbage.setcrossRiver(!cabbage.getcrossRiver());
                    }
                    else
                        System.out.println("操作错误，请选择有效操作！");
                    break;
            }
            if(farmer.getcrossRiver()) {
                farmer.setcrossRiver(!farmer.getcrossRiver());
                farmer.sethasCross(!farmer.gethasCross());}
            if(sheep.getcrossRiver())
            {
                sheep.setcrossRiver(!sheep.getcrossRiver());
                sheep.sethasCross(!sheep.gethasCross());
            }
            if(wolf.getcrossRiver())
            {
                wolf.setcrossRiver(!wolf.getcrossRiver());
                wolf.sethasCross(!wolf.gethasCross());
            }
            if(cabbage.getcrossRiver())
            {
                cabbage.setcrossRiver(!cabbage.getcrossRiver());
                cabbage.sethasCross(!cabbage.gethasCross());
            }
            wolf.eatSheep(sheep,farmer);//狼吃羊，如果羊不在同一边，则吃不到，如果在同一边，羊被吃
            sheep.eatCabbage(cabbage,farmer);//同上
            GameGui.showStatus(farmer,wolf,sheep,cabbage);
            if(choice==0)
                gameOver=true;
            else
                gameOver = isGameOver();
        }
        win=this.hasWin();
        if(win) {
            System.out.println("game over: you win !");
        }else {
            System.out.println("game over: you lose !");
        }
        input.close();
    }
    /*
     * 判断游戏是否结束
     * 输入：无
     * 运算：羊、白菜任一实体被吃，游戏结束，或者狼、羊、白菜均未被吃且全部渡过河，游戏结束
     * 输出：游戏结束--返回true ，未结束--返回false
     */
    public boolean isGameOver() {
        if(sheep.getisAlive()==false||cabbage.getisAlive()==false) {
            return true;
        }
        if(wolf.gethasCross()&&sheep.gethasCross()&&cabbage.gethasCross()) {
            return true;
        }
        return false;
    }
    /*
     * 判断游戏是否胜利
     * 前置条件：游戏结束
     * 输入：无
     * 运算：狼、羊、白菜均未被吃且全部渡过河，游戏胜利，否则失败
     * 输出：游戏胜利--返回true ，失败--返回false
     */
    public boolean hasWin() {
        if(sheep.getisAlive()==false||cabbage.getisAlive()==false) {
            return false;
        }
        if(wolf.gethasCross()&&sheep.gethasCross()&&cabbage.gethasCross()) {
            return true;
        }else {
            return false;
        }
    }

}
