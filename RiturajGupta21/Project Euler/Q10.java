/*The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.*/
public class Q10 {
	public static boolean checkprime(int n) {
		for(int i=3;i<=Math.sqrt(n);i+=2) {
			if(n%i==0)
				return false;
		}
		return true;
	}
	 public static void main(String args[]) {
		 long s=2;
	        for (int i=3;i<2000000;i+=2) {
	            if (checkprime(i)) {
	                s+=i;
	                }
	         }
		 System.out.println(s);
	 }
}
//Output142913828922
