/**
 * Rather silly class for "testing" the rather silly Root3Num class.
 * Wie Sie vielleicht sehen, wird das Produkt der beiden Matrizen auf
 * verschiedene Arten ausgerechnet, sodass auch hier ein Vergleich angestellt
 * werden kann und damit die roundingError-Methode bereits erfüllt ist.
 */
public class TestRoot3Num {
    public static void main(String[] args) {
        // Dimensions of the matrices
        final int m = 5;
        final int n = 4;
        final int p = 7;

        // Matrices for random Root3Nums
        Root3Num[][] fak1 = new Root3Num[m][p];
        Root3Num[][] fak2 = new Root3Num[p][n];

        // Matrices for results
        Root3Num[][] prod_sym   = new Root3Num[m][n]; // symbolic
        double[][] prod_rounded = new double[m][n];   // rounded during calcs
        double[][] prod_exact   = new double[m][n];   // rounded after calcs

        // Random number generator
        RandMore random = new RandMore();

        // Populate matrices
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < p; ++j) {
                fak1[i][j] = new Root3Num(
                                     random.randrange(-99, 100),
                                     random.randrange(-99, 100)
                                 );
            }
        }

        for (int i = 0; i < p; ++i) {
            for (int j = 0; j < n; ++j) {
                fak2[i][j] = new Root3Num(
                                     random.randrange(-9, 10),
                                     random.randrange(-9, 10)
                                 );
            }
        }


        // Die verschiedenen Arten Möglichkeiten, zu multiplizieren (sehr
        // hässlich)
        for (int i = 0; i < m; ++i) {
            for (int k = 0; k < n; ++k) {
                prod_rounded[i][k] = 0.0;
                prod_sym[i][k]     = new Root3Num(0, 0);

                for (int j = 0; j < p; ++j) {
                    prod_rounded[i][k]
                        += fak1[i][j].value() * fak2[j][k].value();
                    prod_sym[i][k] = Root3Num.add(
                                         prod_sym[i][k],
                                         Root3Num.mult(
                                             fak1[i][j],
                                             fak2[j][k]
                                         )
                                     );
                }

                prod_exact[i][k] = prod_sym[i][k].value();
            }
        }

        // alles ausgeben
        print_matr(fak1);
        System.out.println("*");
        print_matr(fak2);
        System.out.println("=");
        System.out.println("symbolisch:");
        print_matr(prod_sym);
        System.out.println("\nnach dem Rechnen gerundet:");
        print_matr_d(prod_exact);
        System.out.println("\nwährend des Rechnens gerundet:");
        print_matr_d(prod_rounded);
    }


    // gibt Matrix als Text aus
    public static void print_matr(Object[][] matrix) {
        for (int i = 0; i < matrix.length; ++i) {
            for (int j = 0; j < matrix[i].length; ++j) {
                System.out.print(matrix[i][j] + "  ");
            }
            System.out.println();
        }
    }

    // Das Ganze für double. -- Warum eigentlich nicht mit der anderen?
    public static void print_matr_d(double[][] matrix) {
        for (int i = 0; i < matrix.length; ++i) {
            for (int j = 0; j < matrix[i].length; ++j) {
                System.out.print(matrix[i][j] + "  ");
            }
            System.out.println();
        }
    }
}
