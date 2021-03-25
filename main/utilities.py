from datetime import datetime
from os.path import splitext

from py_dev_user.settings import MEDIA_DIR


def get_timestamp_path(instance, filename):
    return '{media_dir}/{datetime_mark}{extension}'.format(
        media_dir=MEDIA_DIR,
        datetime_mark=datetime.now().strftime('%Y%m%d%H%M%S'),
        extension=splitext(filename)[1]
    )
