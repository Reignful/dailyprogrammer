/**
 * Created by Josh on 15-06-01.
 */
//Description: The user inputs 3 numbers and the program takes the sum of the squares of the two larger numbers.;w

import java.util.Scanner;

public class challenge34 {
    public static void main(String args[]) {
        double num1, num2, num3;
        Scanner input = new Scanner(System.in);
        System.out.print("Please enter the first number: ");
        num1 = input.nextDouble();
        System.out.print("Please enter the second number: ");
        num2 = input.nextDouble();
        System.out.print("Please enter the third number: ");
        num3 = input.nextDouble();

        sumBiggestSquares(num1, num2, num3);

    }

    public static void sumBiggestSquares(double num1, double num2, double num3) {
        if (num1 <= num2 && num1 <= num3){
            System.out.println(Math.pow(num2, 2) + Math.pow(num3, 2));
        } else if (num2 <= num1 && num2 <= num3){
            System.out.println(Math.pow(num1, 2) + Math.pow(num3, 2));
        } else {
            System.out.println(Math.pow(num1, 2) + Math.pow(num2, 2));
        }
    }
}


