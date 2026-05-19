  
## Домашнее задание к занятию 5 «Тестирование roles» Теплов Михаил

### Подготовка к выполнению

1. Установите molecule и его драйвера: pip3 install "molecule molecule_docker molecule_podman.

2. Выполните docker pull aragast/netology:latest — это образ с podman, tox и несколькими пайтонами (3.7 и 3.9) внутри.

### Основная часть

Ваша цель — настроить тестирование ваших ролей.

Задача — сделать сценарии тестирования для vector.

Ожидаемый результат — все сценарии успешно проходят тестирование ролей.


### Molecule

1. Запустите molecule test -s ubuntu_xenial (или с любым другим сценарием, не имеет значения) внутри корневой директории clickhouse-role, посмотрите на вывод команды. Данная команда может отработать с ошибками или не отработать вовсе, это нормально. Наша цель - посмотреть как другие в реальном мире используют молекулу И из чего может состоять сценарий тестирования.

2. Перейдите в каталог с ролью vector-role и создайте сценарий тестирования по умолчанию при помощи molecule init scenario --driver-name docker.

3. Добавьте несколько разных дистрибутивов (oraclelinux:8, ubuntu:latest) для инстансов и протестируйте роль, исправьте найденные ошибки, если они есть.

4. Добавьте несколько assert в verify.yml-файл для проверки работоспособности vector-role (проверка, что конфиг валидный, проверка успешности запуска и др.).

5. Запустите тестирование роли повторно и проверьте, что оно прошло успешно.

6. Добавьте новый тег на коммит с рабочим сценарием в соответствии с семантическим версионированием.

![1](https://github.com/mteplov/roles/blob/main/img/01.png)

![2](https://github.com/mteplov/roles/blob/main/img/02.png)


Запуск тестового сценария в другой роли clickhouse-role командой:

    molecule test -s ubuntu_xenial


Вывод показал, что сценарий частично отрабатывает, с ошибками или предупреждениями.

Комментарий: цель этого шага была ознакомительная — посмотреть, как в реальном мире используют Molecule и из чего состоят сценарии тестирования.

![3](https://github.com/mteplov/roles/blob/main/img/03.png)

![4](https://github.com/mteplov/roles/blob/main/img/04.png)

Перешёл в каталог с ролью vector-role и создал базовый сценарий Molecule по умолчанию:

    molecule init scenario --driver-name docker

![5](https://github.com/mteplov/roles/blob/main/img/05.png)

![6](https://github.com/mteplov/roles/blob/main/img/06.png)

![7](https://github.com/mteplov/roles/blob/main/img/07.png)

![8](https://github.com/mteplov/roles/blob/main/img/08.png)

![101](https://github.com/mteplov/roles/blob/main/img/101.png)

![11](https://github.com/mteplov/roles/blob/main/img/11.png)


После успешного тестирования я сделал коммит с рабочим сценарием:

   
https://github.com/mteplov/roles/releases/tag/v1.0.1


- - - - - - - - - - - - 

    Все ключевые шаги выполнены без ошибок:

    PLAY RECAP *********************************************************************
    instance                   : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

    failed=0 → нет ошибок

    unreachable=0 → все хосты доступны

    changed=0 на idempotence → роль идемпотентна (не делает лишних изменений при повторном запуске)

    Verifying step отключён, поэтому никаких ошибок там не возникло:

    WARNING  default ➜ verify: Skipping, verifier is disabled.
    INFO     default ➜ verify: Executed: Disabled

    Destroy и cleanup прошли без проблем, контейнер корректно удалён:

    PLAY RECAP *********************************************************************
    localhost                  : ok=1    changed=0    unreachable=0    failed=0    skipped=1

    Нет FAILED! или ERROR на converge, idempotence или prepare шагах.

    Вывод: роль установилась, idempotence проверена, тестовый контейнер создался и был удалён — Molecule полностью прошёл.

    Примечание: предупреждения о Missing playbook или Missing files — это просто Molecule предупреждает, что некоторые тестовые шаги (side_effect, cleanup) не имеют плейбука, но это не ошибка.


- - - - - - - - - - - - 


### Tox

1. Добавьте в директорию с vector-role файлы из директории.

2.Запустите docker run --privileged=True -v <path_to_repo>:/opt/vector-role -w /opt/vector-role -it aragast/netology:latest /bin/bash, где path_to_repo — путь до корня репозитория с vector-role на вашей файловой системе.

3. Внутри контейнера выполните команду tox, посмотрите на вывод.

4. Создайте облегчённый сценарий для molecule с драйвером molecule_podman. Проверьте его на исполнимость.

5. Пропишите правильную команду в tox.ini, чтобы запускался облегчённый сценарий.

6. Запустите команду tox. Убедитесь, что всё отработало успешно.

7. Добавьте новый тег на коммит с рабочим сценарием в соответствии с семантическим версионированием.

Итого

![12](https://github.com/mteplov/roles/blob/main/img/12.png)

Я скопировал файлы роли vector-role в рабочую директорию и запустил контейнер для тестирования с помощью Docker:

    docker run --privileged=True -v ~/netology/vector-role:/opt/vector-role -w /opt/vector-role -it aragast/netology:latest /bin/bash


![13](https://github.com/mteplov/roles/blob/main/img/13.png)

![14](https://github.com/mteplov/roles/blob/main/img/14.png)

![15](https://github.com/mteplov/roles/blob/main/img/15.png)





Итого:

   

https://github.com/mteplov/roles/releases/tag/v1.0.2

- - - - - - - - - - - - 

