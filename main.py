import shutil
import subprocess
import sys

LOFI_RADIO_URL = 'https://www.youtube.com/watch?v=X4VbdwhkE10'
LOFI_RADIO_NAME = 'lofi hip hop radio 📚 beats to relax/study to'
TITLE_ESCAPE_SEQUENCE = f'\033]0;{LOFI_RADIO_NAME}\007'
MISSING_TOOL_MESSAGE = '{} not found'

arguments = [
	'mpv.com' if sys.platform == 'win32' else 'mpv',
	'--no-video',
	'--volume=70',
	'--msg-level=all=error',
	LOFI_RADIO_URL
]

def verify_mpv_installed():
	if not shutil.which('mpv'):
		print(MISSING_TOOL_MESSAGE.format('mpv'))
		sys.exit()

	if not shutil.which('yt-dlp'):
		print(MISSING_TOOL_MESSAGE.format('yt-dlp'))
		sys.exit()

def main():
	verify_mpv_installed()

	print(TITLE_ESCAPE_SEQUENCE, end='')
	print(f'Now playing {LOFI_RADIO_NAME}...')
	try:
		subprocess.run(arguments)
	except KeyboardInterrupt: # Swallow CMD+C
		pass
	except Exception as e: # Print any other error
		print(e)

if __name__ == '__main__':
	main()