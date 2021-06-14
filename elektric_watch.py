#a = int(input())
#print(str(int(a / 60))+':'+ str(int(a % 60)))
n = int(input())
hours = n % (60 * 24) // 60
minutes = n % 60
#print(str(hours), str(minutes).split(':'))
print('%2d:%02d' % ((n / 60), (n % 60)))
