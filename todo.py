def show_todos():
    print("TODO一覧")
    print("状態と優先度")

    print(f"すべてのTODO({len(todos)}件)")
    for todo in todos:
        status = "[完了] " if todo["completed"] else ""
        print(f'{status}{todo["title"]} [{todo["priority"]}]')

