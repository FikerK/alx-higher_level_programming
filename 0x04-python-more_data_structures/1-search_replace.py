#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_r(n):
        return (n if n != search else replace)
    return list(map(s_r, my_list))
