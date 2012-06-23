package date;

/**
 * Provides an IllegalDateException object.
 */
public class IllegalDateException extends Exception {
    /**
     * Message explaining details of the Exception.
     */
    public String message;

    /**
     * Year of the probably wrong date.
     */
    public int year;

    /**
     * Month of the probably wrong date.
     */
    public int month;

    /**
     * Day of the probably wrong date.
     */
    public int day;

    /**
     * Constructs a new <code>IllegalDateException</code> object.
     *
     * @param message a String explaining details of the exception
     * @param year    the year of the probably wrong date
     * @param month   the month of the probably wrong date
     * @param day     the day of the probably wrong date
     */
    public IllegalDateException(String message,
                                int year, int month, int day) {
        super(
            message
            + "\nGiven year:  " + year
            + "\nGiven month: " + month
            + "\nGiven day:   " + day
        );

        this.message = message;
        this.year    = year;
        this.month   = month;
        this.day     = day;
    }
}
