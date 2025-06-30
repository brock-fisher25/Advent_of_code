import java.util.ArrayList;

public class Day_7 {
    public static void run(String input) {
        String[] inputs = process_input(input);
        long[] results = new long[2];
        results[0] = first_solution(inputs);
        results[1] = second_solution(inputs);
        System.out.println("here are results for day 7");
        for (int i = 0; i < results.length; i++) {
            System.out.println(results[i]);
        }
        System.out.println("");
    }
    public static long first_solution(String[] inputs) {
        long total = 0;
        long target = 0;
        for (String line: inputs) {
            String[] string_nums = line.split(" ");
            long[] nums = new long[string_nums.length - 1];
            target = Long.parseLong(string_nums[0].replace(":",""));
            int j = 0;
            for (int i = 1; i < string_nums.length; i++) {
                nums[j++] = Long.parseLong(string_nums[i].trim());
            }
            // build list of every possible combination of operators
            ArrayList<String> combinations = new ArrayList<>();
            char[] operators = {'+', '*'};
            int total_combos = (int) Math.pow(operators.length, string_nums.length - 1);
            for (int i = 0; i < total_combos; i++) {
                StringBuilder sb = new StringBuilder();
                int current = i;

                for (int pos = 0; pos < string_nums.length - 1; pos++) {
                    int index = current % operators.length;
                    sb.insert(0, operators[index]);
                    current /= operators.length;
                }
                combinations.add(sb.toString());
            }
            // try each combo of operators until one works
            long ans = 0;
            for (String combo: combinations) {
                ans = nums[0];
                for (int i = 1; i < nums.length; i++) {
                    if (combo.charAt(i-1) == '+') {
                        ans += nums[i];
                    }
                    else {
                        ans *= nums[i];
                    }
                }
                if (ans == target) {
                    total += ans;
                    break;
                }
            }
        }
        return total;
    }
    public static long second_solution(String[] inputs) {
        long total = 0;
        long target = 0;
        for (String line: inputs) {
            String[] string_nums = line.split(" ");
            long[] nums = new long[string_nums.length - 1];
            target = Long.parseLong(string_nums[0].replace(":",""));
            int j = 0;
            for (int i = 1; i < string_nums.length; i++) {
                nums[j++] = Long.parseLong(string_nums[i].trim());
            }
            // build list of every possible combination of operators
            ArrayList<String> combinations = new ArrayList<>();
            char[] operators = {'+', '*', '|'};
            int total_combos = (int) Math.pow(operators.length, string_nums.length - 1);
            for (int i = 0; i < total_combos; i++) {
                StringBuilder sb = new StringBuilder();
                int current = i;

                for (int pos = 0; pos < string_nums.length - 1; pos++) {
                    int index = current % operators.length;
                    sb.insert(0, operators[index]);
                    current /= operators.length;
                }
                combinations.add(sb.toString());
            }
            // try each combo of operators until one works
            long ans = 0;
            for (String combo: combinations) {
                ans = nums[0];
                for (int i = 1; i < nums.length; i++) {
                    if (combo.charAt(i-1) == '+') {
                        ans += nums[i];
                    }
                    else if (combo.charAt(i-1) == '|') {
                        String part1 = String.valueOf(ans);
                        String part2 = String.valueOf(nums[i]);
                        String combined = part1 + part2;
                        ans = Long.parseLong(combined);
                    }
                    else {
                        ans *= nums[i];
                    }
                }
                if (ans == target) {
                    total += ans;
                    break;
                }
            }
        }
        return total;
    }
    public static String[] process_input(String input) {
        String[] results = input.split("\\n");
        return results;
    }
}