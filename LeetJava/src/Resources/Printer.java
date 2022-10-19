package Resources;

public class Printer {
    public static String printIntArray(int[] arr) {
        String retString = "[";
        for (int i = 0; i < arr.length-1; i++) {
            retString += arr[i];
            retString += ",";
        }
        retString += arr[arr.length-1];
        retString += "]";
        return retString;
    }

    public static String printIntArray(int[][] arr) {
        String retString = "[";
        for (int i = 0; i < arr.length-1; i++) {
            retString += printIntArray(arr[i]);
            retString += ",";
        }
        retString += printIntArray(arr[arr.length-1]);
        retString += "]";
        return retString;
    }
}
