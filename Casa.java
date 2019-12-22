class Casa extends Edificacion{
    
    Casa(int consumo){
        super(consumo);
    }
    void setconsumo(int consumo){
        this.consumo = consumo; 
    }
    int getconsumo(){
        return consumo;
    }
}