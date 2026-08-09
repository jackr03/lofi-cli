import argparse
import shutil
import subprocess
import sys

from lofi.stations import DEFAULT_STATION, STATIONS


TITLE_ESCAPE_SEQUENCE = '\033]0;{}\007'
NOW_PLAYING_MESSAGE = 'Now playing {}...'
MISSING_DEPENDENCY_MESSAGE = '{} not found'

BASE_ARGS = [
	'mpv.com' if sys.platform == 'win32' else 'mpv',
	'--no-video',
	'--volume=70',
	'--msg-level=all=no,statusline=status',
	'--term-status-msg=${?pause==yes:(paused)}',
]


def verify_dependencies_installed():
	for tool in ('mpv', 'yt-dlp'):
		if not shutil.which(tool):
			print(MISSING_DEPENDENCY_MESSAGE.format('mpv'))
			sys.exit(1)


def parse_args():
	parser = argparse.ArgumentParser(
		prog='lofi',
		description='A minimal CLI for playing lofi from the terminal',
	)
	parser.add_argument(
		'station',
		nargs='?',
		default=DEFAULT_STATION,
		choices=STATIONS.keys(),
		help=f'which station to play (default: {DEFAULT_STATION})',
	)
	return parser.parse_args()


def main():
	args = parse_args()
	verify_dependencies_installed()
	station = STATIONS[args.station]

	print(TITLE_ESCAPE_SEQUENCE.format(station.title), end='')
	print(NOW_PLAYING_MESSAGE.format(station.title))

	try:
		sys.exit(subprocess.run(BASE_ARGS + [station.url]).returncode)
	except KeyboardInterrupt: # Swallow Ctrl-C
		pass


if __name__ == '__main__':
	main()
