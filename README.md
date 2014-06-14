**Examples (reply to discussion thread if you have one):**

*   [http://status.thechunk.net/](http://status.thechunk.net/)
*   [http://status.freecraft.eu/](http://status.freecraft.eu/)
*   [http://endercraftbuild.net/status](http://endercraftbuild.net/status)
*   [http://www.minotopia.me/status/](http://www.minotopia.me/status/)
*   [http://status.mycliff.net/](http://status.mycliff.net/)
*   [http://status.mc-sn.us/](http://status.mc-sn.us/)

**Official Thread:** [http://www.spigotmc.org/resources/mc-status-viewer.518/](http://www.spigotmc.org/resources/mc-status-viewer.518/)

**Installation:**

*   `git clone [https://github.com/vemacs/mc-status-viewer.git](https://github.com/vemacs/mc-status-viewer.git)` (I prefer in `/srv`)
*   Edit `index.html` to have the title you want
*   Edit `app/config.yml` to set up your categories and servers, see `[config.example.yml](https://github.com/vemacs/mc-status-viewer/blob/master/app/config.example.yml)`
*   `pip install bottle pyyaml`, depending on your distro, you may need to install `python-pip` and `python-dev` first
*   `cd <where you cloned>/app; python app.py`
*   You can test it by changing `app/app.py `to bind to `0.0.0.0 `and then connecting to `<ip>:8080`, `config.yml` is not accessible to the public, so your backends will stay hidden
*   Run it in a `tmux `or `screen` session
*   Set up a reverse proxy, here&#039;s a [sample nginx config](http://paste.ubuntu.com/7301975/), [Apache instructions](http://paste.ubuntu.com/7401472/)
*   `git pull` to update if there are any updates
*   You can **change the width** by editing `override.css` in the` .btn` class if you have longer server names

Post feedback or suggestions here! Keep in mind that I'm a noob at Python and Javascript (I literally learned JS today), so any code quality feedback would be awesome.

Here's the CPU/mem usage you';ll be looking at (pinging way too many servers, running for an hour):

![](http://i.imgur.com/scyRmnM.png)

It's not 100% accurate due to the nature of server list ping, but it works well enough (99.99999% accurate). If you're having issues, ask your host if this is triggering their anti-DDoS mechanism. Delaying the pings does not seem to help in this situation, so your best bet may be to ask your host, or host it on a box that can ping. Updates are every 5 seconds on the server, and then 3 seconds to pull on the client. Obviously, you should allow the box you're putting this on through your backend firewall.

Technically, you can host the frontend anywhere, just that origin policy complicates things.

If Ctrl+C isn't stopping it, try Ctrl+Z. A restart needs to be issued for config changes to apply.

**IF YOU ARE USING WINDOWS TO RUN A MINECRAFT SERVER, YOU ARE DOING IT WRONG. QUIT ASKING HOW TO RUN THIS ON WINDOWS. INSTRUCTIONS SHOULD BE VERY SIMILAR, BUT NO GUARANTEES THAT THIS WILL WORK.**
