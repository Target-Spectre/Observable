from os.path \
    import dirname, join, isdir

current_file_location: str | None = None


def get_current_file_location() -> str:
    global current_file_location

    if current_file_location is None:
        current_file_location = __file__

    return current_file_location


def set_current_file_location(
    file_path: str
) -> None:
    global current_file_location
    current_file_location = file_path


current_directory_location: str | None = None


def get_current_directory_location() -> str:
    global current_directory_location

    if current_directory_location is None:
        set_current_directory_location(
            dirname(
                get_current_file_location()
            )
        )

    return current_directory_location


def set_current_directory_location(
    value: str
) -> None:
    global current_directory_location
    current_directory_location = value
