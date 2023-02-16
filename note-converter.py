

import os

if __name__ == "__main__" :
    for i in range(1, 30):
        print(f"Converting {i:02d}.02.23.md to {i:02d}.02.23.pdf")
        try:
            os.system(f"pandoc {i:02d}.02.23.md -o {i:02d}.02.23.pdf")
            print("Done!")
        except Exception as e:
            print(f"Conversion failed: {e}")