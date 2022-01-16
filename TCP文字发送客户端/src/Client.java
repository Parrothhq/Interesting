//һ�ѵ�����䣬���ñ����������Զ�����ȥ
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

//����
public class Client{
    private String host = "localhost";  //serve�ĵ�ַ
    private int port = 123;  //server��port

    public Client(){}

    public Client(String host, int port){  //���췽��
        this.host = host;
        this.port = port;
    }

    public void chat(){   //������Ϣ����
        try{  //ʹ��try-catchΧ��
            Socket socket = new Socket(host, port);  //��Ŀ��Socket����ϵͳ
            try {  //ʹ��try-catchΧ��
                DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());  //���Ὣ�����ַ��ŵ�dataOutputStream�У����ɴ���server
                Scanner scanner = new Scanner(System.in);  //Scanner������������
                while (true){  //һֱִ��
                    String send = scanner.nextLine();  //���������ݱ�����send����
                    dataOutputStream.writeUTF(send);   //��send����dataOutputStream����ʼ����
                }
            }finally {
                socket.close();  //ǿ����ֹ�󣬹ر�����
            }
        }catch (IOException e){  //�������
            e.printStackTrace();
        }
    }
    public static void main(String[] args){
        new Client().chat();
    }  //newһ��Client��chat����������ʼִ��
}