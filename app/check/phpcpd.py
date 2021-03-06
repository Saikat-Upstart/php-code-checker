from app.configuration import get_value
from app.helper import output_start, php, get_dirs


def execute():
    output_start('phpcpd')

    dirs = get_dirs()
    check_dir = get_value('check-dir')
    exclude_dirs = get_value('exclude-dirs')
    excludes = ''

    for exclude in exclude_dirs:
        excludes = excludes+' --exclude '+exclude

    print('>>> Excludes: '+excludes)

    php('phpcpd', excludes+' --log-pmd '+check_dir+'pmd-cpd.xml '+dirs['scan'])
