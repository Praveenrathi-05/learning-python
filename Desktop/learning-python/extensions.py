def main():
    file_name = input("File name: ").strip().lower()

    if "." in file_name:
        extension = file_name.rsplit(".", 1)[1]
    else:
        extension = ""

    match extension:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "zip":
            print("application/zip")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")

main()
