class Empresa{
    int PrecioBalon;
    int PrecioLitro;
    int PrecioTransporte;
    public Empresa(int precioBalon,int precioLitro,int PrecioTransporte){
        this.PrecioLitro = precioLitro;
        this.PrecioBalon = precioBalon;
        this.PrecioTransporte = PrecioTransporte;
    }
    public void setPrecioBalon(int precioBalon) {
        this.PrecioBalon = precioBalon;
    }
    public void setPrecioLitro(int precioLitro) {
        this.PrecioLitro = precioLitro;
    }
    public void setPrecioTransporte(int precioTransporte) {
        this.PrecioTransporte = precioTransporte;
    }
    public int getPrecioBalon() {
        return PrecioBalon;
    }
    public int getPrecioLitro() {
        return PrecioLitro;
    }
    public int getPrecioTransporte() {
        return PrecioTransporte;
    }
}
