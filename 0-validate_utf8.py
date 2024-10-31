def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple containing the start and end index for pagination."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)

