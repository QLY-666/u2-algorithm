package sy4.farm.river;
public class Farmer {
    private boolean crossRiver=false;
    private boolean hasCross=false;
    public void showStatus() {
        System.out.println("Farmer has Cross  :"+hasCross);
    }
    public void setcrossRiver(boolean a) {
        crossRiver=a;
    }
    public void sethasCross(boolean a) {
        hasCross=a;
    }
    public boolean getcrossRiver() {
        return  crossRiver;
    }
    public boolean gethasCross() {
        return  hasCross;
    }
}
