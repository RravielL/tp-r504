import java.io.*;
import java.net.*;

public class ServeurUDP
{
	public static void main ( String [ ] args )
	{
		try
		{

			//ServeurTCP1.java
			ServerSocket socketserver = new ServerSocket( 2016 );
			System.out.println( "serveur en attente" );
			Socket socket = socketserver.accept();
			System.out.println( "Connection d'un client" );
			DataInputStream dIn = new DataInputStream( socket.getInputStream() );
			System.out.println( "Message : " + dIn.readUTF());

			socket.close();
			socketserver.close();
		}
		catch( Exception e )
		{
			System.out.println ( " erreur ! " ) ;
		}
	}
}
