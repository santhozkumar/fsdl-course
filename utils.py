class packageVersion:
  ''' Find the version of the Package passed as parameter'''
    def __call__(self, *args):
        for arg in args:
            print(arg.__version__)

ver = packageVersion()
