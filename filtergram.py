import filters

def main():
    file_name = input("What is the filename you want to edit?")
    img = filters.load_img(file_name)

    filters.save_img(img, file_name)
    filters.show_img(img)
  # Ask what image the user wants to edit AKA get the filename from user
  # Load the image from the specified file
  # Save the final image


if __name__ == "__main__":
  main()
