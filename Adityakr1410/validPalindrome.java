/*
Q. A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
	Input: s = "A man, a plan, a canal: Panama"
	Output: true
	Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
	Input: s = "race a car"
	Output: false
	Explanation: "raceacar" is not a palindrome.

Example 3:
	Input: s = " "
	Output: true
	Explanation: s is an empty string "" after removing non-alphanumeric characters.
	Since an empty string reads the same forward and backward, it is a palindrome.
*/


public class validPalindrome 
{
    public static boolean isPalindrome(String s) 
    {
        if (s.isEmpty())
        	return true;
        int head = 0, tail = s.length() - 1;
        char cHead, cTail;
        while(head <= tail) 
        {
        	cHead = s.charAt(head);
        	cTail = s.charAt(tail);
        	if (!Character.isLetterOrDigit(cHead))
        		head++;
        	else if(!Character.isLetterOrDigit(cTail))
        		tail--;
        	else 
        	{
        		if (Character.toLowerCase(cHead) != Character.toLowerCase(cTail))
        			return false;
        		head++;
        		tail--;
        	}
        }
        return true;
    }
    public static void main(String []args)
    {
    	String str = "A man, a plan, a canal: Panama"; // take different inputs
    	System.out.println(isPalindrome(str)?"Palindrome":"Not Palindrome");
    }
}
