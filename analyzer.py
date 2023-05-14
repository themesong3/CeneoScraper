import os


print(*list(map(lambda x: x.split(".")[0], os.listdir("./opinions"))),sep='\n' )