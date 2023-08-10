import sys
input = sys.stdin.readline

import sys
input = sys.stdin.readline

def getsfxarr(s):
	n = len(s)
	t = 1
	sfxarr = list(range(n))
	group = [ord(s[i]) for i in range(n)] + [-1]
	newgroup = [0 for _ in range(n + 1)]
	newgroup[sfxarr[0]] = 0
	newgroup[n] = -1
	while t < n:
		sfxarr.sort(key = lambda x: (group[x], group[min(x+t, n)]))
		# print(sfxarr, group, newgroup)
		for i in range(1, n):
			p, q = sfxarr[i-1], sfxarr[i]
			if group[p] != group[q] or group[min(p + t, n)] != group[min(q + t, n)]:
				newgroup[q] = newgroup[p] + 1
			else:
				newgroup[q] = newgroup[p]
		group = newgroup[:]
		t <<= 1
	return sfxarr

def getlcp(s):
	n = len(s)
	sfxarr = getsfxarr(s)
	k = 0
	lcp = [0 for _ in range(n)]
	inv_sfxarr = [0 for _ in range(n)]
	for i in range(n):
		inv_sfxarr[sfxarr[i]] = i
	for i in range(n):
		if inv_sfxarr[i]:
			j = sfxarr[inv_sfxarr[i] - 1]
			while (j + k < n and i + k < n) and s[j + k] == s[i + k]:
				k += 1
			lcp[inv_sfxarr[i]] = k
			if k > 0:
				k -= 1
	return lcp

def best():
	s = input().rstrip()
	n = len(s)
	print(n*(n+1)//2 - sum(getlcp(s)))

if __name__ == "__main__":
	# solution()
	best()