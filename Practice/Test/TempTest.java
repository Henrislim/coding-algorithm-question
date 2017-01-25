
/**
 * Write a description of TempTest here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */

import java.lang.*;

public class TempTest {
    public static void Test(){
        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        System.out.println(alphabet.indexOf("F"));
        
        StringBuilder sb = new StringBuilder("Start");
        sb.insert(4,"le");
        System.out.println(sb);
    }
    
    public static void Reverse(String s){
        String ret = "";
        for (int i = 0; i<s.length(); i++){
            ret = s.charAt(i) + ret;
        }
        System.out.println(ret);
    }
    
    public static void Character(String s){
        for (int i = 0; i< s.length();i++){
            char ch = s.charAt(i);
            if (Character.isLetter(ch)){
                System.out.println(ch + "is a letter");
            }
            else if (Character.isDigit(ch)){
                System.out.println(ch + "is a digit");
            }
        }
    }
    
    public static void Caesar(String s, int key){
        StringBuilder myBuilder = new StringBuilder(s);
        String book_original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String book_new = book_original.substring(key,book_original.length())
        + book_original.substring(0,key);
        for (int i = 0;i<myBuilder.length();i++){
            char ch = myBuilder.charAt(i);
            int position = book_original.indexOf(ch);
            if (position != -1){
                myBuilder.setCharAt(i,book_new.charAt(position));
            }
        }
        System.out.println(myBuilder.toString());
        
    }
    
    
    
        
}
