from util import extract_title, markdown_to_html_node
from htmlnode import HTMLNode
import os as os

def generate_page(from_path, template_path, dest_path):
    print("============================================================================")
    print(f"Genertaing page from {from_path} to {dest_path} using {template_path}...")
    print("============================================================================")

    content = ""
    template_content = ""

    with open(from_path) as f:
        content = f.read()
        f.close()

    with open(template_path) as f:
        template_content = f.read()
        f.close()

    html = markdown_to_html_node(content).to_html()
    title = extract_title(content)

    escaped_opening_brace = f"{{"
    split = template_content.split("\n")
    for i in range(len(split)):
        stripped = split[i].strip()
        if stripped.startswith("<title>"):
            split[i] = "<title> " + title + " </title>"
        if stripped.startswith(escaped_opening_brace*2):
            split[i] = html
            break

    template_content = "\n".join(split)

    with open(dest_path, "w") as f:
        f.write(template_content)
        f.close()

    print(f"Successfully generated page at {dest_path} using {template_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, file) # content/index.md
        to_path =  os.path.join(dest_dir_path, file) # public/index.md
        print(f"from: {from_path}, to: {to_path}")
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, to_path.replace(".md", ".html"))
        else:
            os.mkdir(to_path)
            generate_pages_recursive(from_path, template_path, to_path)