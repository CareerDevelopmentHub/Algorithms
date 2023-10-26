package ASSIGNMENT1;

import utils.Util;

public class Q16 {
    static int iterations = 0;

    static void permute(String[] arr, int i, int length) {
        if (length == i) {
            Util.display(arr, "Array = ");
            return;
        }
        int j = i;
        for (j = i; j < length; j++) {
            Util.swap(arr, i, j);
            permute(arr, i + 1, length);
            Util.swap(arr, i, j);
        }
        return;
    }

    public static void main(String[] args) {
        String[] arr = { "a", "b", "c", "d", "e" };
        permute(arr, 0, arr.length);
    }
}
