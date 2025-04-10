import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        int[] A = new int[N];
        int cnt=0;
        
        StringTokenizer st = new StringTokenizer(br.readLine()); 
        for(int i=0;i<N;i++){
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);
        
        for(int i=0;i<N;i++){
            int key = A[i];
            int start = 0;
            int end = N-1;
            while (start<end) {
                if(A[start]+A[end]==key){
                    if(start!=i && end!=i){
                        cnt++;
                        break;
                    }
                    else if(start==i) start++;
                    else if(end==i) end--;
                } else if(A[start]+A[end]<key) start++;
                else end--;
            }
        }
        System.out.println(cnt);
    }
}