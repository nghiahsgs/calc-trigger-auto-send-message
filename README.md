# calc-trigger-auto-send-message
calc trigger auto send message

```
Ở bài toán này, tool được đẩy vào ngày bắt đầu, ngày kết thúc + các khoảng thời gian để thực hiện auto gì đó. Ví dụ ngày bắt đầu là 10/02/2021 12h:00 đến ngày 15/02/2021 12h:00 và tần suất gửi là 30m 1 lần
```

Các tần suất được định nghĩa như sau

```
input:
start_time_str = ''
end_time_str = ''
freq_time = ''
additional_time = ''
```

```
output: Liệu đã đến lúc gửi tin chưa
```

freq_time:
```
Lặp lại hàng ngày
Lặp lại hàng tuần
Lặp lại hàng tháng (đúng ngày đó của tháng sau sẽ gửi)
Mọi ngày trong tuần từ thứ 2 đến thứ 6
Lặp lại trong ngày, vd điền 30 thì là 30 phút 1 lần
```
