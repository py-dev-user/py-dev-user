from datetime import datetime
from os.path import splitext


def get_timestamp_path(instance, filename):
    return '{datetime_mark}{extension}'.format(
        datetime_mark=datetime.now().strftime('%Y%m%d%H%M%S'),
        extension=splitext(filename)[1]
    )
