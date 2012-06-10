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
     * Add Root3Num object to this.
     *
     * @param that  a Root3Num to add to this
     * @return a new Root3Num being the sum of this and that
     */
    public Root3Num add(Root3Num that) {
        return new Root3Num(this.a + that.a, this.b + that.b);
    }


    /**
     * Multiply this Root3Num by an integer.
     *
     * @param factor   an int this Root3Num is multiplied by
     * @return  a new Root3Num
     */
    public Root3Num times(int factor) {
        return new Root3Num(factor * this.a, factor * this.b);
    }


    /**
     * Subtract a Root3Num from this.
     *
     * @param that   a Root3Num to subtract from this
     * @return a new Root3Num being the difference between this and that
     */
    public Root3Num sub(Root3Num that) {
        return new Root3Num(this.a - that.a, this.b - that.b);
            // Could be done with this + (-1)*that, but I reckon that's slower
    }


    /**
     * Multiply a Root3Num with this.
     *
     * @param that   a Root3Num to be multiplied with this
     * @return  a new Root3Num being the product of this and that
     */
    public Root3Num mult(Root3Num that) {
        return new Root3Num(
                       this.a * that.a + 3 * this.b * that.b,
                       this.a * that.b +     this.b * that.a
                   );
    }


    /**
     * Return the number's real value as double.
     *
     * @return  a double holding the number's calculated value
     */
    public double value() {
        return this.a + this.b * Math.sqrt(3);
    }


    /**
     * Test whether an object is a Root3Num and equal to this.   Two Root3Nums
     * are equal iff their coefficients are equal.
     *
     * @param o   Object to be tested
     * @return    true if other object is equal to this, false otherwise
     */
    public boolean equals(Object o) {
        // Test whether the other is a valid Root3Num
        if ( o == null || !o.getClass().equals(this.getClass()) ) {
            return false;
        }

        // Compare the two Root3Nums' coefficient
        Root3Num that = (Root3Num) o;
        return this.a == that.a && this.b == that.b;
    }


    /**
     * Override the generic <code>hashCode</code> method.   The hash code for
     * the two ints representing the Root3Num is calculated according to the
     * guidelines in @see.
     *
     * @return  an int being the hash code for this Root3Num
     * @see <a href="http://www.javamex.com/tutorials/collections/hash_function_guidelines.shtml">http://www.javamex.com/tutorials/collections/hash_function_guidelines.shtml</a>
     */
    public int hashCode() {
        return (this.a * 33) ^ this.b;
    }

    /**
     * Override the generic toString method.
     *
     * @return a stringified tuple representing this Root3Num
     */
    public String toString() {
        return "(" + this.a + ", " + this.b + ")";
    }
}
