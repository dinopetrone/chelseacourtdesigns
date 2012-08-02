class BaseModel(object):
    pass


class BaseModelDict(dict):

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            # to conform with __getattr__ spec
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        del self[key]


class BaseViewModel(BaseModelDict):

    def __new__(cls):
        instance = super(BaseViewModel, cls).__new__(cls)
        BaseViewModel.__init__(instance)
        return instance
    
    def __init__(self):
        super(BaseViewModel, self).__init__(self)
        self.title = None
        self.tweets = []
        self.css = []
        self.javascripts = []
        self.body_class = 'internal'
