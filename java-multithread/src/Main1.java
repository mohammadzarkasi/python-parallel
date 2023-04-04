public class Main1 {
    public static void hitung(int awal, int akhir){
        var threadName = Thread.currentThread().getName();
        for(int i = awal; i<akhir;i++){
            System.out.println(threadName + " : " + i);
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    public static void main(String[] args) {
        try {
            var t1 = new Thread(new Runnable() {
                @Override
                public void run() {
                    hitung(1, 20);
                }
            });
            var t2 = new Thread(new Runnable() {
                @Override
                public void run() {
                    hitung(30, 50);
                }
            });

//            var t1 = new MyThread(0,50);
//            var t2 = new MyThread(50,100);

            t1.setPriority(1);
            t2.setPriority(1);
            t1.setName("01-sampai-20");
            t2.setName("30-sampai-50");

            System.out.println("akan menjalankan thread");

            t1.start();
            t2.start();

            System.out.println("thread telah dimulai");

            t1.join();
            t2.join();
        }
        catch (Exception x){
            x.printStackTrace();
        }
    }
}
