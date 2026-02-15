import shutil
import os
from generate import *
    
def main():
    src = "static/"
    dst = "public/"
    src_content = "./content"
    template = "./template.html"
    dst_content = "./public"

    print("deleting public directory...")
    if os.path.exists(dst):
        shutil.rmtree(dst)
    
    print("copying static directory to public directory...")
    copy_directory(src, dst)

    print("generating pages from markdown")
    generate_pages_recursive(src_content, template, dst_content)

main()