# Poseidon
A fast, minimal and lightweight browser

### Requirements

* Requires [WebKit](https://webkitgtk.org/) 2.12.3 or higher

### Dependencies

* Ubuntu/Mint

`# apt-get install gir1.2-evince-3.0 gir1.2-webkit2-4.0 python3-decorator python3-openssl evince-browser-plugin (external)`

If your WebKit version is too old, upgrade it from [here](https://launchpad.net/~webkit-team/+archive/ubuntu/ppa):

`$ sudo add-apt-repository ppa:webkit-team/ppa`

* Fedora

`# dnf install python3-pyOpenSSL.noarch`

### Shortcuts

In the main entry, type:

* `about:plugins` to get a list of loaded plugins
* `about:bookmarks` to open bookmarks tab
* `about:history` to open history tab
* `about:cookies` to open cookies manager tab

### Settings

Edit settings directly from `include/settings.py`. `AdKiller`, `Javascript` and other plugins like `Flash` are activable/deactivable with a switch in the browser menu.

### Languages

Available languages:

* English (`en_US`)
* Italian (`it_IT`)
* French (`fr_FR`)

### Themes

Any image can become a theme, right click on a image and click `Apply as theme`.

### Evince

If [evince](https://wiki.gnome.org/Apps/Evince) and `evince-browser-plugin` are installed, Poseidon will read PDF's directly in the WebKit2.WebView.

Note: In [Arch Linux](https://www.archlinux.org/) you just need to install `evince` as it's plugin comes together with the package.

### Defcon Mode (aka. Incognito)

If set `True` in `include/settings.py`, Poseidon will disable cache, ignore history and cookies independently from their policies.

### Tor

To use Poseidon with Tor, you need [torsocks](https://github.com/dgoulet/torsocks) or alternatively [proxychains](https://github.com/haad/proxychains).

Once Tor is started, through [arm](https://www.torproject.org/projects/arm.html.en) or the discontinued [vidalia](https://en.wikipedia.org/wiki/Vidalia_(software)), you can launch Poseidon in these ways:

* `$ torsocks(or proxychains) ./poseidon` (default mode)
* `$ torsocks(or proxychains) ./poseidon -i` (defcon mode)

### Code snippets, examples, icons, inspirations, peace to:

* https://gist.github.com/kklimonda/890640 (pybrowser.py)
* https://github.com/kvesteri/validators (validators)
* https://github.com/aperezdc/webkit2gtk-python-webextension-example (WebKit2GTK+ Python WebExtension loader)
* https://www.gnome-look.org/p/1012545/ (Faenza)
* http://www.gnome.org (Adwaita)

### Donations

If you enjoy [Poseidon](https://github.com/sidus-dev/poseidon)
consider to buy me a beer!

`BTC: 1Ki95pCN6drymSUY7sS45MLVDkfiKTC8t9`