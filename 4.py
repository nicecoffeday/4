passward = '123456'
i = 3
while i > 0:
	i = i - 1
	pwd = input('請輸入密碼')
	if pwd == passward:
		print('密碼正確')
		break#跳出迴圈
	else:
		print('密碼錯誤')
		if i > 0:
			print('還有', i, '機會')
		else:
			print('掰掰')
	