import java.util.Arrays;

/**
 * Created by Josh on 15-06-14.
 */
public class challenge62 {
    public static void main(String[] args) {
        double t = 98.2, sum = 0;
        int k = 3;

        double[] list  = {18.1, 55.1, 91.2, 74.6, 73.0, 85.9, 73.9, 81.4, 87.1, 49.3, 88.8, 5.7, 26.3, 7.1, 58.2, 31.7, 5.8, 76.9, 16.5, 8.1, 48.3, 6.8, 92.4, 83.0, 19.6};
        //Sorted the list
        Arrays.sort(list);
        //Created a copy of the array list with lowest k elements
        double[] sortedList = Arrays.copyOfRange(list,0,k);
        for (double i: sortedList) {
            //Loop through all elements of sortedList and sum them
            sum += i
        }
        if (sum < t) {
            System.out.println("There is a subset of numbers who's sum is " + sum + " and less than " + t);
        } else {
            System.out.println("There is no subset of numbers who's sum is less than " + t);
        }

    }
}
