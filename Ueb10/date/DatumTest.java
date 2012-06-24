package date;

import org.junit.*;
import static org.junit.Assert.*;

/**
 * Class for testing the class <code>Datum</code>.
 */
public class DatumTest {
    Datum dat1;

    @Before public void setUp() throws IllegalDateException {
        dat1 = new Datum(1968, 7, 10);
    }

    // Tests for the days_in_month() class method
    @Test(expected=IllegalDateException.class)
    public void test_days_in_month_exc_1() throws IllegalDateException {
        Datum.days_in_month(0, 2700);
    }

    @Test(expected=IllegalDateException.class)
    public void test_days_in_month_exc_2() throws IllegalDateException {
        Datum.days_in_month(-60, 3);
    }

    @Test(expected=IllegalDateException.class)
    public void test_days_in_month_exc_3() throws IllegalDateException {
        Datum.days_in_month(13, 999);
    }

    @Test public void test_days_in_month() throws IllegalDateException {
        assertEquals(Datum.days_in_month(4, 1930), 30);
        assertEquals(Datum.days_in_month(10, 1517), 31);
        assertEquals(Datum.days_in_month(2, 1620), 29);
        assertEquals(Datum.days_in_month(2, 1200), 29);
        assertEquals(Datum.days_in_month(2, 1700), 28);
        assertEquals(Datum.days_in_month(2, 1749), 28);
        assertEquals(Datum.days_in_month(2, 0), 29);
        assertEquals(Datum.days_in_month(2, -32), 29);
        assertEquals(Datum.days_in_month(2, -100), 28);
    }

    // Tests for exceptions on constructing invalid Datum's
    @Test(expected=IllegalDateException.class)
    public void test_new_datum_exc_1() throws IllegalDateException {
        Datum bla = new Datum(1777, 0, 23);
    }

    @Test(expected=IllegalDateException.class)
    public void test_new_datum_exc_2() throws IllegalDateException {
        Datum bla = new Datum(9, 15, 12);
    }

    @Test(expected=IllegalDateException.class)
    public void test_new_datum_exc_3() throws IllegalDateException {
        Datum bla = new Datum(1096, 6, 31);
    }

    @Test(expected=IllegalDateException.class)
    public void test_new_datum_exc_4() throws IllegalDateException {
        Datum bla = new Datum(769, 2, 29);
    }

    @Test(expected=IllegalDateException.class)
    public void test_new_datum_exc_5() throws IllegalDateException {
        Datum bla = new Datum(23_500, 10, -4);
    }

    @Test(expected=IllegalDateException.class)
    public void test_new_datum_exc_6() throws IllegalDateException {
        Datum bla = new Datum(1958, 5, 35);
    }

    // Test method setDate()
    @Test public void test_setDate() throws IllegalDateException {
        Datum datum = new Datum(1712, 6, 28);
        datum.setDate(30, 5, 1832);
        assertEquals(datum, new Datum(1832, 5, 30));
    }

    @Test(expected=IllegalDateException.class)
    public void test_setDate_exc() throws IllegalDateException {
        Datum datum = new Datum(1712, 6, 28);
        datum.setDate(31, 4, 1640);
    }

    // Test method setDatum()
    @Test public void test_setDatum() throws IllegalDateException {
        Datum datum = new Datum(1712, 6, 28);
        datum.setDatum(1848, 3, 30);
        assertEquals(datum, new Datum(1848, 3, 30));
    }

    @Test(expected=IllegalDateException.class)
    public void test_setDatum_exc() throws IllegalDateException {
        Datum datum = new Datum(1712, 6, 28);
        datum.setDatum(31, 9, 1688);
    }

    // Test method getYear()
    @Test public void test_getYear() {
        assertEquals(dat1.getYear(), 1968);
    }

    // Test method getDay()
    @Test public void test_getDay() {
        assertEquals(dat1.getDay(), 10);
    }

    // Test method getMonth()
    @Test public void test_getMonth() {
        assertEquals(dat1.getMonth(), 7);
    }

    // Test method getDate()
    @Test public void test_getDate() throws IllegalDateException {
        Datum cloned_dat1 = dat1.getDate();
        assertTrue(cloned_dat1 != dat1);
        assertEquals(cloned_dat1, dat1);
    }

    // Tests for method nextDay()
    @Test public void test_nextDay() throws IllegalDateException {
        Datum datum;

        // Dieses beschissene Interface ist absolut testfeindlich!

        // Tageswechsel
        datum = new Datum(1912, 6, 22);
        datum.nextDay();
        assertEquals(datum, new Datum(1912, 6, 23));
        datum = new Datum(-44, 3, 14);
        datum.nextDay();
        assertEquals(datum, new Datum(-44, 3, 15));

        // Monatswechsel
        datum = new Datum(1992, 5, 30);
        datum.nextDay();
        assertEquals(datum, new Datum(1992, 5, 31));
        datum = new Datum(1992, 5, 31);
        datum.nextDay();
        assertEquals(datum, new Datum(1992, 6, 1));
        datum = new Datum(1872, 4, 30);
        datum.nextDay();
        assertEquals(datum, new Datum(1872, 5, 1));
        datum = new Datum(1834, 8, 30);
        datum.nextDay();
        assertEquals(datum, new Datum(1834, 8, 31));

        // Jahreswechsel
        datum = new Datum(2001, 12, 31);
        datum.nextDay();
        assertEquals(datum, new Datum(2002, 1, 1));
        datum = new Datum(-1, 12, 31);
        datum.nextDay();
        assertEquals(datum, new Datum(0, 1, 1));
        datum = new Datum(-754, 12, 31);
        datum.nextDay();
        assertEquals(datum, new Datum(-753, 1, 1));

        // Schaltjahr oder nicht Schaltjahr
        datum = new Datum(1900, 2, 28);
        datum.nextDay();
        assertEquals(datum, new Datum(1900, 3, 1));
        datum = new Datum(2000, 2, 28);
        datum.nextDay();
        assertEquals(datum, new Datum(2000, 2, 29));
        datum = new Datum(2012, 2, 28);
        datum.nextDay();
        assertEquals(datum, new Datum(2012, 2, 29));
        datum = new Datum(2012, 2, 29);
        datum.nextDay();
        assertEquals(datum, new Datum(2012, 3, 1));
    }

    // Test method toString()
    @Test public void test_toString() throws IllegalDateException {
        assertEquals(new Datum(1821, 5, 3).toString(), "1821-05-03");
        assertEquals(new Datum(-9, 1, 23).toString(), "-9-01-23");
    }

    // Test method compareTo()
    @Test public void test_compareTo() throws IllegalDateException {
        assertEquals(new Datum(1962, 6, 6).compareTo(
                     new Datum(2010, 6, 3)), -1);
        assertEquals(new Datum(1926, 5, 27).compareTo(
                     new Datum(1926, 5, 27)), 0);
        assertEquals(new Datum(1819, 1, 1).compareTo(
                     new Datum(1818, 12, 27)), 1);
    }

    // Test method before()
    @Test public void test_before() throws IllegalDateException {
        assertTrue(new Datum(1986, 11, 13).before(new Datum(1989, 8, 3)));
        assertTrue(! new Datum(1912, 3, 29).before(new Datum(1912, 3, 28)));
        assertTrue(! dat1.before(dat1));
    }

    // Test method after()
    @Test public void test_after() throws IllegalDateException {
        assertTrue(new Datum(1932, 6, 1).after(new Datum(1930, 3, 29)));
        assertTrue(! new Datum(1709, 3, 10).after(new Datum(1709, 3, 11)));
        assertTrue(! dat1.after(dat1));
    }

    // Test equals() method
    @Test public void test_equals() throws IllegalDateException {
        assertEquals(dat1, dat1);
        assertEquals(dat1, new Datum(1968, 7, 10));
        assertEquals(new Datum(1968, 7, 10), dat1);

        assertTrue(!dat1.equals(new Datum(1967, 1, 29)));
        assertTrue(!dat1.equals(null));
        assertTrue(!dat1.equals(new Object()));
    }

    // Test hashCode() method
    @Test public void test_hashcode() throws IllegalDateException {
        assertEquals(dat1.hashCode(), dat1.hashCode());
        assertEquals(dat1.hashCode(), new Datum(1968, 7, 10).hashCode());
    }
}
