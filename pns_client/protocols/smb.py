import subprocess
import sys
import shutil
import os

def connect_to_share(path_to_share):
	command = 'net use * ' + path_to_share
	print command
	try:
		output = subprocess.check_output(command)
	except:
		print output
		sys.exit(1)

	smb_drive = output.split()[1]+'\\'

	for root, dirs, files in os.walk(smb_drive):
		print("{0} has {1} files".format(root, len(files)))
		break




def main():
	connect_to_share('\\\\localhost\\c$')


if __name__ == '__main__':
	main()