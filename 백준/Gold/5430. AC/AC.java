import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            String method = br.readLine();  // "RDD"처럼 단일 문자열로 입력됨
            int n = Integer.parseInt(br.readLine());
            String numList1 = br.readLine();

            // 빈 배열이 입력되는 경우에 대한 처리
            if (n == 0) {
                numList1 = "";
            } else {
                numList1 = numList1.substring(1, numList1.length() - 1);  // 양 끝의 대괄호 제거
            }
            String[] numArray = numList1.split(",");

            Deque<Integer> deque = new LinkedList<>();
            for (String num : numArray) {
                if (!num.isEmpty()) {
                    deque.add(Integer.parseInt(num.trim()));
                }
            }

            boolean isLeft = true;
            boolean error = false;

            for (char cmd : method.toCharArray()) {
                if (cmd == 'R') {
                    isLeft = !isLeft;
                } else if (cmd == 'D') {
                    if (deque.isEmpty()) {
                        System.out.println("error");
                        error = true;
                        break;
                    } else {
                        if (isLeft) {
                            deque.pollFirst();  // 왼쪽에서 제거
                        } else {
                            deque.pollLast();  // 오른쪽에서 제거
                        }
                    }
                }
            }

            if (!error) {
                StringBuilder sb = new StringBuilder();
                sb.append("[");

                while (!deque.isEmpty()) {
                    sb.append(isLeft ? deque.pollFirst() : deque.pollLast());
                    if (!deque.isEmpty()) {
                        sb.append(",");
                    }
                }

                sb.append("]");
                System.out.println(sb);
            }
        }
    }
}
