import java.lang.Math;

/**
 * Calculation with numbers of the format (a + b*sqrt(3)).   This utterly
 * reusable class implements arithmetic operations on numbers of the format (a
 * + b*sqrt(3)). In analogy with complex numbers, all operations are done with
 * the integer coefficients a and b. Thus rounding errors and calculation
 * expenses are decreased.
 */
public class Root3Num {
    // The coefficients
    public final int a;
    public final int b;

    /**
     * Class constructor.
     *
     * @param a  the first parameter
     * @param b  the second parameter
     */
    public Root3Num(int a, int b) {
        this.a = a;
        this.b = b;
    }

    /**
     * Return the number's real value as double.
     *
     * @return  a double holding the number's calculated value
     */
    public double value() {
        return this.a + this.b * Math.sqrt(3);
    }
}
