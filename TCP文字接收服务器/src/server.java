//一堆导入操作，让编译器帮你导入即可
import java.io.DataInputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class server{
    private int port = 123;  //服务器开放端口（与Client一致）
    public server(){ }
    public server(int port){this.port = port;}  //构造方法
    public void service(){  //服务器显示主方法
        try{  //try-catch包围
            ServerSocket server = new ServerSocket(port);  //在server上开放端口
            Socket socket = server.accept();  //获得server的IP，并组装Socket
            try{
                DataInputStream inputStream = new DataInputStream(socket.getInputStream());  //取出传输过来的字符

                while(true){  //一直读取
                    String accept = inputStream.readUTF();  //将传过来的字符保存在accept变量
                    System.out.println(accept);  //打印出来
                }
            }finally {
                socket.close();  //关闭连接
                server.close();  //关闭服务
            }
        }catch (IOException e){
            e.printStackTrace();
        }
    }

    public static void main(String[] args){
        new server().service();
    }
}

