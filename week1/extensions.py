def main():

    # Prompt user for file name and split into file name and extension
    file, extension = input("File name: ").split(".")

    # Determine MIME type based on file extension using match statement
    match extension.lower():
        case "gif" | "jpg" | "jpeg":
            mime = "image"
        case "pdf":
            mime = "document"
        case "zip":
            mime = "archive"
        case "txt":
            mime = "text"
        # If file extension does not match any of the specified cases, set MIME type to application/octet-stream
        case _:
            mime = "application/octet-stream"

    # Print MIME type based on determined MIME type and file extension
    if mime == "application/octet-stream":
        print("application/octet-stream") 
    else:
        print(f"{mime}/{extension.lower()}")    

main()