
class Ciudad{
    int id;
    int nEdificios;
    int nCasa;
    public Ciudad(int id){
        this.id = id;
    }
    public Ciudad(int id, int nEdificios, int nCasa){
        this.id = id;
        this.nEdificios = nEdificios;
        this.nCasa = nCasa;
    }
    public void setid(int id) {
        this.id = id;
    }
    public void setnEdificios(int nEdificios) {
        this.nEdificios = nEdificios;
    }
    public void setnCasa(int nCasa) {
        this.nCasa = nCasa;
    }
    public int getid() {
        return id;
    }
    public int getnCasa() {
        return nCasa;
    }
    public int getnEdificios() {
        return nEdificios;
    }
}
