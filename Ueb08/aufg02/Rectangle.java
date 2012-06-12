import java.util.ArrayList;
import java.lang.Math;

/**
 * Klasse für Rechtecke im Koordinatensystem.   Rechtecke werden repräsentiert
 * durch die Koordinaten der linken unteren Ecke sowie durch Breite und Höhe.
 * Ihre Seiten sind immer parellel zu den Koordinatenachsen.
 */
public class Rectangle {
    int x, y, width, height;

    /**
     * Creates a new Rectangle.
     *
     * @param x      abscissa of the Rectangle's lower left corner
     * @param y      ordinate of the Rectangle's lower left corner
     * @param width  the Rectangle's width
     * @param height the Rectangle's height
     */
    public Rectangle(int x, int y, int width, int height) {
        this.x      = x;
        this.y      = y;
        this.width  = width;
        this.height = height;
    }


    /**
     * Creates a new standard Rectangle.   The standard rectangle is position
     * in the point of origin and its height and width are 10.
     */
    public Rectangle() {
        this(0, 0, 10, 10);
    }


    /**
     * Tests whether this Rectangle shares size and position with another.
     *
     * @param that  a Rectangle to be compared with this
     * @return   <code>true</code> if they share size and position
     *           <code>false</code> otherwise
     */
    public boolean identical(Rectangle that) {
        return this.x      == that.x
            && this.y      == that.y
            && this.width  == that.width
            && this.height == that.height;
    }

    //public Rectangle clone()
        // wird geerbt


    /**
     * Tests whether this <code>Rectangle</code> and that have the same area.
     *
     * @param that  a <code>Rectangle</code> whose area is to be compared with
     *              this'
     * @return   <code>true</code> if they have the same area
     *           <code>false</code> otherwise
     */
    public boolean equal(Rectangle that) {
        return this.area() == that.area();
    }

    /**
     * Calculates the area of this <code>Rectangle</code>.
     *
     * @return  the area of this <code>Rectangle</code>
     */
    public int area() {
        return this.width * this.height;
    }

    /**
     * Test whether a <code>Rectangle</code> overlaps with this one.
     *
     * @param that   a <code>Rectangle</code> tested whether it overlaps with
     *               this
     * @return  <code>true</code> if they overlap
     *          <code>false</code> otherwise
     */
    public boolean overlaps(Rectangle that) {
        return this.x               < that.x + that.width
            && this.y               < that.y + that.height
            && this.x + this.width  > that.x
            && this.y + this.height > that.y;
    }

    /**
     * Test whether this <code>Rectangle</code> contains another one.
     *
     * @param that  a <code>Rectangle</code> tested whether it is contained by
     *              this one
     * @return <code>true</code> if this contains that
     *         <code>false</code> otherwise
     */
    public boolean contains(Rectangle that) {
        return this.y <= that.y && this.x <= that.x
            && this.x + this.width  >= that.x + that.width
            && this.y + this.height >= that.y + that.height;
    }


    /**
     * Calculate the complete sumOfSquares of this <code>Rectangle</code>
     * into squares. This is done by dividing the rectangle into a square of
     * min(width, height) side length and a remaining rectangle that is
     * recursively divided up. If min(width, height) of the remaining
     * rectangle is 1 or 0, it is completely decomposed.
     *
     * @return  an <code>ArrayList</code> containing the squares this
     *          <code>Rectangle decomposes into</code>
     */
    public ArrayList<Rectangle> sumOfSquares() {
        // Create empty list for the squares this is to be decomposed into
        ArrayList<Rectangle> square_list = new ArrayList();

        // Decompose this recursively
        return this.decompose_further(square_list);
    }

    /**
     * Sub-method for {@link sumOfSquares}.   This method does the real
     * end-recursive work.
     *
     * @param square_list  an <code>ArrayList</code> of
     *                     <code>Rectangle</code>s containing the squares the
     *                     <code>Rectangle</code>  has been divided into
     *                     already
     * @return  an <code>ArrayList</code> of all squares the
     *          <code>Rectangle</code> decomposes into
     */
    private ArrayList<Rectangle>
        decompose_further(ArrayList<Rectangle> square_list) {
        Rectangle rem_rect;

        // New square sits in the lower part of the array
        if (this.width < this.height) {
            // Add new square to the list
            square_list.add(new Rectangle(this.x, this.y, width, width));

            // Create object for remaining Rectangle
            rem_rect   = new Rectangle(
                                 this.x, this.y + width,
                                 width, height - width
                             );
        }
        // New square sits in the left part of the array
        else if (this.width > this.height) {
            square_list.add(new Rectangle(this.x, this.y, height, height));
            rem_rect   = new Rectangle(
                                 this.x + height, this.y,
                                 width - height, height
                             );
        }
        // (Remaining) array is square already (anchor)
        else {
            return square_list;
        }

        // Decompose even further
        return rem_rect.decompose_further(square_list);
    }
}
