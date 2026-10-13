package sy4.farm.river;
public class Sheep {
    private boolean crossRiver=false;
    private boolean hasCross=false;
    private boolean isAlive=true;
    public void showStatus() {
        System.out.println("Sheep is alive  :"+isAlive+"       Sheep has Cross  :"+hasCross);
    }
    public void eatCabbage(Cabbage cabbage,Farmer farmer) {
        if((cabbage.gethasCross()==this.hasCross)&&(farmer.gethasCross()!=this.hasCross))
            cabbage.setisAlive(!(cabbage.getisAlive()));
    }
    public void setcrossRiver(boolean a) {
        crossRiver=a;
    }
    public void sethasCross(boolean a) {
        hasCross=a;
    }
    public void setisAlive(boolean a) {
        isAlive=a;
    }
    public boolean getcrossRiver() {
        return  crossRiver;
    }
    public boolean gethasCross() {
        return  hasCross;
    }
    public boolean getisAlive() {
        return  isAlive;
    }
}
