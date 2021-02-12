//Author:       Danhong Li
//Date:         12/13/2020
//Description:  Add, Edit Ship, curise, and passenger. 
//				Also print ship name, ship in service list, ship full list
//				cruise list, cruise details, and passenger list.

import java.util.ArrayList;
import java.util.Scanner;

public class driver {
    public static void main(String[] args) {

        ArrayList<Ship> ships = new ArrayList<>();
        ArrayList<Cruise> cruises = new ArrayList<>();
        ArrayList<Passenger> passengers = new ArrayList<>();

        // Some Sample data

        // ship
        Ship shipA = new Ship("Viking Sun",true,200,150,88,100,50);
        Ship shipB = new Ship("Viking Orion",false,300,120,66,60,30);
        Ship shipC = new Ship("Viking Sea",true,350,160,99,70,50);
        ships.add(shipA);
        ships.add(shipB);
        ships.add(shipC);
        // cruise
        Cruise cruiseA = new Cruise("Western Mediterranean", "Rome,Pisa,Cannes,Palma,Barcelona,Naples,Rome",shipA);
        Cruise cruiseB = new Cruise("Greek Isles & Italy","Rome,Kotor,Corfu,Naples,Pisa,Roma",shipA);
        Cruise cruiseC = new Cruise("Bermuda","New York,Royal Naval Dockyard,New York",shipC);
        cruises.add(cruiseA);
        cruises.add(cruiseB);
        cruises.add(cruiseC);
        // passenger
        Passenger passengerA = new Passenger("Haniya Daly","view",cruiseA);
        Passenger passengerB = new Passenger("Karim Alford","ocean",cruiseB);
        Passenger passengerC = new Passenger("Esme Huber","suite",cruiseC);
        passengers.add(passengerA);
        passengerA.cruise.ship.bookView();
        passengers.add(passengerB);
        passengerB.cruise.ship.bookOcean();
        passengers.add(passengerC);
        passengerC.cruise.ship.bookSuite();
        // Sample end

        Scanner scanner = new Scanner(System.in);
        String select;
        do{
            displayMenu();
            select = scanner.nextLine();
            switch (select){
                case "1":
                    try{
                        Ship ship = createShip();
                        ships.add(ship);
                        System.out.println("Add Ship successfully!");
                    }catch (Exception e) {
                        System.out.println("***** Enter invalid! Check your input! *****");
                    }
                    break;
                case "2":
                    try{
                        editShip(ships);
                    }catch (Exception e){
                        System.out.println("***** Enter invalid! Check your input! *****");
                    }
                    break;
                case "3":
                    try{
                        Cruise cruise = createCruise();
                        cruises.add(cruise);
                        System.out.println("Add Cruise successfully!");
                    }catch (Exception e){
                        System.out.println("***** Enter invalid! Check your input! *****");
                    }
                    break;
                case "4":
                    try{
                        editCruise(cruises);
                    }catch (Exception e){
                        System.out.println("***** Enter invalid! Check your input! *****");
                    }
                    break;
                case "5":
                    try{
                        Passenger passenger = createPassenger();
                        cruises.add(passenger);
                        System.out.println("Add Cruise successfully!");
                    }catch (Exception e){
                        System.out.println("***** Enter invalid! Check your input! *****");
                    }
                    break;
                case "6":
                    try{
                        editPassenger(passengers);
                    }catch (Exception e){
                        System.out.println("***** Enter invalid! Check your input! *****");
                    }
                    break;
                case "A":
                    printAllshipsName(ships);
                    break;
                case "B":
                    printAllshipsInservice(ships);
                    break;
                case "C":
                    printAllships(ships);
                    break;
                case "D":
                    printAllcruisesShow(cruises);
                    break;
                case "E":
                    printAllcruises(cruises);
                    break;
                case "F":
                    printAllpassengers(passengers);
                    break;
            }
        }while (!select.equals("x"));


    }
    public static void displayMenu(){
        System.out.println("");
        System.out.println("");
        System.out.println ( "\t\t\tLuxury Ocean Cruise Outings" );
        System.out.println ( "\t\t\t\t\tSystem Menu\n" );
        System.out.println ( "[1] Add Ship            [A] Print Ship Names" );
        System.out.println ( "[2] Edit Ship           [B] Print Ship In Service List" );
        System.out.println ( "[3] Add Cruise          [C] Print Ship Full List" );
        System.out.println ( "[4] Edit Cruise         [D] Print Cruise List" );
        System.out.println ( "[5] Add Passenger       [E] Print Cruise Details" );
        System.out.println ( "[6] Edit Passenger      [F] Print Passenger List" );
        System.out.println ( "[x] Exit System" );
        System.out.println ( "\nEnter a menu selection: " );
    }
    public static Ship createShip(){
        Scanner scanner = new Scanner(System.in);
        Ship s = new Ship();
        System.out.println("Enter the name of the ship:");
        s.setShipName(scanner.nextLine());
        System.out.println("Is this ship In Service(Type in ture or false):");
        s.setInService(scanner.nextBoolean());
        System.out.println("The number of Balcony Cabin is:");
        s.setNumBalcony(scanner.nextInt());
        System.out.println("The number of Ocean Cabin is:");
        s.setNumOcean(scanner.nextInt());
        System.out.println("The number of View Cabin is:");
        s.setNumView(scanner.nextInt());
        System.out.println("The number of Suite Cabin is:");
        s.setNumSuite(scanner.nextInt());
        System.out.println("The number of Interior Cabin is:");
        s.setNumInterior(scanner.nextInt());
        System.out.println(s.toString());
        return s;
    }
    // add function
    public static Cruise createCruise(){
        Scanner scanner = new Scanner(System.in);
        Cruise c = new Cruise();
        System.out.println("The name of cruise is:");
        c.setCruiseName(scanner.nextLine());
        System.out.println("The ports of call is:");
        c.setPorts(scanner.nextLine());
        System.out.println("The ship name is:");
        c.setShipName(scanner.nextLine());
        return c;
    }
    public static Passenger createPassenger(){
        Scanner scanner = new Scanner(System.in);
        Passenger p = new Passenger();
        System.out.println("The name of passenger is:");
        p.setPassengerName(scanner.nextLine());
        System.out.println("The cabin is:");
        p.setPassengerCabin(scanner.nextLine());
        System.out.println("The cruise is:");
        p.setCruiseName(scanner.nextLine());
        return p;
    }
    public static void editShip(ArrayList<Ship> ships){
        printAllships(ships);
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number you would like to edit:");
        int n = scanner.nextInt();
        Ship s = createShip();
        ships.set(n-1, s);
    }
    // edit function
    public static void editCruise(ArrayList<Cruise> cruises){
        printAllcruises(cruises);
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number you would like to edit:");
        int n = scanner.nextInt();
        Cruise c = createCruise();
        cruises.set(n-1,c);
    }
    public static void editPassenger(ArrayList<Passenger> passengers){
        printAllpassengers(passengers);
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number you would like to edit:");
        int n = scanner.nextInt();
        Passenger p = createPassenger();
        passengers.set(n-1,p);
    }
    // print all
    public static void printAllships(ArrayList<Ship> ships){
        int i = 1;
        for (Ship s:ships) {
            System.out.println(i);
            System.out.println(s.toString());
            i++;
        }
    }
    public static void printAllcruises(ArrayList<Cruise> cruises){
        int i = 1;
        for (Cruise c:cruises) {
            System.out.println(i);
            System.out.println(c.toString());
            i++;
        }
    }
    public static void printAllpassengers(ArrayList<Passenger> passengers){
        int i = 1;
        for (Passenger p:passengers) {
            System.out.println(i);
            System.out.println(p.toString());
            i++;
        }
    }
    // print all ships name
    public static void printAllshipsName(ArrayList<Ship> ships){
        int i = 1;
        for (Ship s:ships) {
            System.out.println(i);
            System.out.println(s.getShipName());
            i++;
        }
    }
    // print all ships in service
    public static void printAllshipsInservice(ArrayList<Ship> ships){
        int i = 1;
        for (Ship s:ships) {
            if (s.isInService()){
                System.out.println(i);
                System.out.println(s.toString());
                i++;
            }
        }
    }
    // print all cruise list
    public static void printAllcruisesShow(ArrayList<Cruise> cruises){
        int i = 1;
        for (Cruise c:cruises) {
            System.out.println(i);
            System.out.println(c.show());
            i++;
        }
    }
}