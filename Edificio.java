class Edificio extends Edificacion {
    
    Edificio(int consumo){
        super(consumo);
    }
    void setconsumo(int consumo){
        this.consumo = consumo; 
    }
    int getconsumo(){
        return consumo;
    }    
}