from django.db.models import ObjectDoesNotExist

from commons.models import Variable

class VariablesDatabase(object):
    
    database = [
        {'keyword': 'user_profile_key_length', 'value_int': 3},
        {'keyword': 'cpu_worker_key_length', 'value_int': 5},
    ]

    def __init__(self):
        super(VariablesDatabase, self).__init__()
        return

    def update_database(self):
        for record in self.database:
            try:
                v = Variable.objects.get(keyword=record['keyword'])
            except ObjectDoesNotExist as e:
                v = Variable()
                v.keyword = record['keyword']
            
            keys = ['value_int', 'value_string', 'value_boolean']
            for key in keys:
                if key in record.keys():
                    if v.__getattribute__(key) is None:
                        v.__setattr__(key, record[key])
            v.save()
        return

