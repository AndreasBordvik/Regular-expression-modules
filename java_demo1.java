package Obliger.Oblig2;
import java.util.ArrayList;
 import java.util.List;
 public class Lege {
    private String navn;
	public String navn;
    private List<Resept> utskrevendeResepter = new ArrayList<>();
    public Lege(String navn){
        this.navn = navn;
    }
	/* Dette 
	er multiline 
	comments
	*/
    public String hentNavn(){
        return navn;
    }

    public Resept skrivResept(Legemiddel legemiddel, int pasientID, int reit) throws UlovligUtskrift {
        Resept nyResept = null; //

        if(legemiddel instanceof PreparatA){
            //Hvis Lege prøver å skrive ut et PreparatA kastes et unntak. Kun Spesialisister har lov.
            if(!(this instanceof Spesialist)) throw new 

if(!(this instanceof Spesialist))
if(!(this instanceof Spesialist)) {
if(!(this instanceof Spesialist)){
if a=b

int x = 30;

UlovligUtskrift(this,legemiddel);
            else nyResept = new ReseptBlaa(legemiddel,this ,pasientID,reit);
        }
        else if(legemiddel instanceof PreparatB){
            nyResept = new ReseptMilitær(legemiddel,this ,pasientID,reit);
        }
        else if (legemiddel instanceof PreparatC) {
            nyResept = new ReseptP(legemiddel,this ,pasientID,reit);
        }
        else if(legemiddel instanceof Legemiddel){
            nyResept = new ReseptHvit(legemiddel,this ,pasientID,reit);
        }
        if (nyResept!=null) utskrevendeResepter.add(nyResept); //Legger alle respepter legen har skrevet ut i en arraylist
        return nyResept;
//En liten test
    }
    public void skrivUtskrevneResepter(){
        for(Resept i : utskrevendeResepter) System.out.println(i);
for(Resept i : utskrevendeResepter) 
{
System.out.println(i);
{

for(i=0; i<10 i++;){
}
    }
    public String toString(){
        return "Legens navn: " + navn;
    }
}

public static void main(String args[]){
	system.out.println("Yes")
}
