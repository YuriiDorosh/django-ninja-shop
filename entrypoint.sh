# #!/bin/bash

# wait_for_port() {
#     local host=${POSTGRES_HOST}
#     local port=${POSTGRES_PORT}
#     local timeout=10
#     local start_time=$(date +%s)

#     local nc_command="nc"
#     type $nc_command >/dev/null 2>&1 || nc_command="ncat"

#     while ! $nc_command -z "$host" "$port" >/dev/null 2>&1; do
#         sleep 1
#         local current_time=$(date +%s)
#         local elapsed_time=$((current_time - start_time))
#         echo "trying to connecto to pg via $host:$port"

#         if [ $elapsed_time -ge $timeout ]; then
#             echo "Unable to connect to pg"
#             exit 1
#         fi
#     done
# }

# wait_for_port "postgres" 5430

python manage.py runserver 0.0.0.0:8000