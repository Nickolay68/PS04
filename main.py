import wikipediaapi
def print_paragraphs(page):
    paragraphs = page.text.split('\n\n')
    for i, paragraph in enumerate(paragraphs):
        print(f"Параграф {i + 1}:\n{paragraph}\n")
        if i < len(paragraphs) - 1:
            continue_reading = input("Введите 'n' для следующего параграфа или 'm' для меню: ")
            if continue_reading.lower() == 'm':
                break


def list_links(page):
    links = list(page.links.keys())
    for i, link in enumerate(links):
        print(f"{i + 1}. {link}")
    return links


def main():
    wiki_wiki = wikipediaapi.Wikipedia('ru')

    while True:
        query = input("Введите запрос для поиска на Википедии: ")

        page = wiki_wiki.page(query)
        if not page.exists():
            print("Страница не найдена. Попробуйте другой запрос.")
            continue

        print(f"Текущая статья: {page.title}")

        while True:
            action = input(
                "Выберите действие: \n1. Листать параграфы\n2. Перейти на связанную страницу\n3. Выйти из программы\nВведите номер действия: ")

            if action == '1':
                print_paragraphs(page)
            elif action == '2':
                print("Связанные страницы:")
                links = list_links(page)

                try:
                    link_choice = int(input("Введите номер связанной страницы, чтобы перейти на нее: ")) - 1
                    if 0 <= link_choice < len(links):
                        page = wiki_wiki.page(links[link_choice])
                        print(f"Текущая статья: {page.title}")
                    else:
                        print("Неверный номер. Попробуйте снова.")
                except ValueError:
                    print("Пожалуйста, введите допустимый номер.")
            elif action == '3':
                print("Выход из программы.")
                return
            else:
                print("Неверный ввод. Пожалуйста, выберите действие 1, 2 или 3.")

    if __name__ == '__main__':
      main()


