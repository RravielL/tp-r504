//ServeurTCP1.java
ServerSocket socketserver = new ServerSocket( 2016 );
System.out.prinln( "serveur en attente" );
Socket socket = socketserver.accept();
System.out.println( "Connection d'un client" );
DataInputStream dIn = new DataInputStream( socket.getInputStream() );
System.out.println( "Message : " + dIn.readUTF());

socket.close();
socketserver.close();