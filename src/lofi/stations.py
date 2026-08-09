from typing import NamedTuple


class Station(NamedTuple):
	url: str
	title: str


DEFAULT_STATION = 'lofi'
STATIONS: dict[str, Station] = {
	'lofi': Station('https://www.youtube.com/watch?v=X4VbdwhkE10', 'lofi hip hop radio 📚 beats to relax/study to'),
	'jazz': Station('https://www.youtube.com/watch?v=E2vONfzoyRI', 'jazz lofi radio 🎷 beats to chill/study to'),
	'synthwave': Station('https://www.youtube.com/watch?v=4xDzrJKXOOY', 'synthwave radio 🌌 beats to chill/game to'),
}
