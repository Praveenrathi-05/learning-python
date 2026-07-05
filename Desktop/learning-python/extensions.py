def main():
    file_name = input("File name: ").lower().strip()
    seperator_count = file_name.count('.')
    if seperator_count == 1:
        name , extension = file_name.split(".")
        print(file_type(extension, name if extension == "txt" else ""))
    elif seperator_count == 2:
        name , _ , extension = file_name.split(".")
        print(file_type(extension, name if extension == "txt" else ""))
    else:
        print("application/octet-stream")

def file_type(extension, name = ""):
    if extension == "jpg":
        extension = "jpeg"
    match extension:
        case "gif" | "jpeg" | "png":
            return f"image/{extension}"
        case "pdf" | "zip" :
            return f"application/{extension}"
        case "txt":
            return f"text/{name}"
        case _:
            return "application/octet-stream"

main()
