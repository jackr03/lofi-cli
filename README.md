# lofi-cli

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

A minimal CLI for playing lofi from the terminal.

Uses [`mpv`](https://mpv.io/) for playback and [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) to resolve the stream.

## Install

Requires [`mpv`](https://mpv.io/) and [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) on your PATH. Install via your platform's package manager (`brew`, `winget`, etc.).

Then install the CLI with `pip`:

```bash
pip install .
```

## Usage

Type `lofi` in your terminal to start:

```bash
lofi
```

Or pass a station name to play a different stream:

```bash
lofi jazz
lofi synthwave
```

Available stations: `lofi` (default), `jazz`, `synthwave`.

While playing: `9`/`0` adjust volume, `m` mutes, `p` or `space` pauses, `q` quits.
