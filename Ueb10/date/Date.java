package date;

public interface Date {
    public int getDay();
    public int getMonth();
    public int getYear();
    public Date getDate();

    public void nextDay();
    public void setDate(int day, int month, int year)
           throws IllegalDateException;
    public boolean after(Date date);
    public boolean before(Date date);
    public String toString();
}
