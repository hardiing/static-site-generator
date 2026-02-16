import shutil
import os
import sys
from generate import *
    
def main():
    if len(sys.argv) >= 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    src = "static/"
    src_content = "./content"
    template = "./template.html"
    dst_content = "./docs"

    print("deleting public directory...")
    if os.path.exists(dst_content):
        shutil.rmtree(dst_content)
    
    print("copying static directory to public directory...")
    copy_directory(src, dst_content)

    print("generating pages from markdown")
    generate_pages_recursive(src_content, template, dst_content, basepath)

main()