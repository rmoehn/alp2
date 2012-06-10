import org.junit.*;
import static org.junit.Assert.*;

public class Root3NumTest {
    private Root3Num num_zero;
    private Root3Num num_one;
    private Root3Num num1;
    private Root3Num num2;

    private double delta = 0.000_000_1;

    // Create objects to run the tests on
    @Before public void setUp() {
        num_zero = new Root3Num(0, 0);
        num_one  = new Root3Num(1, 1);
        num1 = new Root3Num(21, 4);
        num2 = new Root3Num(-12, 7);
    }

    // Test method value()
    @Test public void test_value() {
        assertEquals(num1.value(), 27.92820323, delta);
        assertEquals(num2.value(), 0.124355653, delta);
    }

    // Test method times()
    @Test public void test_times() {
        assertEquals(new Root3Num(84, 16), num1.times(4));
        assertEquals(new Root3Num(12, -7), num2.times(-1));
        assertEquals(num_zero,             num2.times(0));
        assertEquals(num1,                 num1.times(1));
    }

    // Test instance method add()
    @Test public void test_inst_add() {
        assertEquals(new Root3Num(9, 11), num1.add(num2));
        assertEquals(new Root3Num(9, 11), num2.add(num1));
        assertEquals(num1, num1.add(num_zero));
    }

    // Test instance method sub()
    @Test public void test_inst_sub() {
        assertEquals(new Root3Num(33, -3), num1.sub(num2));
        assertEquals(new Root3Num(-33, 3), num2.sub(num1));
        assertEquals(num2, num2.sub(num_zero));
    }

    // Test instance method mult()
    @Test public void test_inst_mult() {
        assertEquals(new Root3Num(-168, 99), num1.mult(num2));
        assertEquals(new Root3Num(-168, 99), num2.mult(num1));
        assertEquals(new Root3Num(9, -5), num2.mult(num_one));
            // (1, 1) not the neutral element here
        assertEquals( num2, num2.mult( new Root3Num(1, 0) ) );
        assertEquals(num_zero, num1.mult(num_zero));
    }

    // Test equals() method
    @Test public void test_equals() {
        assertEquals(num1, num1);
        assertEquals(num1, new Root3Num(21, 4));
        assertEquals(new Root3Num(21, 4), num1);

        assertTrue(!num1.equals(num2));
        assertTrue(!num1.equals(null));
        assertTrue(!num1.equals(new Object()));
    }

    // Test gt() method
    @Test public void test_gt() {
        assertTrue(  num1.gt(num2)     );
        assertTrue( !num2.gt(num1)     );
        assertTrue(  num2.gt(num_zero) );
        assertTrue( !num2.gt(num2)     );
    }

    // Test lt() method
    @Test public void test_lt() {
        assertTrue(  num2.lt(num1)     );
        assertTrue( !num1.lt(num2)     );
        assertTrue(  num2.times(-1).lt(num_zero) );
        assertTrue( !num2.lt(num2)     );
    }

    // Test hashCode() method
    @Test public void test_hashcode() {
        assertEquals(num1.hashCode(), num1.hashCode());
        assertEquals(num1.hashCode(), new Root3Num(21, 4).hashCode());
    }
}
