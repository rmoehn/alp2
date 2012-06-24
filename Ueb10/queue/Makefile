SimpleQueueTest.class: SimpleQueueTest.java SimpleQueue.java EmptyQueueException.java Queue.java
	javac $(CP) SimpleQueueTest.java SimpleQueue.java EmptyQueueException.java Queue.java

.PHONY: test
test: SimpleQueueTest.class
	java $(CP) org.junit.runner.JUnitCore queue.SimpleQueueTest

%.class: %.java
	javac $(CP) $<

CP = -cp /usr/share/java/junit4.jar:/home/erle/ALPII/Ueb10:/home/erle/ALPII:/home/erle/ALPII/Ueb08
