Root3NumTest.class: Root3Num.class Root3NumTest.java
	javac Root3NumTest.java

Root3Num.class: Root3Num.java
	javac Root3Num.java

TestRoot3Num.class: TestRoot3Num.java RandMore.class Root3Num.class
	javac TestRoot3Num.java

RandMore.class: RandMore.java
	javac RandMore.java

test: Root3NumTest.class
	java org.junit.runner.JUnitCore Root3NumTest

matr: TestRoot3Num.class
	java TestRoot3Num

.PHONY : test matr
