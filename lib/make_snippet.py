def make_snippet(string):
    words = string.split()
    string_ = " ".join(words[:5])
    if len(words) > 5:
        string_ += "..."

    return string_