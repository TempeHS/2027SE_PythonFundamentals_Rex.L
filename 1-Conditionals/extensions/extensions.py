userFile = input("Enter a file name: ").lower()

if userFile.endswith("gif"):
      print("image/gif")
elif userFile.endswith("jpg") or userFile.endswith("jpeg"):
      print("image/jpeg")
elif userFile.endswith("png"):
      print("image/png")
elif userFile.endswith("pdf"):
      print("application/pdf")
elif userFile.endswith("txt"):
      print("text/plain")
elif userFile.endswith("zip"):
      print("application/zip")
else:
      print("application/octet-stream")