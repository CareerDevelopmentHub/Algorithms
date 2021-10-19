/*The sum of the squares of the first ten natural numbers is,
1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.*/
public class Q6{
	public static void main (String args[]){
		int a=(100*101*201)/6,b=(100*101)/2;
		System.out.print(((b*b)-a));
		}
}
//Output25164150
