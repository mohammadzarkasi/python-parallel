public class MyThread extends  Thread{
    private  int start, akhir;
    MyThread(int start, int akhir){
        this.start=start;
        this.akhir=akhir;
    }

    @Override
    public void run() {
        for(int i = start; i < akhir; i++){
            System.out.println("angka: " + i);
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
