#!/bin/bash

# MySQL root credentials
MYSQL_USER="root"
MYSQL_PASSWORD="yourpassword"

# Users to check
USERS=("user_0d_1" "user_0d_2")

# Function to get privileges for a user
get_user_privileges() {
    local user=$1
    echo "Privileges for $user:"
    mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW GRANTS FOR '$user'@'localhost';" 2>/dev/null
    if [ $? -ne 0 ]; then
        echo "Error retrieving privileges for $user"
    fi
    echo
}

# Main script
for user in "${USERS[@]}"; do
    get_user_privileges "$user"
done

