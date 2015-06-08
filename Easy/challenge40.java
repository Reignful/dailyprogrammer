/**
 * Created by Josh on 15-06-08.
 */

//Description: Print the numbers from 1 - 1000 without using any loops
public class challenge40 {
    public static void printNum(int num) {
        //Base case
        if (num <= 1000) {
            //Prints out the current number
            System.out.println(num);
            printNum(num + 1);
        }
    }

    public static void main(String[] args) {
        printNum(1);
    }
}
