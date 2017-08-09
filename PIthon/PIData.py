''' PIData
    Storage containers for PI data
'''

import datetime
from pandas import Series
import pytz
import semver

class PISeries(Series):
    'An extension to pandas.Series which always uses the timestamps as index and PI tag as name'

    version = semver.format_version(0, 1, 0)

    def __init__(self, tag, timestamp, value, uom = None, *args, **kwargs):
        Series.__init__(self,
                        data = value,
                        index = timestamp,
                        name = tag,
                        *args, **kwargs)
        self.tag = tag
        self.uom = uom

    @staticmethod
    def timestamp_to_index(timestamp):
        local_tz = pytz.timezone('Europe/Amsterdam')
        return datetime.datetime(
            timestamp.Year,
            timestamp.Month,
            timestamp.Day,
            timestamp.Hour,
            timestamp.Minute,
            timestamp.Second,
            timestamp.Millisecond*1000
            ).replace(tzinfo = pytz.utc).astimezone(local_tz)
