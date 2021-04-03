public class dataType {
    public static void main(String[] args) {
        Integer a=1;
        Float b=2f;
        Double d=3.0;
        Character c='s';
        String S="kumar";
        Boolean bl= true;
        
        System.out.println( a.getClass().getSimpleName()+" "+b.getClass().getSimpleName()+
                            " "+d.getClass().getSimpleName()+" "+c.getClass().getSimpleName()+" "+S.getClass().getSimpleName()+" "+
                               bl.getClass().getSimpleName());

    }
}
