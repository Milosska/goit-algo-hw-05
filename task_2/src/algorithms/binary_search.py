def binary_search(element: float, array: list[float]) -> tuple[int, float]:
    iterration_count = 0
    min_elem_index = 0
    max_elem_index = len(array) - 1

    while min_elem_index <= max_elem_index:
        iterration_count += 1
        mid_elem_index = (min_elem_index + max_elem_index) // 2
        nearest_value = array[mid_elem_index]

        if nearest_value == element:
            return (iterration_count, nearest_value)

        elif nearest_value > element:
            max_elem_index = mid_elem_index - 1

        else:
            min_elem_index = mid_elem_index + 1

    # If no strict match, return nearest bigger value
    nearest_value = array[min_elem_index] if min_elem_index < len(array) else array[-1]
    return (iterration_count, nearest_value)
