import os
import shutil
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def manage_files(source, destiny):
    source, destiny = Path(source), Path(destiny) 
    for p in source.iterdir():
        if os.path.isdir(p):
            new_destiny = destiny / p.name  
            os.mkdir(new_destiny)  
            manage_files(p, new_destiny)  
        else:
            file_dest = destiny / p.name  
            shutil.copyfile(p, file_dest)

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def extract_title(markdown):
    header = markdown.splitlines()
    
    for text in header:
        if text.startswith("# "):
            title = text.strip().replace("#","")
            return title
        
    raise Exception("no title found")

def generate_page(from_path,template_path, destiny_path):
    print(f"Generating page from {from_path} to {destiny_path} using {template_path}")
    md_file = open(from_path,"r+")
    temp = open(template_path,"r+")
    dest_path = open(destiny_path,"w")
    

    with (md_file as m,temp as t,dest_path as new_html):
        content = m.read()
        template = t.read()
        title = extract_title(content)
        html_string = markdown_to_html_node(content).to_html()
        template = template.replace("{{ Title }}",title)
        template = template.replace("{{ Content }}", html_string)
        if (os.path.dirname(destiny_path) != ""):
                os.makedirs(os.path.dirname(destiny_path), exist_ok=True)
        new_html.write(template)
        new_html.close()
        m.close()
        t.close()

    print(f"\n\n{destiny_path} generated.\n\n")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content, destiny = Path(dir_path_content), Path(dest_dir_path)
    os.makedirs(dest_dir_path, exist_ok=True)

    for item in content.iterdir():
        if os.path.isdir(item):
            new_dest_dir = destiny / item.name
            generate_pages_recursive(item, template_path, new_dest_dir)
        elif os.path.isfile(item) and item.suffix == ".md":
            output_path = destiny / (item.stem + '.html')
            generate_page(item, template_path, output_path)

    
        #print(content)

def main():
    dir_path_static = "./static"
    dir_path_public = "./public"
    dir_path_content = "./content"
    template_path = "./template.html"

    if os.path.exists("./public"):
        shutil.rmtree("./public")
    os.mkdir("./public")

    manage_files(dir_path_static, dir_path_public)
    #copy_files_recursive(dir_path_static, dir_path_public)

    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
    )
    
    
    
    

main()
