import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


def compress_images(tree):
    children = get_children(tree)
    new_meta = copy.deepcopy(get_meta(tree))
    new_children = []
    for child in children:
        if is_file(child) and get_name(child).endswith('.jpg'):
            meta = copy.deepcopy(get_meta(child))
            meta['size'] = meta['size'] // 2
            new_children.append(mkfile(get_name(child), meta))
        else:
            new_children.append(child)
    return mkdir(get_name(tree), new_children, new_meta)
