

import os

if __name__ == "__main__" :
    files = os.listdir()
    notes = [file for file in files if (file.endswith(".md") and not file.startswith("README"))]
    # get all changed files from git
    changed = os.popen("git diff --name-only").read().splitlines()
    # filter out files that are not changed
    converted_files = [file for file in notes if file in changed]


    # Update files
    for file in converted_files:
        print(f"Converting {file} to pdf...")
        try:
            os.system(f'pandoc {file} -o {file.split(".md")[0]}.pdf')
            print("Done!")
        except Exception as e:
            print(f"Conversion failed: {e}")


    # Update README.md
    print("Updating README.md...")
    readme = open("README.md", "w")
    readme.write("# AfetBilgi Notlar\n")
    readme.write("""
[tr] AfetBilgi nin geliştirilme sürecinde aldığım notları burada paylaşacağım. Sürecin düzenli ve dürüst bir anlatımı olması açısından, ileride geriye baktığımızda yaptığımız hataları görebilmemiz, neleri düşünmüştük de unuttuk acaba diye araştırmamız açısından iyi olacağını düşünüyorum.

[en] I'll share the notes I took during the development of AfetBilgi here. I think it will be good for us to be able to see the mistakes we made in the process, to be able to research what we thought of but forgot later, also to have a regular and honest explanation of the process.\n""")
    readme.write("\n## Notlar\n")
    for file in sorted(notes):
        readme.write(f"\n- [{file.split('.md')[0]}](./{file})")

    readme.write("\n")
    readme.close()