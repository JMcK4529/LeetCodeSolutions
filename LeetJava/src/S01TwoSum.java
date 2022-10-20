/* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. */

import Resources.Printer;       // Opting to import my own method for Array -> String, 
//import java.util.Arrays;

public class S01TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] answer = new int[2];
        for (int i = 0; i < nums.length; i++) {         // Iterate through every pair of values
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i]+nums[j] == target) {        // Check if they sum to the target
                    answer[0] = i;                      
                    answer[1] = j;                      
                    break;                              // If yes, stop the loop
                }
            }
        }
        return answer;                                  // Return the answer in the form [i,j]
    }

    // From here on is debugging work, including tests for the method.
    public static void main(String[] args) {
        S01TwoSum sol = new S01TwoSum();

        int[][] answers = new int[3][5];
        int[] targets = new int[3];
        answers[0] = new int[] {2,7,11,15};
        targets[0] = 9;
        answers[1] = new int[] {3,2,4,0,0};
        targets[1] = 6;
        answers[2] = new int[] {3,3,0,0,0};
        targets[2] = 6;

        for (int i = 0; i < answers.length; i++) {
            System.out.println(Printer.printIntArray(sol.twoSum(answers[i], targets[i])));  // Using my own method for Array -> String
            //System.out.println(Arrays.toString(sol.twoSum(answers[i], targets[i])));      // This would be the usual toString method
        }
    }
}