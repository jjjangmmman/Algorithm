import java.io.*;
import java.util.*;


public class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int suNo = Integer.parseInt(st.nextToken());
        int quizNo = Integer.parseInt(st.nextToken());
        
        long[] S = new long[suNo+1];
        
        st = new StringTokenizer(br.readLine());
        for(int i=1;i<=suNo;i++){
            S[i] = S[i-1] + Integer.parseInt(st.nextToken());
        }
        
        StringBuilder sb = new StringBuilder();
        for(int q=0;q<quizNo;q++){
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            sb.append(S[j] - S[i-1]).append('\n');
        }
        System.out.print(sb);
    }
}