/* Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.
Mapping:
2 -> a,b,c
3 -> d,e,f
4 -> g,h,i
5 -> j,k,l
6 -> m,n,o
7 -> p,q,r,s
8 -> t,u,v
9 -> w,x,y,z
Note that 1 does not map to any letters.
*/

/* length of array = n0*n1*n2*n3
* where ni is the number of characters mapped to the ith digit
* 
* e.g. digits = "274"
* [apd,ape,apf,aqd,aqe,aqf,ard,are,arf,asd,ase,asf,
* bpd,bpe,bpf,bqd,bqe,bqf,brd,bre,brf,bsd,bse,bsf,
* cpd,cpe,cpf,cqd,cqe,cqf,crd,cre,crf,csd,cse,csf]
* 
* Algorithm:
* for first digit, do n0*n1*n2*n3/n0 of each in a row
* for second digit, do n0*n1*n2*n3/n0*n1 of each in a row
* for third digit, do n0*n1*n2*n3/n0*n1*n2 of each in a row
* for fourth digit, do 1 of each in a row
*/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class S17LetterCombinationsOfAPhoneNumber {
    public List<String> letterCombinations(String digits) {
        
        // Here's a phone keypad as a HashMap
        Map<Character, String[]> keypadMap = new HashMap<Character, String[]>() {{
            put('2',new String[] {"a","b","c"});
            put('3',new String[] {"d","e","f"});
            put('4',new String[] {"g","h","i"});
            put('5',new String[] {"j","k","l"});
            put('6',new String[] {"m","n","o"});
            put('7',new String[] {"p","q","r","s"});
            put('8',new String[] {"t","u","v"});
            put('9',new String[] {"w","x","y","z"});
        }};

        // Some maths calculating the number of possible combinations of strings
        // and therefore the length of the array
        int[] n = new int[digits.length()];
        for (int i = 0; i < digits.length(); i++) {
            n[i] = keypadMap.get(digits.charAt(i)).length;
        }
        
        int nTotal = 1;
        for (int i = 0; i < n.length; i++) {
            nTotal *= n[i];
        }

        // Now make a String array of that length
        // (We are working in a String[] for ease of operations like concatenating at each index)
        String[] possibleStrings = new String[nTotal];

        // For each spot in the array, add the right letters from the HashMap
        // They are stored in the HashMap as str, NOT char, so we are concatenating strings
        
        /*
        With di[] representing the String[] in the HashMap which corresponds to the char 'di'
        And di is the ith digit in the digits variable

        We need to put the following into the array

        {
        n1*n2*n3 lots of d0[0]
        n1*n2*n3 lots of d0[1]
        n1*n2*n3 lots of d0[2]
        n1*n2*n3 lots of d0[3]
        }

        {
        n2*n3 lots of d1[0]
        n2*n3 lots of d1[1]
        n2*n3 lots of d1[2]
        n2*n3 lots of d1[3]
        }
        n1 times (each time + n1*n2*n3 to starting arrayindex)

        {
        n3 of d2[0]
        n3 of d2[1]
        n3 of d2[2]
        n3 of d2[3]
        }
        n1*n2 times (each time + n2*n3 to starting arrayindex)

        {
        1 of d3[0]
        1 of d3[1]
        1 of d3[2]
        1 of d3[3]
        }
        n1*n2*n3 times (each time + n3 to starting arrayindex)
         */

        for (int i = 0; i < possibleStrings.length; i++) {
            if (digits.length() >= 1) {
                for (int j = 0; j < keypadMap.get(digits.charAt(0)).length; j++) {
                    if ( (i >= j*nTotal/n[0]) && (i < (j+1)*nTotal/n[0])) {
                        possibleStrings[i] = keypadMap.get(digits.charAt(0))[j];
                    }
                }
            }

            if (digits.length() >= 2) {
                for (int j = 0; j < keypadMap.get(digits.charAt(1)).length; j++) {
                    for (int k = 0; k < n[1]; k++){
                        if ( (i >= j*nTotal/(n[0]*n[1]) + k*(nTotal/n[0])) && (i < (j+1)*nTotal/(n[0]*n[1]) + k*(nTotal/n[0])) ) {
                            possibleStrings[i] += keypadMap.get(digits.charAt(1))[j];
                        }
                    }
                }
            }

            if (digits.length() >= 3) {
                for (int j = 0; j < keypadMap.get(digits.charAt(2)).length; j++) {
                    for (int k = 0; k < n[1]*n[2]; k++)
                    if ( (i >= j*nTotal/(n[0]*n[1]*n[2]) + k*(nTotal/(n[0]*n[1]))) && (i < (j+1)*nTotal/(n[0]*n[1]*n[2]) + k*(nTotal/(n[0]*n[1]))) ) {
                        possibleStrings[i] += keypadMap.get(digits.charAt(2))[j];
                    }
                }
            }

            if (digits.length() >= 4) {
                for (int j = 0; j < keypadMap.get(digits.charAt(3)).length; j++) {
                    for (int k = 0; k < n[1]*n[2]*n[3]; k++) {
                        if ( (i >= j + k*(nTotal/(n[0]*n[1]*n[2]))) && (i < (j+1) + k*(nTotal/(n[0]*n[1]*n[2])))) {
                            possibleStrings[i] += keypadMap.get(digits.charAt(3))[j];
                        }
                    }
                }
            }
        }

        // Convert to List<String> for the correct output type
        List<String> possibleStringsList = new ArrayList<String>(Arrays.asList(possibleStrings));

        // Return the list
        return possibleStringsList;
    }

    public static void main(String[] args) {
        S17LetterCombinationsOfAPhoneNumber sol = new S17LetterCombinationsOfAPhoneNumber();
        String[] tests = new String[] {"23","","2","3789"};
        for (int i = 0; i < tests.length; i++) {
            System.out.println(String.join(", ", sol.letterCombinations(tests[i])));
        }
    }
}