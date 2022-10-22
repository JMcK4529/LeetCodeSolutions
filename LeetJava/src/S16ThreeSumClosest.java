/* Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
 */

/* Constraints:
3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4
 */

// Standard imports
import java.util.Arrays;
import java.lang.Math;

// Class named to fit filing system
public class S16ThreeSumClosest {
    public int threeSumClosest(int[] nums, int target) {
        // Initial declarations
        int[] closestTriplet = new int[] {0,0,0};       // The closest triplet match found so far
        int closestSum = 20001;                         // Starting with a closestSum which is higher than any possible value
                                                        // given the constraints on nums and target
        int[] currentTriplet = new int[3];              // The current triplet being considered
        int currentSum;                                 // The sum of currentTriplet's values

        for (int i = 0; i < nums.length-2; i++) {       // Iterate through each possible triplet
            currentTriplet[0] = nums[i];                // Adding each value to the currentTriplet as we go

            for (int j = i+1; j < nums.length-1; j++) {
                currentTriplet[1] = nums[j];

                for (int k = j+1; k < nums.length; k++) {
                    currentTriplet[2] = nums[k];

                    currentSum = Arrays.stream(currentTriplet).sum();        // Update currentSum

                    if (Math.abs(currentSum-target) < (closestSum-target)) { // If the currentSum is closer to the target than the closestSum
                        for (int z = 0; z < closestTriplet.length; z++) {    // Then update closestTriplet...
                            closestTriplet[z] = currentTriplet[z];
                        }
                        closestSum = Arrays.stream(closestTriplet).sum();    // ... and update closestSum
                    } else {}
                }

            }

        }

        return closestSum;  // Return the closestSum found
    }

    // From here on is debugging work, including tests for the method.
    public static void main(String[] args) {
        S16ThreeSumClosest sol = new S16ThreeSumClosest();
        int[][] tests = new int[][] {{-1,2,1,-4},{0,0,0}};
        int[] targets = new int[] {1,1};
        for (int x = 0; x < tests.length; x++) {
            System.out.println(sol.threeSumClosest(tests[x],targets[x]));
        }
    }
}
