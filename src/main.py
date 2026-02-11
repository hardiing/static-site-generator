from textnode import TextNode, TextType
import os
import shutil
import errno

def copy_directory(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)

    for item in os.listdir(source):
        from_path = os.path.join(source, item)
        to_path = os.path.join(destination, item)
        print(f" * {from_path} copied to {to_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_directory(from_path, to_path)

def main():
    src = "static/"
    dst = "public/"

    print("deleting public directory...")
    if os.path.exists(dst):
        shutil.rmtree(dst)
    
    print("copying static directory to public directory...")
    copy_directory(src, dst)

main()