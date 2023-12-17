import phonebook_processor as pp

phone_pattern = r"(\+7|8)?[\s-]?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})\s?\(?(доб\.?)?\s?(\d+)?\)?"
phone_substitute = r"+7(\2)\3-\4-\5 \6\7"

if __name__ == "__main__":
