if __name__=="__main__":
    socks_list = [int(input()) for _ in range(5)]
    socks_set = set()
    
    for sock in socks_list:
        if sock in socks_set:
            socks_set.remove(sock)
        else:
            socks_set.add(sock)
    
    [print(sock) for sock in socks_set]