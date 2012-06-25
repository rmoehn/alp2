package queue;

import org.junit.*;
import static org.junit.Assert.*;

import aufg01.Root3Num;
import local.util.RandMore;

/**
 * Class for testing the class <code>SimpleQueue</code>.
 */
public class SimpleQueueTest {
    public int testnums_cnt = 500;

    public Root3Num[] testnums = new Root3Num[testnums_cnt];

    @Before public void setUp() {
        // Populate the array of Root3Nums for testing with random stuff
        RandMore random = new RandMore();
        for (int i = 0; i < testnums_cnt; ++i) {
            testnums[i] = new Root3Num(
                                  random.randrange(-99, 100),
                                  random.randrange(-99, 100)
                              );
        }
    }

    // Test basic operations -- difficult to test separately
    @Test public void test_basic() throws EmptyQueueException {
        SimpleQueue<Root3Num> queue = new SimpleQueue<Root3Num>();

        assertTrue(queue.empty());
        assertEquals("()", queue.toString());

        // Some simple stuff
        queue.enqueue(testnums[0]);

        assertEquals(queue.head(), testnums[0]);
        assertTrue(!queue.empty());
        assertEquals(queue.toString(), "(" + testnums[0] + ")");

        assertEquals(queue.dequeue(), testnums[0]);
        assertTrue(queue.empty());

        // Some random operations
        queue.enqueue(testnums[1]);
        queue.enqueue(testnums[2]);
        assertEquals(queue.head(), testnums[1]);
        queue.enqueue(testnums[3]);
        assertEquals(queue.dequeue(), testnums[1]);
        assertEquals(queue.dequeue(), testnums[2]);
        queue.enqueue(testnums[4]);
        queue.enqueue(testnums[5]);

        assertEquals(
            queue.toString(),
            "(" + testnums[3] + ", " + testnums[4] + ", "
            + testnums[5] + ")"
        );

        assertTrue(! queue.empty());

        assertEquals(queue.dequeue(), testnums[3]);
        assertEquals(queue.dequeue(), testnums[4]);

        assertEquals(queue.toString(), "(" + testnums[5] + ")");
        assertEquals(queue.dequeue(), testnums[5]);

        assertTrue(queue.empty());

        queue.enqueue(testnums[6]);
        assertEquals(queue.toString(), "(" + testnums[6] + ")");
        assertEquals(queue.dequeue(), testnums[6]);

        assertTrue(queue.empty());

        // Should also account for the extensibility of the fellow
        for (int i = 0; i < testnums_cnt; ++i) {
            queue.enqueue(testnums[i]);
            assertTrue(!queue.empty());
        }
        for (int i = 0; i < testnums_cnt; ++i) {
            assertTrue(!queue.empty());
            assertEquals(queue.dequeue(), testnums[i]);
        }

        // Same procedure but probably somewhere in the middle of the array
        // Or not?
        for (int i = 0; i < testnums_cnt; ++i) {
            queue.enqueue(testnums[i]);
            assertTrue(!queue.empty());
        }
        for (int i = 0; i < testnums_cnt; ++i) {
            assertTrue(!queue.empty());
            assertEquals(queue.dequeue(), testnums[i]);
        }
        assertTrue(queue.empty());
    }

    // Test exceptions
    @Test(expected=EmptyQueueException.class)
    public void test_exc_1() throws EmptyQueueException {
        SimpleQueue<Integer> queue = new SimpleQueue<Integer>();
        Integer bla = queue.head();
    }

    @Test(expected=EmptyQueueException.class)
    public void test_exc_2() throws EmptyQueueException {
        SimpleQueue<Integer> queue = new SimpleQueue<Integer>();
        Integer bla = queue.dequeue();
    }

    @Test(expected=EmptyQueueException.class)
    public void test_exc_3() throws EmptyQueueException {
        SimpleQueue<Integer> queue = new SimpleQueue<Integer>();
        queue.enqueue(4);
        Integer bla = queue.dequeue();
        bla = queue.dequeue();
    }
}
