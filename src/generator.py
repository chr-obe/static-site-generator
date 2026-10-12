import os

from markdown_blocks import markdown_to_html_node


def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no h1 header found")

def generate_page(basepath: str, from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    markdown = ""

    with open(from_path) as f:
        markdown = f.read()

    template = ""

    with open(template_path) as f:
        template = f.read()

    content = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(basepath: str, dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    if os.path.isfile(dir_path_content):
        generate_page(basepath, dir_path_content, template_path, dest_dir_path.replace(".md", ".html"))
        return

    content_dir_contents = os.listdir(dir_path_content)

    for item in content_dir_contents:
        new_dir_path = os.path.join(dir_path_content, item)
        new_dest_path = os.path.join(dest_dir_path, item)

        generate_pages_recursive(basepath, new_dir_path, template_path, new_dest_path)
