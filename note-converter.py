

import os

if __name__ == "__main__" :
    files = os.listdir()
    notes = [file for file in files if (file.endswith(".md") and not file.startswith("README"))]
    # get all changed files from git
    changed = os.popen("git diff --name-only").read().splitlines()
    # filter out files that are not changed
    converted_files = [file for file in notes if file in changed]


    for file in converted_files:
        print(f"Converting {file} to pdf...")
        try:
            os.system(f'pandoc {file} -o {file.split(".md")[0]}.pdf')
            print("Done!")
        except Exception as e:
            print(f"Conversion failed: {e}")