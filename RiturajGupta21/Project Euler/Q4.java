/*A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.*/
public class Q4{
	public static int pali(){
		int pro=0;
		for (int i=999;i>900;i--) {
			for (int j=i;j>900;j--) {
				pro=i*j;
				if(check(pro)) {
					return pro;
				}
			}
		}
		return -1;
	}
		public static int rev(int pro) {
			int r=0;
			int d;
			while(pro>0) {
				d=pro%10;
				r=r*10+d;
				pro/=10;
			}
			return r;
		}
		public static boolean check(int pro) {
			if(rev(pro)==pro) {
				return true;
			}
			return false;
		}
	
	public static void main(String[] args){
		System.out.println(pali());
	}
}
//Output906609
