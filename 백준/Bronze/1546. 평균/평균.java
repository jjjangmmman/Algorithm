import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc  = new Scanner(System.in);
        int N = sc.nextInt();
        int A[] = new int[N];
        for(int i =0;i<A.length;i++){
            A[i] = sc.nextInt();
        }
        int sum = 0;
        int max = 0;
        for(int i=0;i<A.length;i++){
            if(A[i]>max) max=A[i];
            sum+=A[i];
        }
        System.out.println((double)sum*100/max/N);
    }
}