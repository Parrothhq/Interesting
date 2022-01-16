//一堆导入语句，可让编译器帮你自动加上去
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

//主类
public class Client{
    private String host = "localhost";  //serve的地址
    private int port = 123;  //server的port

    public Client(){}

    public Client(String host, int port){  //构造方法
        this.host = host;
        this.port = port;
    }

    public void chat(){   //发送信息方法
        try{  //使用try-catch围绕
            Socket socket = new Socket(host, port);  //将目标Socket交给系统
            try {  //使用try-catch围绕
                DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());  //待会将输入字符放到dataOutputStream中，即可传到server
                Scanner scanner = new Scanner(System.in);  //Scanner读入输入内容
                while (true){  //一直执行
                    String send = scanner.nextLine();  //把输入内容保存在send变量
                    dataOutputStream.writeUTF(send);   //将send交给dataOutputStream，开始传输
                }
            }finally {
                socket.close();  //强制终止后，关闭连接
            }
        }catch (IOException e){  //报错输出
            e.printStackTrace();
        }
    }
    public static void main(String[] args){
        new Client().chat();
    }  //new一个Client的chat方法，程序开始执行
}