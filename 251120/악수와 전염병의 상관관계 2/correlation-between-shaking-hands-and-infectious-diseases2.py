N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

handshakes.sort(key=lambda x: x[0])

infected = [P]

for h in handshakes:
    if h[1] in infected or h[2] in infected:
        if h[1] in infected and h[2] in infected:
            if infected.count(h1) < 1 + K:
                infected.append(h[1])

            if infected.cunt(h2) < 1 + K:
                infected.append(h[2])

        
        elif h[1] in infected and h[2] not in infected:
            if infected.count(h[1]) < 1 + K:
                infected.append(h[1])
                infected.append(h[2])
        
        elif h[2] in infected and h[1] not in infected:
            if infected.count(h[2]) < 1 + K:
                infected.append(h[1])
                infected.append(h[2])

    else:
        continue



people = [i+1 for i in range(N)]
answer = []

for i in range(N):
    if people[i] in infected:
        answer.append('1')
    
    else:
        answer.append('0')

print("".join(answer))
