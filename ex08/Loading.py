def ft_tqdm(lst: range) -> None:
    """
    Iterate over a given list/range while displaying a progress bar.

    Args:
        lst (range): A list or range over which to iterate.

    Yields:
        The next value from the list/range.

    Usage:
        for item in ft_tqdm(my_list):
            process(item)
    """
    total_length = len(lst)

    def print_progress_bar(completed):
        bar_length = 100
        progress = int((completed / total_length) * bar_length)
        bar = '█' * progress + '-' * (bar_length - progress)
        percentage = int((completed / total_length) * 100)
        print(f'{percentage}%|{bar}| {completed}/{total_length}', end='\r')

    for i, value in enumerate(lst):
        print_progress_bar(i + 1)
        yield value
