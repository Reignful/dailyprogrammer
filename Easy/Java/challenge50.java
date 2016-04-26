/**
 * Created by Josh on 15-06-12.
 *
/
import java.util.Arrays;

public class challenge50 {
    public static void main(String[] args) {
        //Test Cases
        int C = 8;
        int[] L = {2, 1, 9, 4,4, 56, 90, 3};
        System.out.println( Arrays.toString(findStoreCredit(C, L)) );
    }
    public static int[] findStoreCredit (int C, int[] L) {
        //Create an array to return the answer.
        int[] answer = new int [2];
        //Goes through the array, checks if any two numbers add up to C.
        for (int i = 0; i < L.length; i++) {
            for (int k = i + 1; k < L.length; k++) {
                if (L[i] + L[k] == C) {
                    //Adds index of the sum to an array.
                    answer[0] = i + 1;
                    answer[1] = k + 1;
                    return answer;
                }
            }
        }
        return answer;
    }
}
