package local.util;

import java.util.Random;

public class RandMore extends Random {
    /**
     * Returns an integral random number in the range a to b-1.
     */
    public int randrange(int a, int b) {
        return this.nextInt(b - a) + a;
    }

    /**
     * Returns a double random number in the range a to b.
     */
    public double dblrange(double a, double b) {
        return this.nextDouble() * (b - a) + a;
    }
}
