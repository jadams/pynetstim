import imaplib
from pns_client import utils
from pns_client import timer

def get_mail(hostname, port, username, password)
	M = imaplib.IMAP4(hostname, port)
	M.login(username, password)
	M.select()
	typ, data = M.search(None, 'ALL')
	for num in data[0].split():
		typ, data = M.fetch(num, '(RFC822)')
		print 'Message %s\n%s\n' % (num, data[0][1])
	M.close()
	M.logout()