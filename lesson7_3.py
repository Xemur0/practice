import os
import shutil

my_project = r'C:\Users\Александр\PycharmProjects\Xemur0\my_project'
templates_dir = os.path.join(my_project, 'templates')
try:
    if not os.path.exists(templates_dir):
        os.mkdir(templates_dir)
    for main_dir in os.listdir(my_project):
        templs = [a for a in os.scandir(os.path.join(my_project, main_dir)) if a.name == 'templates']
        for b in templs:
            b_dir = os.path.join(templates_dir, main_dir)
            if not os.path.exists(b_dir):
                os.mkdir(b_dir)
            for root, dir, file in os.walk(b):
                for f in os.scandir(root):
                    if f.is_file():
                        shutil.copyfile(f.path, os.path.join(b_dir, f.name))
except FileNotFoundError:
    print('Запустите сначала файлик lesson7_2.py')