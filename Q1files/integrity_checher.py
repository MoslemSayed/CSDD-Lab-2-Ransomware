import hashlib,sys,os

def file_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def main():
    expected_hash = open("Q1hash.txt", "r").read()
    for file in os.listdir("."):
        if file.endswith(".exe"):
            computed_hash = file_hash(file)
            if computed_hash == expected_hash:
                print("file found:", file)
                open("result.txt", "w").write(file+":"+computed_hash)
                break

if __name__ == "__main__":
    main()