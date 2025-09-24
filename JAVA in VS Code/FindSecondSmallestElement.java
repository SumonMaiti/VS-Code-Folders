import java.util.*;

class FindElement {

    int second_small, index = 0, index2 = 0;

    int secondSmallest(int n, int arr[]) { // method defined

        second_small = arr[0];

        for (int i = 0; i < n; i++) {

            if (arr[i] < second_small) {

                second_small = arr[i];
                index = i;

            }
        }

        int min;
        if (index != 0)
            min = arr[0];
        else
            min = arr[1];

        for (int i = 0; i < n; i++) {

            if (arr[i] < min && i != index) {

                index2 = i;
                second_small = arr[i];

            }
        }
        return index2;
    }
}

class FindSecondSmallestElement {

    public static void main(String args[]) {

        int n, key, index;

        Scanner sc = new Scanner(System.in);

        FindElement arrob = new FindElement();

        int arr[] = new int[18];

        System.out.print("Enter no. of elements: ");
        n = sc.nextInt();

        System.out.println("Enter elements......... ");
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        index = arrob.secondSmallest(n, arr);

        for (int i = index; i < n - 1; i++)
            arr[i] = arr[i + 1];

        System.out.println("After evaluating, the final array is ..............\n");
        for (int i = 0; i < n - 1; i++)
            System.out.printf("%d ", arr[i]);

    }
}