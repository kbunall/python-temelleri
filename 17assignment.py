# x = 5
# y = 10
# z = 20
# x,y,z = 5,10,20

# x += 5 # x = x + 5
# x -= 5 # x = x - 5
# x *= 5 # x = x * 5
# x /= 5 # x = x / 5
# x %= 5 # x = x % 5 Mod alma
# y //= 5 # y = y // 5 Tam bölme
# y **= 5 # y = y ** 5 Üslü alma

values = 1,2,3

print(values)
print(type(values))

x,y,*z=values

print(x,y,z[0])