def morloc_split(delim, s):
    if delim == "":
        return list(s)
    return s.split(delim)

def morloc_lines(s):
    return s.split("\n")

def morloc_words(s):
    return s.split()

def morloc_chars(s):
    return list(s)

def morloc_join(delim, xs):
    return delim.join(xs)

def morloc_unlines(xs):
    return "\n".join(xs)

def morloc_unwords(xs):
    return " ".join(xs)

def morloc_contains(needle, haystack):
    return needle in haystack

def morloc_startsWith(prefix, s):
    return s.startswith(prefix)

def morloc_endsWith(suffix, s):
    return s.endswith(suffix)

def morloc_toUpper(s):
    return s.upper()

def morloc_toLower(s):
    return s.lower()

def morloc_trim(s):
    return s.strip()

def morloc_trimStart(s):
    return s.lstrip()

def morloc_trimEnd(s):
    return s.rstrip()

def morloc_replace(old, new, s):
    return s.replace(old, new, 1)

def morloc_replaceAll(old, new, s):
    return s.replace(old, new)

def morloc_padLeft(width, fill, s):
    if len(fill) == 0:
        return s
    pad_needed = width - len(s)
    if pad_needed <= 0:
        return s
    padding = (fill * ((pad_needed // len(fill)) + 1))[:pad_needed]
    return padding + s

def morloc_padRight(width, fill, s):
    if len(fill) == 0:
        return s
    pad_needed = width - len(s)
    if pad_needed <= 0:
        return s
    padding = (fill * ((pad_needed // len(fill)) + 1))[:pad_needed]
    return s + padding

def morloc_isBlank(s):
    return len(s.strip()) == 0
