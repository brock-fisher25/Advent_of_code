import java.util.ArrayList;
import java.util.Collections;

public class Day_1 {
    public static void run(String input) {
        ArrayList<Integer> list = process_input(input);
        int[] results = new int[2];
        results[0] = first_solution(list);
        results[1] = second_solution(list);
        System.out.println("here are results for day 1");
        for (int i = 0; i < results.length; i++) {
            System.out.println(results[i]);
        }

    }
    public static int first_solution(ArrayList<Integer> list) {
        ArrayList<Integer> list1 = new ArrayList<>();
        ArrayList<Integer> list2 = new ArrayList<>();
        // create two separate lists of input values
        boolean add_list1 = true;
        for (Integer num : list) {
            if (add_list1) {
                list1.add(num);
                add_list1 = false;
            }
            else {
                list2.add(num);
                add_list1 = true;
            }
        }
        Collections.sort(list1);
        Collections.sort(list2);
        int total = 0;
        for (int i = 0; i < list1.size(); i++) {
            total += Math.abs(list1.get(i) - list2.get(i));
        }
        return total;
    }
    public static int second_solution(ArrayList<Integer> list) {
        return 0;
    }
    public static ArrayList<Integer> process_input(String input) {
        ArrayList<Integer> list = new ArrayList<>();
        String[] split = input.split("\\s+");
        for (String part: split) {
            int num = Integer.parseInt(part);
            list.add(num);
        }
        return list;
    }
}
