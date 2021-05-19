import datetime
from utils_check_job_now import *

if __name__ =="__main__":
    start_time_str = '2021-05-19 18:49:00'
    end_time_str = '2021-10-26 19:49:00'
    start_time = datetime.datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')

    now = datetime.datetime.now()
    T_loop_min = 5 # 5phut bot quet 1 lan


    # Lặp lại hàng ngày
    freq_time = 1
    # # Lặp lại hàng tuần
    freq_time = 2
    # # Lặp lại hàng tháng (đúng ngày đó của tháng sau sẽ gửi)
    freq_time = 3
    # # Mọi ngày trong tuần từ thứ 2 đến thứ 6
    freq_time = 4
    # # Lặp lại trong ngày, vd điền 30 thì là 30 phút 1 lần
    freq_time = 5
    additional_time = 30

    while True:
        print(now)
        kq = is_now_valid(start_time,end_time,now,freq_time,additional_time,T_loop_min)
        if kq:
            print('---------',now)
            write_file_line('code.html','%s'%now)
        now += datetime.timedelta(minutes=T_loop_min)