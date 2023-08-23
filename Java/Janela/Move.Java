public class Move implements Runnable {
  private Win win;
  public Move(Win win) {
      this.win = win;
  }
  @Override
  public void run() {
      for (;;) {
          try {
              Thread.sleep(200);
              int x = win.getLocation().x;
              int y = win.getLocation().y;
              x++;
              y++;
              win.setLocation(x, y);
          } catch (Execption e) {

          }
      }
  }
}