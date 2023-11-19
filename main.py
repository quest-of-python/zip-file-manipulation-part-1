import pathlib


from zip_manipulation import retrieve_text_file_names


def main():
    archive_path = pathlib.Path("random_files.zip")

    print(retrieve_text_file_names(archive_path))


if __name__ == '__main__':
    main()
