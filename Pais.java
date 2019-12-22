import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.IOException;

class Pais implements Grafo{
    // int [][] matrizAdj: Matriz de adyacencia, forma que elejimos para representar el grafo.
    int matrizAdj[][];
    // List<Ciudad> ciudades: Lista para almacenar las ciudades
    List<Ciudad> ciudades;
    int nNodes;
    int nEdges;
    Pais(int nNodes, int nEdges, List<Ciudad> ciudades){
        this.ciudades = ciudades;
        this.matrizAdj = new int [nNodes][nNodes];
        this.nNodes = nNodes;
        this.nEdges = nEdges;
    }
    public void setciudades (List<Ciudad> ciudades){
        this.ciudades = ciudades;
    }
    public void setmatrizAdj(int nNodes){
        this.matrizAdj = new int [nNodes][nNodes];
    }
    public void setnEdges(int nEdges) {
        this.nEdges = nEdges;
    }
    public void setnNodes(int nNodes) {
        this.nNodes = nNodes;
    }
    public List<Ciudad> getciudades(){
        return ciudades;
    }
    public int[][] getmatrizAdj() {
        return matrizAdj;
    }
    public int getnEdges() {
        return nEdges;
    }
    public int getnNodes() {
        return nNodes;
    }
    public int edgeWeigth(int n1, int n2){
        return matrizAdj[n1][n2];
    }
    public List<Integer> shortestPath(int n1, int n2){
        ShortestPath stp = new ShortestPath(nNodes);
        
        return stp.caminoDijkstra(matrizAdj, n1, n2);
    }
    public void addEdge(int n1, int n2, int peso){
        matrizAdj[n1][n2] = peso;
        matrizAdj[n2][n1] = peso;
    }
    public void addNode(int id){
        ciudades.add(new Ciudad(id));
    }

    public static void main(String[] args) {
        Empresa Lipigas;
        int cont = 0, contCasas = 0, contEdificios = 0;
        Pais Chile;
        Scanner lineaM, lineaE, lineaEd;
        List<List<Edificio>> edificios = new ArrayList<List<Edificio>>();
        List<List<Casa>> casas = new ArrayList<List<Casa>>();
        List<Ciudad> ciudades = new ArrayList<Ciudad>();
        File mapa, edificaciones, empresa;
        try{
            edificaciones = new File("edificaciones.txt");
            empresa = new File("empresa.txt");
            mapa = new File("mapa.txt");
            lineaM = new Scanner(mapa);
            lineaE = new Scanner(empresa);
            lineaEd = new Scanner(edificaciones);
            int precioBalon = lineaE.nextInt();
            int precioLitro = lineaE.nextInt();
            int costoTransporte = lineaE.nextInt();
            Lipigas = new Empresa(precioBalon,precioLitro,costoTransporte);
            int nCiudades = lineaM.nextInt();
            int nCaminos = lineaM.nextInt();
            Chile = new Pais(nCiudades, nCaminos, ciudades);
            while (lineaEd.hasNext()){
                int id = lineaEd.nextInt();
                int nCasas = lineaEd.nextInt();
                int nEdificios = lineaEd.nextInt();
                Chile.addNode(id);
                Chile.getciudades().get(cont).setnCasa(nCasas);
                Chile.getciudades().get(cont).setnEdificios(nEdificios);
                contCasas = 0;
                contEdificios = 0;
                casas.add(new ArrayList<Casa>());
                edificios.add(new ArrayList<Edificio>());
                if (nCasas == 0){
                    casas.get(cont).add(new Casa(0));
                }
                if (nEdificios == 0){
                    edificios.get(cont).add(new Edificio(0));
                }
                while (contCasas < nCasas){
                    casas.get(cont).add(new Casa(lineaEd.nextInt()));
                    contCasas++;
                }
                while (contEdificios < nEdificios){
                    edificios.get(cont).add(new Edificio(lineaEd.nextInt()));
                    contEdificios++;
                }
                cont++;
            }
            Chile.setmatrizAdj(nCiudades);
            for(cont = 0; cont < nCaminos; cont++){
                int nodo1 = lineaM.nextInt();
                int nodo2 = lineaM.nextInt();
                int peso = lineaM.nextInt();
                Chile.addEdge(nodo1, nodo2, peso);
            }
            List<List<Integer>> nVehiculos = new ArrayList<List<Integer>>();
            int x, j;
            int max = Integer.MIN_VALUE;
            int ciudad_optima = -1;
            ShortestPath stp = new ShortestPath(Chile.getnNodes());
            int[] utilidades_por_ciudad = new int[Chile.getnNodes()];
            for (cont = 0; cont < Chile.getnNodes(); cont++){
                int costo = 0;
                int venta = 0;
                int[] distancias = stp.costDijkstra(Chile.getmatrizAdj(), cont);
                for(j = 0; j < Chile.getnNodes(); j++){
                    nVehiculos.add(new ArrayList<Integer>());
                    Ciudad actual = Chile.getciudades().get(j);
                    List<Casa> consumos_c = casas.get(j);
                    List<Edificio> consumos_e = edificios.get(j);
                    Iterator<Casa> iterador_c = consumos_c.iterator();
                    while (iterador_c.hasNext()) {
                        venta += (iterador_c.next().getconsumo()*Lipigas.getPrecioBalon());
                    }
                    Iterator<Edificio> iterador_e = consumos_e.iterator();
                    while (iterador_e.hasNext()) {
                        venta += (iterador_e.next().getconsumo())*Lipigas.getPrecioLitro();
                    }
                    nVehiculos.get(j).add(actual.getnEdificios());
                    if (actual.getnCasa() != 0){
                        nVehiculos.get(j).add(1);
                    }
                    else{
                        nVehiculos.get(j).add(0);
                    }
                    for (x = 0; x < Chile.getnNodes(); x++){
                        if (actual.nCasa != 0) {
                            costo += distancias[x]*(Lipigas.getPrecioTransporte())*(1+actual.getnEdificios());
                        }
                        else{
                            costo += distancias[x]*(Lipigas.getPrecioTransporte())*(actual.getnEdificios());
                        }
                    }
                }
                utilidades_por_ciudad[cont] = venta - costo;
                if (utilidades_por_ciudad[cont] > max){
                    ciudad_optima = cont;
                    max = utilidades_por_ciudad[cont];
                }
            }                       
            System.out.println("La ciudad"+" "+ciudad_optima+" "+"es la ubicacion optima");
            for (j = 0; j < Chile.getnNodes(); j++){
                System.out.println("ciudad"+" "+ j+":");
                System.out.println("-Utilidad"+" "+utilidades_por_ciudad[j]);
                System.out.println("-Se utilizaron "+nVehiculos.get(j).get(0)+" "+"camiones cisterna y "+nVehiculos.get(j).get(1)+" camionetas");
            }                                                                                     
        }
        catch(FileNotFoundException e){
            System.out.println("Error al abrir el arachioasd");
        }
        catch(IOException e){
            System.out.println("algo");
        }

    }
}
