#!/usr/bin/python
def deduplicate_list(list):
    deduplicated = []
    for i in list:
      if i not in deduplicated:
        deduplicated.append(i.rstrip())
    return deduplicated

def diff_list(first, second):
        second = set(second)
        return [item for item in first if item not in second]
