def get_last_word_length(s: str) -> int:
    result = s.rstrip()

    return len(result.split(" ")[-1])


if __name__ == "__main__":
    print(get_last_word_length("hello world  "))
    print(get_last_word_length("hello world"))
    print(get_last_word_length("  hello world  "))