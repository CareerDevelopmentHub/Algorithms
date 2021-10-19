/*The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?*/
public class Q3 {
	public static void main(String args[]) {
		long n;
		long a=600851475143l;
		long q=a;
		long b=0;
		for(n=3;n<=Math.sqrt(q);n+=2){
			while(a%n==0) {
				b=n;
				a=a/n;
				break;
			}
		}
		System.out.println(b);
	}
}
//Output6857
