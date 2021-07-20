``` python
def solution(w,h):
    gradient = h / w
    width_count = 0; height_count = 0
    for i in range(1, w + 1):
        if (gradient * i) % 1 == 0:
            width_count = i
            height_count = gradient * width_count
            break
    return int(w * h - (width_count + height_count - 1) * w / width_count)
```
- 개같네 ㄹㅇ