from collections import deque
from collections import defaultdict
nums = [11,0,1,10,5,19]

# d is dict with key as 
d = {}

spoken = deque([], maxlen=100)

times_spoken = defaultdict(lambda: 0)

turn = 0

while True:
    turn += 1
    print(f"Turn {turn}")
    if nums:
        n = nums.pop(0)
        temp_q = deque([], maxlen=2)
        temp_q.append(turn)
        d[n] = temp_q
        print(f"The number spoken is a starting number.")
        print(f"Say {n}")
        spoken.append(n)
    else:
        last_spoken = spoken[-1]
        print(f"last spoken was {last_spoken}")
        print(f"num times this has been spoken is {times_spoken[last_spoken]}")
        if times_spoken[last_spoken] == 0:
            n = 0
        else:
            # print("calc diff")
            if len(d[last_spoken]) == 1:
                n = 0
            else:    
                diff = d[last_spoken][1] - d[last_spoken][0]
                print(f"diff is {diff}")
                n = diff

        print(f"Say {n}")
        spoken.append(n)
        times_spoken[n] += 1
        if n in d:
            d[n].append(turn)
        else:
            d[n] = deque([turn], maxlen=2)

    if turn == 2020:
        print(f"the answer is {n}")
        break
