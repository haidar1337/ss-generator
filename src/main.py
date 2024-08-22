from htmlnode import LeafNode
from page_generator import generate_page, generate_pages_recursive
from textnode import TextNode
from util import *
from text_types import *
import os as os
import shutil as shutil

def main():
    copy_directory_recursively("static", "public")

    generate_pages_recursive("content", "template.html", "public")

def copy_directory_recursively(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)

    for dirc in os.listdir(source):
        if os.path.isfile(os.path.join(source, dirc)):
            shutil.copy(os.path.join(source, dirc), destination)
        else:
            os.mkdir(os.path.join(destination, dirc))
            copy_directory_recursively(os.path.join(source, dirc), os.path.join(destination, dirc))

main()