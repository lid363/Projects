import java.util.*;
import java.io.*;
import java.lang.*;

public class Cutoff_Ranks {
    public int cutOffRank(int cutOffRank, int num, int[] scores){
        int meetNum = 0;
        if(num < cutOffRank || 0 == cutOffRank || num != scores.length)
        {
            return 0;
        }
        if(num > 0 && num <= (int) Math.pow(10,5))
        {
            Arrays.sort(scores);
            for(int i = scores.length - 1; i > -1; i--)
            {
                if (scores[i] > 100)
                {
                    return 0;
                }
                if(scores.length - 1 == i)
                {
                    meetNum = meetNum + 1;
                }
                else
                {
                    int lastScore = scores[i+1];
                    if(lastScore == scores[i] || meetNum < cutOffRank)
                    {
                        meetNum = meetNum + 1;
                    }
                    else
                    {
                        break;
                    }
                }
            }
        }
        return meetNum;
    }

}


