package shapes;

/**
 * @author M. Esponda
 * @version 1.0
 */

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.util.AbstractList;
import java.util.Random;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class TestRectangle extends JFrame {
	
  /* This is a simple java class as support for the testing of your Rectangle class. 
   * The class creates a window on your screen, visualizes some 
   * Rectangle-Objects and call the methods of your Rectangle class.
   * 
   * It's really not necessary to change anything in this code.
   * 
   * You also don't need to understand all the details of the methods on this class 
   * to write your solutions.
   * 
   * Please ask your tutor in your exercise session if you want to learn 
   * more detail about this class.
   */
	
	private static final long serialVersionUID = 1L;
	
	RectanglesPanel rectanglesPanel = new RectanglesPanel();
  
	public TestRectangle(){
		setSize(400,500);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		testOverlaps();
		testContains();
		testSumOfSquares();
		testCompareOperations();
		add(rectanglesPanel);
		setVisible(true); 
	}
  
	public void testOverlaps(){
	    // overlaps: First case    
	    LabeledRectangle lr1 = new LabeledRectangle( 15, 25, 20, 20 );
	    LabeledRectangle lr2 = new LabeledRectangle( 20, 30, 30, 30 );
	    if ( lr1.r.overlaps( lr2.r ) )
	      lr1.label = "overlaps";
	    else
	    	lr1.label = "not overlaps";
	    rectanglesPanel.add( lr1 );
	    rectanglesPanel.add( lr2 );
	    
	    // overlaps: Second case    
	    LabeledRectangle lr3 = new LabeledRectangle( 105, 25, 30, 40 );
	    LabeledRectangle lr4 = new LabeledRectangle( 110, 30, 40, 20 );
	    if ( lr3.r.overlaps( lr4.r ) )
	        lr3.label = "overlaps";
	    else
	    	lr3.label = "not overlaps";
	    rectanglesPanel.add( lr3 );
	    rectanglesPanel.add( lr4 );
	    
	    // overlaps: 3th case    
	     LabeledRectangle lr5 = new LabeledRectangle( 215, 20, 20, 40 );
	     LabeledRectangle lr6 = new LabeledRectangle( 200, 30, 60, 20);	   
	    if ( lr5.r.overlaps( lr6.r ) )
	        lr5.label = "overlaps";
	    else
	    	lr5.label = "not overlaps";
	    rectanglesPanel.add( lr5 );
	    rectanglesPanel.add( lr6 );
	    
	    // overlaps: 4th case    
	    LabeledRectangle lr7 = new LabeledRectangle( 20, 120, 60, 60 );
	    LabeledRectangle lr8 = new LabeledRectangle( 30, 130, 30, 30 );
	    if ( lr7.r.overlaps( lr8.r ) )
	        lr7.label = "overlaps";
	    else
	    	lr7.label = "not overlaps";
	    rectanglesPanel.add( lr7 );
	    rectanglesPanel.add( lr8 );
	    
	    // overlaps: 5th case    
	    LabeledRectangle lr9 = new LabeledRectangle( 120, 120, 20, 30 );
	    LabeledRectangle lr10 = new LabeledRectangle( 146, 115, 30, 30 );
	    if ( lr9.r.overlaps( lr10.r ) )
	        lr9.label = "overlaps";
	    else
	    	lr9.label = "not overlaps";
	    rectanglesPanel.add( lr9 );
	    rectanglesPanel.add( lr10 );
	    
	    // overlaps: 6th case    
	    LabeledRectangle lr11 = new LabeledRectangle( 220, 120, 30, 30 );
	    LabeledRectangle lr12 = new LabeledRectangle( 200, 160, 30, 20 );
	    if ( lr11.r.overlaps( lr12.r ) )
	        lr11.label = "overlaps";
	    else
	    	lr11.label = "not overlaps";
	    rectanglesPanel.add( lr11 );
	    rectanglesPanel.add( lr12 );
	    
	    // overlaps: 7th case    
	    LabeledRectangle lr13 = new LabeledRectangle( 20, 220, 30, 30 );
	    LabeledRectangle lr14 = new LabeledRectangle( 10, 215, 30, 20 );
	    if ( lr13.r.overlaps( lr14.r ) )
	        lr13.label = "overlaps";
	    else
	    	lr13.label = "not overlaps";
	    rectanglesPanel.add( lr13 );
	    rectanglesPanel.add( lr14 );
  }
  
  public void testContains(){
	// contains: First case
    LabeledRectangle lr1 = new LabeledRectangle( 110, 220, 40, 40 );
    LabeledRectangle lr2 = new LabeledRectangle( 120, 230, 20, 20 );
    if ( lr1.r.contains( lr2.r ) )
        lr1.label = "contains :)";
    else
    	lr1.label = "not contains";
    rectanglesPanel.add( lr1 );
    rectanglesPanel.add( lr2 );
    
	// contains: Second case
    LabeledRectangle lr3 = new LabeledRectangle( 200, 225, 20, 20 );
    LabeledRectangle lr4 = new LabeledRectangle( 240, 235, 40, 40 );
    if ( lr3.r.contains( lr4.r ) )
        lr3.label = "contains :)";
    else
    	lr3.label = "not contains";
    rectanglesPanel.add( lr3 );
    rectanglesPanel.add( lr4 );
    
	// contains: 3th case
    LabeledRectangle lr5 = new LabeledRectangle( 20, 300, 40, 50 );
    LabeledRectangle lr6 = new LabeledRectangle( 40, 315, 50, 20 );
    if ( lr5.r.contains( lr6.r ) )
        lr5.label = "contains :)";
    else
    	lr5.label = "not contains";
    rectanglesPanel.add( lr5 );
    rectanglesPanel.add( lr6 );
  }
  
  public void testSumOfSquares(){
	// sumSquares: First example
	  LabeledRectangle r1 = new LabeledRectangle (120, 310, 90,40);
	  rectanglesPanel.add(r1);
	  r1.label = "Looks correct?";
	  AbstractList<Rectangle> list = r1.r.sumOfSquares();
	    int sumOfAreas = 0;
	    for (Rectangle r : list){
	    	sumOfAreas = sumOfAreas + r.area();
	    	rectanglesPanel.add(new LabeledRectangle(r.x, r.y, r.width, r.height));
	    } 
    	if (r1.r.area()==sumOfAreas)
    		r1.label = "the sum is correct";
    	else
    		r1.label = "the sum is wrong";	
    
    // sumSquares: Second example
  	  LabeledRectangle r2 = new LabeledRectangle (220, 310, 99,140);
  	  rectanglesPanel.add(r2);
  	  r2.label = "Looks correct?";
  	    AbstractList<Rectangle> rects2 = r2.r.sumOfSquares();
  	    sumOfAreas = 0;
  	    for (Rectangle r : rects2){
  	    	sumOfAreas = sumOfAreas + r.area();
  	    	rectanglesPanel.add(new LabeledRectangle(r.x, r.y, r.width, r.height));
  	    } 
      	if (r2.r.area()==sumOfAreas)
      		r2.label = "the sum is correct";
      	else
      		r2.label = "the sum is wrong";	
  }	  
  
  public void testCompareOperations(){
	    // equal: Test example    
	    LabeledRectangle lr1 = new LabeledRectangle( 15, 390, 20, 20 );
	    LabeledRectangle lr2 = new LabeledRectangle( 40, 390, 20, 20 );
	    if ( lr1.r.equal( lr2.r ) )
	      lr1.label = "equal";
	    else
	    	lr1.label = "not equal";
	    rectanglesPanel.add( lr1 );
	    rectanglesPanel.add( lr2 );
	    
	    // identical: Test example    
	    LabeledRectangle lr3 = new LabeledRectangle( 115, 390, 40, 40 );
	    LabeledRectangle lr4 = new LabeledRectangle( 115, 390, 40, 40 );
	    if ( lr3.r.identical( lr4.r ) )
	      lr3.label = "identical";
	    else
	    	lr3.label = "not identical";
	    rectanglesPanel.add( lr3 );
	    rectanglesPanel.add( lr4 );
  }
 
  
  public class RectanglesPanel extends JPanel {
  
	private static final long serialVersionUID = 1L;
	
	ArrayList <LabeledRectangle> rects;
	  Random rand = new Random();
	  Font font = new Font("Arial",Font.BOLD,10);
	  
	  public RectanglesPanel(int width, int height) {
		  this.setSize(width, height);
	  }

	  public RectanglesPanel() {
	     rects = new ArrayList<LabeledRectangle>();
	     setBackground( Color.black );
	  }

	  public void add( LabeledRectangle r ) {
	     rects.add( r );
	  }
	  
	  public Color randomColor(){
		  int nb = 75; // to avoid a random dark color
		  int maxValue = 255-nb;
		  return new Color(rand.nextInt(maxValue)+nb,rand.nextInt(maxValue)+nb,rand.nextInt(maxValue)+nb);
	  }

	  public void paint( Graphics g ) {
		 super.paint(g);
		 g.setFont(font);
	     for ( int i=0; i<rects.size(); i++ ) {
	    	 LabeledRectangle lr = rects.get(i);
	        g.setColor( (Color) randomColor() );
	        g.drawRect( lr.r.x, lr.r.y, lr.r.width, lr.r.height );
	        g.setColor(Color.WHITE);
	        g.drawString(lr.label, lr.r.x, lr.r.y-10);
	     }
	  }

	} // end of class RectanglesPanel
   
  	public class LabeledRectangle{
	  
	  String label;
	  Rectangle r;
	  
	  public LabeledRectangle(int x, int y, int width, int height){
		  r = new Rectangle(x, y, width, height);
		  label = "";
	  }  
	  
  } // end of class LabeledRectangle
  
  	public static void main( String[] argv ) {    
		 new TestRectangle();
    }
  	
} // end of class TestRectangle