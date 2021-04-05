import java.util.*;

class listsOPs{

    public static void main(String [] args){
        List<String> ls = new ArrayList<String>();
        ls.add("sai");
        ls.add("kumar");
        ls.add("sandra");
    
        System.out.println(ls);
        
        System.out.println(ls.get(2));
        System.out.println(ls.remove(2));
        System.out.println(ls);
        System.out.println(ls.size());
       String [] lsNew =ls.toArray(new String [ls.size()]);
       System.out.println(Arrays.toString(lsNew));

    }
}