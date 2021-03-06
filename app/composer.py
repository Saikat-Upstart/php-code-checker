import os
from app.configuration import get_value
from app.helper import php, output_error


def initialization():
    checker_dir = get_value('checker-dir')

    if not os.path.isfile(checker_dir+'bin/composer'):
        download(checker_dir)
    if not os.path.isfile(checker_dir+'bin/phpcs'):
        composer('install')


def download(checker_dir):
    php_bin = get_value('php')
    if not os.path.exists(checker_dir+'bin'):
        os.makedirs(checker_dir+'bin')
    print('>>> Download composer')
    os.system('curl -sS https://getcomposer.org/installer | '+php_bin+' -- --install-dir='+checker_dir+'bin --filename=composer')


def update():
    composer('self-update')
    composer('update')


def project_installation():
    code = php('composer', 'install --optimize-autoloader')
    if code != 0:
        output_error('The composer install command for the project failed with the code '+str(code))


def composer(arguments):
    base_dir = os.getcwd()
    os.chdir(get_value('checker-dir'))

    php('composer', arguments)

    os.chdir(base_dir)
