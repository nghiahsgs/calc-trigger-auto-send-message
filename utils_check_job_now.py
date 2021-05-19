import datetime
import io

def write_file_line(file_name,ndung_line):
    f = io.open(file_name, 'a', encoding='utf-8')
    f.write('%s\n'%ndung_line)
    f.close()

def is_now_valid(start_time,end_time,now,freq_time,additional_time,T_loop_min):
    if start_time<now and now<end_time:
        delta_minute = (now - start_time).total_seconds()/60
        # Lặp lại hàng ngày
        if freq_time==1:
            if delta_minute%(24*60)<T_loop_min:
                print('send_message')
                return True
                
        
        # Lặp lại hàng tuần
        elif freq_time ==2:
            if delta_minute%(7*24*60)<T_loop_min:
                print('send_message')
                return True
            
        # Lặp lại hàng tháng (đúng ngày đó của tháng sau sẽ gửi)
        elif freq_time==3:
            if now.day==start_time.day:
                if delta_minute%(24*60)<T_loop_min:
                    print('send_message')
                    return True
        
        # Mọi ngày trong tuần từ thứ 2 đến thứ 6
        elif freq_time==4:
            if now.weekday()<5:
                if delta_minute%(24*60)<T_loop_min:
                    print('send_message')
                    return True
        # Lặp lại trong ngày, vd điền 30 thì là 30 phút 1 lần
        elif freq_time==5:
            if delta_minute%(additional_time)<T_loop_min:
                print('send_message')
                return True
