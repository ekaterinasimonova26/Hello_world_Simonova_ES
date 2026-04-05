#!/bin/bash

check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "Предупреждение: Скрипт не запущен от имени суперпользователя!"
        exit 1
    else
        echo "Скрипт запущен от имени суперпользователя."
    fi
}

check_root
