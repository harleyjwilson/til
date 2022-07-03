# Clean Up Old Homebrew Install Files

When [Homebrew](https://brew.sh) installs formulas and casks it will keep the old versions around. Homebrew won't automatically delete it, you will have to do it yourself with the following command.

```bash
$ brew cleanup
```

This will delete those old files and report back how much space they were taking up.

If you use the Oh My Zsh framework with the brew plugin using the `bubc` command will run both `brew upgrade` and `brew cleanup`.
