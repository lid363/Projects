public class Cruise extends Ship{
    private String cruiseName;
    private String ports;
    protected Ship ship;

    public Cruise() {
    }

    public Cruise(String cruiseName, String ports, Ship ship) {
        this.cruiseName = cruiseName;
        this.ports = ports;
        this.ship = ship;
    }

    public String getCruiseName() {
        return cruiseName;
    }

    public void setCruiseName(String cruiseName) {
        this.cruiseName = cruiseName;
    }

    public String getPorts() {
        return ports;
    }

    public void setPorts(String ports) {
        this.ports = ports;
    }

    public Ship getShip() {
        return ship;
    }

    public void setShip(Ship ship) {
        this.ship = ship;
    }

    public String show() {
        return "Cruise{" +
                "cruiseName='" + cruiseName + '\'' +
                ", ports='" + ports + '\'' +
                '}';
    }

    @Override
    public String toString() {
        return "Cruise{" +
                "cruiseName='" + cruiseName + '\'' +
                ", ports='" + ports + '\'' +
                ", ship=" + ship +
                '}';
    }
}