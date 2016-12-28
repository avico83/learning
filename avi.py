class logtofile():

    def __init__( self , username):

        self.username = username

        print "my username is %s" % self.username

    def __write__( self, username ):
        print "inside def my username is %s" % username
        print "self my username is %s" % self.username

a = logtofile("avi")
a.__write__("cohen")
print a.username




