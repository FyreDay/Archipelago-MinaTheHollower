
def range_incl(a: int, b: int) -> range:
    return range(a, b+1)

#Images for a single map Id
mapping_single: dict[int, int] = {
    317: 1,    # => "route1"
}

#Images for multiple map id
mapping_range: dict[range, int] = {
    range_incl(356, 364): 0,  # BADGE GATES, overworld
}

def should_change(map_id: int) -> bool:
    if map_id in mapping_single:
        return True
    for rang in mapping_range:
        if map_id in rang:
            return True
    return False

def map_page_index(data: int) -> int:
    if data in mapping_single:
        return mapping_single[data]
    for rang in mapping_range:
        if data in rang:
            return mapping_range[rang]
    return 0