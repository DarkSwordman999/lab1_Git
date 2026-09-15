# Лабораторная работа №1 — Git

**Фураев Владислав Викторович, группа 221341, вариант 10.**

## Цель работы

Освоить систему контроля версий Git: создание репозитория, работу с ветками, создание коммитов, слияние изменений и использование удалённого репозитория GitHub.

## Проект

Учебный Python-проект **«Todo List»**.

Возможности:
- добавление задач;
- просмотр задач;
- выполнение задач;
- удаление задач;
- редактирование задач.

## Запуск

```bash
python todo.py
```

## Использованный сторонний репозиторий

```text
https://github.com/SharpRhyme/todo-cli
```

Репозиторий был клонирован для изучения структуры проекта.

## Собственный GitHub-репозиторий

```text
https://github.com/DarkSwordman999/lab1_Git
```

## Ветки проекта

| Ветка | Назначение |
|---|---|
| main | Основная версия проекта |
| develop | Ветка разработки |
| feature/delete-task | Добавление удаления задач |
| feature/edit-task | Добавление редактирования задач |

## История коммитов

```text
feat: add basic todo application
feat: add task deletion
merge: integrate task deletion
feat: add task editing
merge: integrate task editing
docs: add project readme
chore: add gitignore
```

## Слияние веток

Использовалась команда:

```bash
git merge --no-ff
```

Слияния:

```text
feature/delete-task -> develop
feature/edit-task -> develop
```

## Проверка Git

```bash
git log --oneline --graph --all
```

```text
* 07bd416 chore: add gitignore
* 79fe3c9 docs: add project readme
*   ed40398 merge: integrate task editing
|\
| * d5538fb feat: add task editing
|/
*   2525db9 merge: integrate task deletion
|\
| * b6d913e feat: add task deletion
|/
* 5119548 feat: add basic todo application
```

## Проверка состояния

```bash
git status
```

Результат:

```text
nothing to commit, working tree clean
```

## Технологии

- Python 3
- Git
- GitHub
- PowerShell
# Лабораторная работа №1 — Git

**Фураев Владислав Викторович, группа 221341, вариант 10.**

## Цель работы

Освоить систему контроля версий Git: создание репозитория, работу с ветками, создание коммитов, слияние изменений и использование удалённого репозитория GitHub.

## Проект

Учебный Python-проект **«Todo List»**.

Возможности:
- добавление задач;
- просмотр задач;
- выполнение задач;
- удаление задач;
- редактирование задач.

## Запуск

```bash
python todo.py
```

## Использованный сторонний репозиторий

```text
https://github.com/SharpRhyme/todo-cli
```

Репозиторий был клонирован для изучения структуры проекта.

## Собственный GitHub-репозиторий

```text
https://github.com/DarkSwordman999/lab1_Git
```

## Ветки проекта

| Ветка | Назначение |
|---|---|
| main | Основная версия проекта |
| develop | Ветка разработки |
| feature/delete-task | Добавление удаления задач |
| feature/edit-task | Добавление редактирования задач |

## История коммитов

```text
feat: add basic todo application
feat: add task deletion
merge: integrate task deletion
feat: add task editing
merge: integrate task editing
docs: add project readme
chore: add gitignore
```

## Слияние веток

Использовалась команда:

```bash
git merge --no-ff
```

Слияния:

```text
feature/delete-task -> develop
feature/edit-task -> develop
```

## Проверка Git

```bash
git log --oneline --graph --all
```

```text
* 07bd416 chore: add gitignore
* 79fe3c9 docs: add project readme
*   ed40398 merge: integrate task editing
|\
| * d5538fb feat: add task editing
|/
*   2525db9 merge: integrate task deletion
|\
| * b6d913e feat: add task deletion
|/
* 5119548 feat: add basic todo application
```

## Проверка состояния

```bash
git status
```

Результат:

```text
nothing to commit, working tree clean
```

## Технологии

- Python 3
- Git
- GitHub
- PowerShell
