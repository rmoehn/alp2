DatumTest.class: DatumTest.java Datum.class IllegalDateException.class

Datum.class: Datum.java IllegalDateException.class

Date.class: Date.java

Comparable.class: Comparable.java

IllegalDateException.class: IllegalDateException.java

.PHONY: test
test: DatumTest.class
	java $(CP) org.junit.runner.JUnitCore date.DatumTest

%.class: %.java
	javac $(CP) $<

CP = -cp /usr/share/java/junit4.jar:/home/erle/ALPII/Ueb10
