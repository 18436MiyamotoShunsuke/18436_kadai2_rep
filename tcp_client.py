import socket
with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
    #サーバを指定
    s.connect(('10.40.2.26',50007))
    #サーバにメッセージを送る
    s.sendall(b'helloaaa')
    #ネットワークのバッファサイズは1024,サーバからの文字列を取得する
    data=s.recv(1024)
    print(repr(data))