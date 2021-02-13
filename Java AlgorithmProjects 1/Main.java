

public class Main {
    public static void main(String[] args) {

        int cutOffRank = 3;
        int num = 4;
        int[] scores = {100, 50, 50, 25};
        Cutoff_Ranks c = new Cutoff_Ranks();

        System.out.println(c.cutOffRank(cutOffRank, num, scores ));

    }
    }
