import org.junit.*;
import static org.junit.Assert.*;

public class Root3NumTest {
    private Root3Num num1;
    private Root3Num num2;
    private double delta = 0.000_000_1;

    // Create objects to run the tests on
    @Before public void setUp() {
        num1 = new Root3Num(21, 4);
        num2 = new Root3Num(-12, 7);
    }

    // Test method value()
    @Test public void test_value() {
        assertEquals(num1.value(), 27.92820323, delta);
        assertEquals(num2.value(), 0.124355653, delta);
    }
}
