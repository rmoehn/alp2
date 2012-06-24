package date;

import java.util.Formatter;

/**
 * Provides an object for simple date operations.
 */
public class Datum {
    private int year;
    private int month;
    private int day;

    /**
     * Constructs a new <code>Datum</code> object.   Year, month and day have
     * to be given in ISO order.
     *
     * @param year  the year of the date (negative numbers for years BCE)
     * @param month the month of the date
     * @param day   the day of the date
     *
     * @throws IllegalDateException If an invalid date was given
     */
    public Datum(int year, int month, int day) throws IllegalDateException {
        this.setDatum(year, month, day);
    }

    /**
     * Sets the parameters of a <code>Datum</code> object.   Year, month and
     * day have to be given in ISO order.
     *
     * @param year  the year of the date (negative numbers for years BCE)
     * @param month the month of the date
     * @param day   the day of the date
     *
     * @throws IllegalDateException If an invalid date was given
     */
    public void setDatum(int year, int month, int day)
           throws IllegalDateException {
        // Die on weird month
        if (month < 1 || month > 12) {
            throw new IllegalDateException(
                          "Invalid month number.",
                          year, month, day
                      );
        }

        // Die on weird day
        if (day < 1 || day > days_in_month(month, year)) {
            throw new IllegalDateException(
                          "Invalid day of month.",
                          year, month, day
                      );
        }

        // Set this Datum's fields
        this.year  = year;
        this.month = month;
        this.day   = day;
    }

    /**
     * Sets the parameters of a <code>Datum</code> object.   Year, month and
     * day have to be given in day-month-year-order.
     *
     * @param day   the day of the date
     * @param month the month of the date
     * @param year  the year of the date (negative numbers for years BCE)
     *
     * @throws IllegalDateException If an invalid date was given
     */
    public void setDate(int day, int month, int year)
           throws IllegalDateException {
        this.setDatum(year, month, day);
    }

    /**
     * Changes this <code>Datum</code> to the day after it.
     */
    public void nextDay() throws IllegalDateException {
        // Current day is last day of month...
        if (this.day == days_in_month(this.month, this.year)) {
            // ...and last day of year: Set to start of following year.
            if (this.month == 12) {
                ++this.year;
                this.month = 1;
                this.day   = 1;
            }
            // ...and midst in the year: Set to start of following month.
            else {
                ++this.month;
                this.day = 1;
            }
        }
        // Current day is ordinary day: Set to following day.
        else {
            ++this.day;
        }
    }

    /**
     * Determine the number of days in a month in a certain year.
     *
     * @param month  the number of the month
     * @param year   the year (negative numbers for years BCE)
     *
     * @return the number of days in the month month in the year year
     *
     * @throws IllegalDateException If the number of the month is silly
     */
    public static int days_in_month(int month, int year)
           throws IllegalDateException {
        switch (month) {
            case  1: /* falls through */
            case  3: /* falls through */
            case  5: /* falls through */
            case  7: /* falls through */
            case  8: /* falls through */
            case 10: /* falls through */
            case 12:
                return 31; // Make sure to insert breaks upon removing return.
            case  4: /* falls through */
            case  6: /* falls through */
            case  9: /* falls through */
            case 11: /* falls through */
                return 30;
            case  2:
                if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
                    // Leap year
                    return 29;
                }
                else {
                    return 28;
                }
            default:
                throw new IllegalDateException(
                              "Invalid month number.",
                              year, month, 0
                          );
        }
    }

    /**
     * Returns the year of this <code>Datum</code>.
     *
     * @return the year of this Datum
     */
    public int getYear() {
        return this.year;
    }

    /**
     * Returns the month of this <code>Datum</code>.
     *
     * @return the month of this Datum
     */
    public int getMonth() {
        return this.month;
    }

    /**
     * Returns the day of this <code>Datum</code>.
     *
     * @return the day of this Datum
     */
    public int getDay() {
        return this.day;
    }

    /**
     * Returns a copy of this <code>Datum</code>.
     *
     * @return a Datum being the copy of this
     */
    public Datum getDate() throws IllegalDateException {
        return new Datum(this.year, this.month, this.day);
    }

    /**
     * Compares this <code>Datum</code>  with the specified <code>Datum</code>
     * for order. Returns -1, 0, or a 1 as this <code>Datum</code> is less
     * than, equal to, or greater than the specified <code>Datum</code> . This
     * is this class' implementation of the {@link Comparable} interface.
     *
     * @param that the Datum to be compared with this
     * @return -1, 0 or 1 as this Datum is less than, equal to, or greater
     *         than the specified Datum
     * @see Comparable
     */
    public int compareTo(Datum that) {
        if (this.year  < that.year) {
            return -1;
        }
        if (this.year  > that.year) {
            return  1;
        }
        if (this.month < that.month) {
            return -1;
        }
        if (this.month > that.month) {
            return  1;
        }
        if (this.day   < that.day) {
            return -1;
        }
        if (this.day   > that.day) {
            return  1;
        }

        return 0; // Equality left.
    }

    /**
     * Checks whether this <code>Datum</code> is after a given Datum.
     *
     * @param that the Datum to be checked
     * @return <code>true</code> if this Datum is after that
     *         <code>false</code> otherwise
     */
    public boolean after(Datum that) {
        return this.compareTo(that) == 1;
    }

    /**
     * Checks whether this <code>Datum</code> is before a given Datum.
     *
     * @param that the Datum to be checked
     * @return <code>true</code> if this Datum is before that
     *         <code>false</code> otherwise
     */
    public boolean before(Datum that) {
        return this.compareTo(that) == -1;
    }

    /**
     * Returns this <code>Datum</code>'s date as a String, probably in accord
     * with ISO.
     *
     * @return a String representing this Datum
     */
    public String toString() {
        return String.format("%d-%02d-%02d", this.year, this.month, this.day);
    }

    /**
     * Test whether an object is a <code>Datum</code>  and equal to this.
     * Two <code>Datum</code>s are equal iff their year, month and date are
     * equal.
     *
     * @param o   Object to be tested
     * @return    <code>true</code> if other object is equal to this,
     *            <code>false</code> otherwise
     */
    public boolean equals(Object o) {
        // Test whether the other is a Datum at all
        if ( o == null || !o.getClass().equals(this.getClass()) ) {
            return false;
        }

        // Compare the two Datums' year, month, day
        Datum that = (Datum) o;
        return this.year  == that.year
            && this.month == that.month
            && this.day   == that.day;
    }

    /**
     * Override the generic <code>hashCode</code> method.   The hash code for
     * the three ints representing the <code>Datum</code> is calculated
     * according to the guidelines in @see.
     *
     * @return  an int being the hash code for this Datum
     * @see <a href="http://www.javamex.com/tutorials/collections/hash_function_guidelines.shtml">http://www.javamex.com/tutorials/collections/hash_function_guidelines.shtml</a>
     */
    public int hashCode() {
        return (this.year * 33) ^ (this.month * 37) ^ this.day;
    }

}
