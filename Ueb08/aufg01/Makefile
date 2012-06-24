Root3NumTest.class: Root3Num.class Root3NumTest.java
	javac $(CP) Root3NumTest.java

Root3Num.class: Root3Num.java
	javac $(CP) Root3Num.java

TestRoot3Num.class: TestRoot3Num.java RandMore.class Root3Num.class
	javac $(CP) TestRoot3Num.java

RandMore.class: RandMore.java
	javac $(CP) RandMore.java

test: Root3NumTest.class
	java $(CP) org.junit.runner.JUnitCore Root3NumTest

matr: TestRoot3Num.class
	java $(CP) TestRoot3Num

.PHONY : test matr
CP = -cp /usr/share/java/junit4.jar:/home/erle/ALPII:/home/erle/ALPII/Ueb08
