public class FigurasGeometricas {
    private double valor1;
    private double valor2;

    public FigurasGeometricas(double valor1, double valor2) {
        this.valor1 = valor1;
        this.valor2 = valor2;
    }

    public double areaCirculo() { 
        return Math.PI * Math.pow(valor1, 2);
    }

    public double areaRectangulo() { 
        return valor1 * valor2;
    }

    public double areaTriangulo() { 
        return (valor1 * valor2) / 2;
    }

    public double areaTrapecio(double base2) { 
        return ((valor1 + base2) / 2) * valor2;
    }

    public double areaPentagono() { 
        double perimetro = 5 * valor1;
        double apotema = valor2; 
        return (perimetro * apotema) / 2;
    }

    public static void main(String[] args) {
        FigurasGeometricas circulo = new FigurasGeometricas(7, 0);
        System.out.println("Área del círculo: " + circulo.areaCirculo());

        FigurasGeometricas rectangulo = new FigurasGeometricas(10, 5);
        System.out.println("Área del rectángulo: " + rectangulo.areaRectangulo());

        FigurasGeometricas triangulo = new FigurasGeometricas(10, 5);
        System.out.println("Área del triángulo: " + triangulo.areaTriangulo());

        FigurasGeometricas trapecio = new FigurasGeometricas(8, 5);
        System.out.println("Área del trapecio: " + trapecio.areaTrapecio(6));

        FigurasGeometricas pentagono = new FigurasGeometricas(5, 4);
        System.out.println("Área del pentágono: " + pentagono.areaPentagono());
    }
}