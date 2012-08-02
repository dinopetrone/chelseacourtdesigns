from fabric.api import local, task
from fabric.operations import prompt
from fabric.contrib.console import confirm

@task
def view():
    view_name = prompt("Enter View Name: \nEX: About \nHint: Already auto suffixed with 'View':").lower()
    local("sed -e 's/{view_name}/"+view_name.title()+"/g' fabfile/templates/view.txt > www/views/"+view_name+'.py')
    
    if confirm('--------------\nCreate a Service?:'):
        service_name = prompt("--------------\nEnter Service Name: \nEX: About \nHint:Already auto suffixed with 'Service' \nHint:hit enter to use view name:").lower()
        if service_name == '':
            service_name = view_name
        local("sed -e 's/{service_name}/"+service_name.title()+"/g' -e 's/{lower_service_name}/"+service_name+"/g' fabfile/templates/service.txt > www/services/"+service_name+".py")

    if confirm('--------------\nCreate HTML stub?:'):
        html_name = prompt("--------------\nHTML File name: \nHit enter to leave same as view_name").lower()
        if html_name == '':
            html_name = view_name
        local('cp fabfile/templates/html.txt www/templates/'+html_name+'.html')
        local("sed 's/{html}/"+html_name+"/g' www/views/"+view_name+".py > www/views/"+view_name+".py.tmp")
        local("mv www/views/"+view_name+".py.tmp www/views/"+view_name+".py")    
        pass
    
    
    
    
