N = int(input())
for e in range(1,N+1):
	T = int(input())
	# nhap nhieu input
	a = list(map(int, input().split()))
	b = []
	y =	[]
	z = []
	i = 0
	j = 0
	for t in range(0,T):
		i += 1
		j += 1
		if a[i-1] > a[-j]:
			b.append(a[-j])
			i = i-1
		elif a[i-1] <= a[-j]:
			b.append(a[i-1])
			j = j-1

	y.append(b[0])
	for x	in range(0,T-1):
		if b[x] <= b[x+1]:
			y.append(b[x+1])
			d = len(y)

	max_so_far = y[0]
	z=[]
	# đây là cách so sánh để tìm đc dãy có số nào lớn hơn vì khi m >= số lớn nhất hiện tại thì khi tìm đc m thì h m mới là số lớn nhất hiện tại và tiếp m khác
	for m in y:
		if m >= max_so_far:
			z.append(m)
			max_so_far = m

	zl = len(z)

	
	
			# d = len(c)


				
	print('Case #' + str(e)+': ' +str(zl))
	# print(f)