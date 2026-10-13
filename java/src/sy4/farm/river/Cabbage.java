package sy4.farm.river;

public class Cabbage {
    private boolean crossRiver=false;
    private boolean hasCross=false;
    private boolean isAlive=true;
    public void showStatus() {
        System.out.println("cabbage is alive  :"+isAlive+"       cabbage has Cross  :"+hasCross);
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
