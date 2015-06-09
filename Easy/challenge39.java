/**
 * Created by Josh on 15-06-08.
 */

/*Description: Write a function that displays the numbers from 1 to an input parameter n
if the current number is divisible by 3 the function should write "Fizz" and if the function is
divisible by 5 the function should write "Buzz".  If the number is divisible by both write "FizzBuzz"
*/

import java.util.Scanner;

public class challange39 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        System.out.print("Please enter a number: ");
        int n = input.nextInt();

        for (int i = 0; i <= n; i++){
            //Output a phrase depending if dividable by a certain number.
            System.out.println(i % 3  == 0 && i % 5 == 0 ? "FizzBuzz" : i % 3 == 0 ? "Fizz" : i % 5 == 0 ? "Buzz" : i );
        }
    }
}
