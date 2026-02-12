userFile = input("Enter a file name: ").lower()

match userFile:
      case userFile.endswith("gif"):
            print("image/gif")
      case userFile.endswith("jpg") | userFile.endswith("jpeg"):
            print("image/jpeg")
      case userFile.endswith("png"):
            print("image/png")
      case userFile.endswith("pdf"):
            print("application/pdf")
      case userFile.endswith("txt"):
            print("text/plain")
      case userFile.endswith("zip"):
            print("application/zip")
      case _:
            print("application/octet-stream")