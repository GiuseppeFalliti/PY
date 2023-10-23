
public class Poligono {
    private float[] poligono;
    
    public Poligono(){
        poligono=new float[50];
    }

    public void add(int index,float p){
        poligono[index]=p;
    }
    public void print(){
        System.out.println("elenco punti");
        for (int i = 0; i < poligono.length; i++) {
            System.out.println(poligono[i]);
            
        }

     
    }
    public void togli(int i){
        if((i>=0) && (i<poligono.length)){
            poligono[i]=0;
        }

    }   
}