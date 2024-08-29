import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        // n(n+1)/2  => 2*X <= n(n+1) 인 부분 찾으면 해당 라인에 있다. (n-1)n 을 빼고 남은 값에다가 n-left+1 를 분모로 +1+left를 분자로
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        Stack<Integer> stack = new Stack<>();

        for ( int i = 1; i<=n; i++) {
            String[] callNum = br.readLine().split(" ");

            int num = Integer.parseInt(callNum[0]);
            if (num == 0){
                stack.pop();
            } else {
                stack.push(num);
            }
        }
        int sum = 0;
        for (int value : stack) {
            sum += value;
        }

        System.out.println(sum);
    }

}