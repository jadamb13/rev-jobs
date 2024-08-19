class Job(object):
    def __init__(self):
        self._length = ''
        self._pay_per_minute = ''
        self._pay_total = ''
        self._quality = ''
        self._type = ''
        self._accent = ''
        self._time_due = ''
        self._subject = ''
        self._number_of_speakers = ''
        self._media_type = ''
        self._unclaims = ''
        self._age = ''

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length

    def get_pay_per_minute(self):
        return self._pay_per_minute

    def set_pay_per_minute(self, pay_per_minute):
        self._pay_per_minute = pay_per_minute

    def get_pay_total(self):
        return self._pay_total

    def set_pay_total(self, pay_total):
        self._pay_total = pay_total

    def get_quality(self):
        return self._quality

    def set_quality(self, quality):
        self._quality = quality

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def get_accent(self):
        return self._accent

    def set_accent(self, accent):
        self._accent = accent

    def get_time_due(self):
        return self._time_due

    def set_time_due(self, time_due):
        self._time_due = time_due

    def get_subject(self):
        return self._subject

    def set_subject(self, subject):
        self._subject = subject

    def get_number_of_speakers(self):
        return self._number_of_speakers

    def set_number_of_speakers(self, number_of_speakers):
        self._number_of_speakers = number_of_speakers

    def get_media_type(self):
        return self._media_type

    def set_media_type(self, media_type):
        self._media_type = media_type

    def get_unclaims(self):
        return self._unclaims

    def set_unclaims(self, unclaims):
        self._unclaims = unclaims

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age
