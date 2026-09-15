\# Лабораторная работа №1 — Git



\*\*Фураев Владислав Викторович, группа 221341, вариант 10.\*\*



\## Цель работы



Освоить работу с системой контроля версий Git: создание репозитория, работу с ветками, создание коммитов, слияние изменений и подготовку проекта к публикации.



\## Проект



Учебный Python-проект «Todo List».



Программа представляет собой консольный список задач и поддерживает:



\- добавление задач;

\- просмотр списка задач;

\- отметку задач как выполненных;

\- удаление задач;

\- редактирование задач.



\## Запуск проекта



```bash

python todo.py

```



\## Использованный сторонний репозиторий



В качестве основы был выбран открытый GitHub-репозиторий:



```text

https://github.com/SharpRhyme/todo-cli

```



Репозиторий был клонирован для изучения структуры проекта и истории Git. Собственный проект разработан отдельно.



\## Разработка проекта



В процессе выполнения лабораторной работы были созданы следующие ветки:



\- `main` — основная ветка проекта;

\- `develop` — ветка разработки;

\- `feature/delete-task` — разработка функции удаления задач;

\- `feature/edit-task` — разработка функции редактирования задач.



\## История коммитов



Основные коммиты проекта:



```text

feat: add basic todo application

feat: add task deletion

merge: integrate task deletion

feat: add task editing

merge: integrate task editing

```



Сообщения функциональных коммитов выполнены с использованием Conventional Commits.



\## Слияние веток



Для объединения функциональных веток использовалось слияние без fast-forward:



```bash

git merge --no-ff

```



Были выполнены слияния:



```text

feature/delete-task → develop

feature/edit-task → develop

```



\## Проверка истории Git



Для просмотра структуры веток использовалась команда:



```bash

git log --oneline --graph --all

```



Текущая история разработки:



```text

\*   ed40398 (HEAD -> develop) merge: integrate task editing

|| \* d5538fb (feature/edit-task) feat: add task editing

|/

\*   2525db9 merge: integrate task deletion

|| \* b6d913e (feature/delete-task) feat: add task deletion

|/

\* 5119548 (main) feat: add basic todo application

```



\## Проверка состояния проекта



Для проверки отсутствия незакоммиченных изменений использовалась команда:



```bash

git status

```



Результат:



```text

On branch develop

nothing to commit, working tree clean

```



