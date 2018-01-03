
ACCOUNT = "zhoupengzu"
PASSWORD = "zhoupengzu"

print('请输入用户名:')
user_account = input()
print('请输入密码:')
user_password = input()
if user_account == ACCOUNT and user_password == PASSWORD :
    print('Login Success!')
else:
    print('Login failed!')

