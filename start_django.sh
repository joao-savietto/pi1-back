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

wait_for_db $MYSQL_HOST $MYSQL_PORT
while getopts ":h:" opt; do
  case $opt in
    h) COMMAND="$OPTARG";;
    \?) echo "Invalid option: -$OPTARG"; exit 1;;
  esac
done

shift $(($OPTIND - 1))

if [ -z "$COMMAND" ]; then
  COMMAND="gunicorn pi1back.wsgi:application --bind 0.0.0.0:8000"
fi

python manage.py migrate
exec ${COMMAND}