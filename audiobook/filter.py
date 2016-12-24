from typing import List


def get_filter(filter_list: List[str]):
    filters = []
    for filter_item in filter_list:
        key, val = filter_item.split(':')
        filters.append((key, val,))

    def filter_item(item):
        if not filters:
            return item
        for filter_item in filters:
            if filter_item[0] in item:
                # key exists
                if type(item[filter_item[0]]) is list:
                    if filter_item[1] in item[filter_item[0]]:
                        return item
                elif item[filter_item[0]] == filter_item[1]:
                    return item
        return None
    return filter_item
