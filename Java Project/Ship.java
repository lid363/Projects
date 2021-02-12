import java.util.List;

public class Ship {
    private String shipName;
    private boolean inService;
    private int numBalcony;
    private int numOcean;
    private int numView;
    private int numSuite;
    private int numInterior;

    List<Cruise> cruises;

    public Ship() {
    }

    public Ship(String shipName, boolean inService, int numBalcony, int numOcean, int numView, int numSuite, int numInterior) {
        this.shipName = shipName;
        this.inService = inService;
        this.numBalcony = numBalcony;
        this.numOcean = numOcean;
        this.numView = numView;
        this.numSuite = numSuite;
        this.numInterior = numInterior;
    }

    public String getShipName() {
        return shipName;
    }

    public void setShipName(String shipName) {
        this.shipName = shipName;
    }

    public boolean isInService() {
        return inService;
    }

    public void setInService(boolean inService) {
        this.inService = inService;
    }

    public int getNumBalcony() {
        return numBalcony;
    }

    public void setNumBalcony(int numBalcony) {
        this.numBalcony = numBalcony;
    }

    public int getNumOcean() {
        return numOcean;
    }

    public void setNumOcean(int numOcean) {
        this.numOcean = numOcean;
    }

    public int getNumView() {
        return numView;
    }

    public void setNumView(int numView) {
        this.numView = numView;
    }

    public int getNumSuite() {
        return numSuite;
    }

    public void setNumSuite(int numSuite) {
        this.numSuite = numSuite;
    }

    public int getNumInterior() {
        return numInterior;
    }

    public void setNumInterior(int numInterior) {
        this.numInterior = numInterior;
    }

    public List<Cruise> getCruises() {
        return cruises;
    }

    public void setCruises(List<Cruise> cruises) {
        this.cruises = cruises;
    }

    @Override
    public String toString() {
        return "Ship{" +
                "shipName='" + shipName + '\'' +
                ", inService=" + inService +
                ", numBalcony=" + numBalcony +
                ", numOcean=" + numOcean +
                ", numView=" + numView +
                ", numSuite=" + numSuite +
                ", numInterior=" + numInterior +
                ", cruises=" + cruises +
                '}';
    }
    public void bookBalcony(){
        if (this.numBalcony>=1){
            this.numBalcony -= 1;
        }else {
            System.out.println("Cabin is full!");
        }
    }
    public void bookOcean(){
        if (this.numOcean>=1){
            this.numOcean -= 1;
        }else {
            System.out.println("Cabin is full!");
        }
    }public void bookView(){
        if (this.numView>=1){
            this.numView -= 1;
        }else {
            System.out.println("Cabin is full!");
        }
    }public void bookSuite(){
        if (this.numSuite>=1){
            this.numSuite -= 1;
        }else {
            System.out.println("Cabin is full!");
        }
    }public void bookInterior(){
        if (this.numInterior>=1){
            this.numInterior -= 1;
        }else {
            System.out.println("Cabin is full!");
        }
    }
}