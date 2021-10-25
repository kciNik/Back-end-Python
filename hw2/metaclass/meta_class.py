class MyMeta(type):

    def __call__(cls, *args, **kwargs):
        create = super().__call__(*args, **kwargs)
        custom_dct = {}
        for key, value in create.__dict__.items():
            if not (key.startswith('__') and key.endswith('__')):
                custom_dct['custom_' + key] = value
            else:
                custom_dct[key] = value
        create.__dict__ = custom_dct
        return create

    def __new__(cls, name, bases, dct):
        custom_dct = {}
        for key, val in dct.items():
            if not (key.startswith('__') and key.endswith('__')):
                custom_dct['custom_' + key] = val
            else:
                custom_dct[key] = val
        return super().__new__(cls, name, bases, custom_dct)
