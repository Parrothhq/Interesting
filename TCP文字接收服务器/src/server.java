//һ�ѵ���������ñ��������㵼�뼴��
import java.io.DataInputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class server{
    private int port = 123;  //���������Ŷ˿ڣ���Clientһ�£�
    public server(){ }
    public server(int port){this.port = port;}  //���췽��
    public void service(){  //��������ʾ������
        try{  //try-catch��Χ
            ServerSocket server = new ServerSocket(port);  //��server�Ͽ��Ŷ˿�
            Socket socket = server.accept();  //���server��IP������װSocket
            try{
                DataInputStream inputStream = new DataInputStream(socket.getInputStream());  //ȡ������������ַ�

                while(true){  //һֱ��ȡ
                    String accept = inputStream.readUTF();  //�����������ַ�������accept����
                    System.out.println(accept);  //��ӡ����
                }
            }finally {
                socket.close();  //�ر�����
                server.close();  //�رշ���
            }
        }catch (IOException e){
            e.printStackTrace();
        }
    }

    public static void main(String[] args){
        new server().service();
    }
}

