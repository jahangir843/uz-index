# Uz Index IPTV

This repository contains a professional M3U-based IPTV dashboard with auto-refresh support.

## Features
- Clean, modern channel viewer
- Grouped categories like Bangla, News, Sports, Movies, etc.
- Search and category filter
- Auto-update every 10 minutes
- Manual refresh button
- Works well for GitHub Pages or simple static hosting

## Files
- `index.html` — main dashboard page
- `styles.css` — modern styling
- `app.js` — M3U parsing and auto-refresh logic
- `playlist.m3u` — source IPTV list

## Usage
1. Open `index.html` in a browser, or publish the repository via GitHub Pages.
2. The app automatically loads the playlist from the GitHub raw URL.
3. It refreshes automatically every 10 minutes and can be refreshed manually at any time.

## Auto-update source
The app fetches:
`https://raw.githubusercontent.com/jahangir843/uz-index/uzalam/playlist.m3u`

If you want, you can also replace this with your own raw M3U URL later.
