import shutil
from generate import *
    
def main():
    src = "static/"
    dst = "public/"
    src_content = "content/index.md"
    template = "template.html"
    dst_content = "public/index.html"

    print("deleting public directory...")
    if os.path.exists(dst):
        shutil.rmtree(dst)
    
    print("copying static directory to public directory...")
    copy_directory(src, dst)

    print("generating page from markdown")
    generate_page(src_content, template, dst_content)

main()