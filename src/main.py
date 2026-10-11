import os
import shutil


def main() -> None:
    copy_file_contents("static/", "public/", True)

def copy_file_contents(src: str, dest: str, top_level: bool = False) -> None:
    # check for valid paths
    if not os.path.exists(src):
        raise ValueError(f"invalid path: {src}")

    if top_level:
        if os.path.exists(dest):
            shutil.rmtree(dest)
        os.mkdir(dest)

    if not os.path.isfile(src):
        contents = os.listdir(src)
        print(contents)
        for content in contents:
            new_src = os.path.join(src, content)
            new_dest = os.path.join(dest, content)
            if not os.path.isfile(new_src):
                os.mkdir(new_dest)
                copy_file_contents(new_src, new_dest)
            else:
                print(f"copying {new_src} to {new_dest}")
                shutil.copy(new_src, new_dest)
    else:
        shutil.copy(src, dest)

if __name__ == "__main__":
    main()
