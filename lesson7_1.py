import os

root_dir = 'my_project'
dirs = 'settings', 'mainapp', 'adminapp', 'authapp', 'something'

for i in dirs:
    dir_path = os.path.join(root_dir, i)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)




