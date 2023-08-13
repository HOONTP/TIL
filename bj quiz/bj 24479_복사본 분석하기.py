from sys import stdin, stdout
def main():
    n, m, r = map(int, stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0]*(n + 1)
    stack = [r]
    for a, b in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
        graph[a].append(b)
        graph[b].append(a)
    order = 1
    while stack:
        print(stack) #다 넣었으니까 뒤에서부터 뺸다.
        cur = stack.pop()#제일 마지막에 들어간 수를 빼고
        if visited[cur]:#아직 안들어간 곳이면 진행
            continue
        visited[cur] = order#99에 2를 부여? 왜? 아니었죠 / 들어갔으니 다음 번호 부여
        order += 1
        for nex in sorted(graph[cur], reverse=True):#만약 99부터 2까지 들어갔따치자.
            # 새로 들어온 곳 역순으로 다 넣음. 방문한 곳은 제외.
            if not visited[nex]:#0이면 트루라서 진행
                stack.append(nex)
    stdout.write("\n".join(map(str, visited[1:])))

main()