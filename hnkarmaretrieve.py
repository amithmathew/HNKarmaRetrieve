# Python
#
# Returns my HNKarma for display on the Conky HUD
#
# Created 26 Oct 2010 - Amith P Mathew
#


from urllib import urlopen
import sys

profname = 'put_profile_name_here'
profpage = str(urlopen('http://news.ycombinator.com/user?id=' + profname).read())
KarmaLoc = profpage.find("karma:</td><td>")
if KarmaLoc == -1:
    print "Error retrieving HN Karma!"
    sys.exit(-1)
else:
    Karma =  profpage[KarmaLoc+15:KarmaLoc+18]
    print Karma