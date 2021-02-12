public class Passenger extends Cruise{
    private String passengerName;
    private String passengerCabin;
    protected Cruise cruise;

    public Passenger(){
    }
    public Passenger(String passengerName, String passengerCabin, Cruise cruise) {
        this.passengerName = passengerName;
        this.passengerCabin = passengerCabin;
        this.cruise = cruise;
    }

    public String getPassengerName() {
        return passengerName;
    }

    public void setPassengerName(String passengerName) {
        this.passengerName = passengerName;
    }

    public String getPassengerCabin() {
        return passengerCabin;
    }

    public void setPassengerCabin(String passengerCabin) {
        this.passengerCabin = passengerCabin;
    }

    public Cruise getCruise() {
        return cruise;
    }

    public void setCruise(Cruise cruise) {
        this.cruise = cruise;
    }

    @Override
    public String toString() {
        return "Passenger{" +
                "passengerName='" + passengerName + '\'' +
                ", passengerCabin='" + passengerCabin + '\'' +
                ", cruise=" + cruise +
                '}';
    }
}