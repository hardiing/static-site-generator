import os
import shutil
from markdown_blocks import *
from htmlnode import HTMLNode

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

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line.strip("# ")
            return title
    raise Exception("no h1 found")

def generate_page(from_path, template_path, dest_path):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")
    f = open(from_path, "r")
    md = f.read()
    f.close()

    f = open(template_path, "r")
    template = f.read()
    f.close()

    node = markdown_to_html_node(md)
    html = node.to_html()

    title = extract_title(md)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path == "":
        os.makedirs(dest_dir_path, exist_ok=True)
    f = open(dest_path, "w")
    f.write(template)