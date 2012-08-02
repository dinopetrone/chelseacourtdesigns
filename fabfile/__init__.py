
@task
def run():
    local('python manage.py runserver 8080')


@task
def reset():
	local('rm -f sqlite.db')
	local('yes no | python manage.py syncdb')
	local('python manage.py loaddata currencies')
	local('python manage.py createsuperuser --username=user --email=user@host.com')


