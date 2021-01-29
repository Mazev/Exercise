version = ''.join(map(str,input().split('.')))
new_version = '.'.join(str(int(version) + 1 ))
print(new_version)