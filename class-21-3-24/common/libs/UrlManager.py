class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        # ver = "%s" % (11111)
        ver = "%s" % 1.0
        path = "/static" + path + "?ver=" + ver
        return UrlManager.buildUrl(path)