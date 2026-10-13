package sy4.farm.river;

public class Wolf {
    private boolean crossRiver=false;
    private boolean hasCross=false;
    private boolean isAlive=true;
    public void showStatus() {
        System.out.println("Wolf is alive  :"+isAlive+"       Wolf has Cross  :"+hasCross);
    }
    public void eatSheep(Sheep sheep,Farmer farmer) {
        if((sheep.gethasCross()==this.hasCross)&&(farmer.gethasCross()!=this.hasCross))
            sheep.setisAlive(!sheep.getisAlive()) ;
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
