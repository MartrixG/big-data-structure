import time
import random
import threading
num_ips = 500000
base_time = 1588504628
tot_secs = 2592000
def convert_time(secs):
    return time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(secs))

def random_ip():
    m = random.randint(0,255)
    n = random.randint(0,255)
    x = random.randint(0,255)
    y = random.randint(0,255)
    randomIP=str(m) + '.' + str(n) + '.' + str(x) + '.' +str(y)
    return randomIP

def prepare_ip():
    ips = []
    for i in range(num_ips):
        ips.append(random_ip())
    return ips

def generate_log(filename, ips):
    f = open(filename, 'w+')
    for i in range(tot_secs):
        if random.randint(0, 10000) == 4396:
            attack_ip = random.choice(ips)
            for j in range(100):
                print(convert_time(base_time + float(i)), attack_ip, file=f)
        else:
            for j in range(random.randint(0, 5)):
                print(convert_time(base_time + float(i)), random.choice(ips), file=f)

if __name__ == "__main__":
    ips = prepare_ip()
    threads = []
    t1 = threading.Thread(target=generate_log, args=("server1.log", ips))
    threads.append(t1)
    t2 = threading.Thread(target=generate_log, args=("server2.log", ips))
    threads.append(t2)
    t3 = threading.Thread(target=generate_log, args=("server3.log", ips))
    threads.append(t3)
    t4 = threading.Thread(target=generate_log, args=("server4.log", ips))
    threads.append(t4)
    t5 = threading.Thread(target=generate_log, args=("server5.log", ips))
    threads.append(t5)
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print("all threads finished.")