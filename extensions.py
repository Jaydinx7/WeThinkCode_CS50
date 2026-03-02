# .gif image/gif
# .jpg image/jpeg
# .jpeg image/jpeg
# .png image/png
# .pdf application/pdf
# .txt text/plain
# .zip application/zip

extension = input("File name: ").strip().lower()


def main():
    if ".gif" in extension:
        print("image/gif")
    elif ".jpg" in extension or "jpeg" in extension:
        print("image/jpeg")
    elif ".png" in extension:
        print("image/png")
    elif ".pdf" in extension:
        print("application/pdf")
    elif ".txt" in extension:
        print("text/plain")
    elif ".zip" in extension:
        print("application/zip")
    else:
        print("application/octet-stream")


main()
