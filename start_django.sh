#!/bin/bash

set -e

wait_for_db() {
  local db_host="$1"
  local db_port="$2"
  local max_tries=10
  local try=0

  until mysqladmin ping -h "$db_host" -P "$db_port" --silent; do
    try=$((try+1))
    if [ $try -gt $max_tries ]; then
      echo "Max tries reached, exiting"
      exit 1
    fi
    echo "Waiting for database to be ready..."
    sleep 5
  done
}

# Wait for the MySQL server to be ready
wait_for_db $MYSQL_HOST $MYSQL_PORT
python manage.py migrate

exec "$@"