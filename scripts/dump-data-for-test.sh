#!/bin/sh

# Run this script after the following things are done:
# 1. Get into the backend/ directory [cd backend/]
# 2. Make sure you have virtual environment [pipenv --three] which is required once
# 2. Activate virtual environment using [pipenv shell]
# 3. Make sure to install all packages using [pip install -r requirements.txt]
# 4. Run [./manage.py makemigrations]
# 5. Run [./manage.py migrate]
# 6. Now run the script using [../scripts/dump-data-for-test.sh]

if [ -x "manage.py" ]; then
    ./manage.py dumpdata --exclude auth.permission \
                         --exclude contenttypes \
                         --exclude auth.group \
                         --exclude auth.user \
                         --exclude sessions.session \
                         --exclude admin.logentry --indent 2 > db.json
else
    echo "Read '`basename "$0"`' before executing it"
fi
