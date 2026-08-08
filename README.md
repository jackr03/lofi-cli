# lofi-cli

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

A minimal CLI for playing lofi from the terminal.

Uses [`mpv`](https://mpv.io/) for playback and [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) to resolve the stream.

## Install

Requires [`mpv`](https://mpv.io/) and [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) on your PATH. Install via your platform's package manager (`brew`, `winget`, etc.).

Then install the CLI with `pip`:

```bash
pip install -e .
```

## Usage
Type `lofi` in your terminal to start. Playback blocks the terminal instance - press `q` or `Cmd+C`) to quit.
