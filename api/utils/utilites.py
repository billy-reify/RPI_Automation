import uuid
from datetime import datetime



class Utilities(object):
    @staticmethod
    def get_uuid():
        return uuid.uuid4()

    @staticmethod
    def get_collection_start_time():
        """
        This method generates a iso 8601 formatted utc timestamp
        for use in RPI Event Reporting.
        """
        my_date = datetime.utcnow().isoformat(timespec='milliseconds') + 'Z'
        return my_date

    @staticmethod
    def is_publishedTime_greater_than_collectionTime(publishedTime,collectionTime):
        """
        This method takes parameters and removes utc related characters "T" and "Z"
        in order to convert them to a format that can be compared to determine the
        difference in time between them.
        :param publishedTime:
        :param collectionTime:
        :return: boolean value whether the publishedTime is greater than the collectionTime parameters
        """
        collection_start_time = collectionTime.replace("T"," ").replace("Z","")
        published_event_time = publishedTime.replace("T"," ").replace("Z","")
        delta = abs(datetime.strptime(published_event_time, '%Y-%m-%d %H:%M:%S.%f') >
                    datetime.strptime(collection_start_time, '%Y-%m-%d %H:%M:%S.%f'))
        return bool(delta)


