
import java.io.*;
import java.util.*;
import java.util.Collections;
import java.util.stream.Collectors;
class GFG {
	public static void main (String[] args) {
	    String n="I love India";
		
		String[] newlist=n.split(" ");
		List<String> finalList=new ArrayList<>();
		    
		for(int j=0;j<newlist.length;j++)
		{
		    int i=0;
		    String cd=newlist[j];
		    char c=cd.charAt(0);
		    if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||
		    c=='A'||c=='E'||c=='I'||c=='O'||c=='U')
		    {
	        String added=newlist[j]+"ma";
	        while(i<j+1){
	            added+='a';
	            i++;
	        }
	        finalList.add(added);
		    }
		else{
		String check=cd.substring(1)+c+"ma";
		 while(i<j+1){
	            check+='a';
	            i++;
	        }
	       
		finalList.add(check);
		    
		}
		
		}
		
		String finalString=finalList.stream().collect(Collectors.joining(" "));
		System.out.println(finalString);
	}
}