# github_backup_user_repos
Clone and pull all repositories of one or more user for backup.

Setup
=====
```
sudo apt-get install git python
```
or
```
sudo apt-get install git python3
```
and
```
git clone https://github.com/Oros42/github_backup_user_repos.git
```

Run
===
```
cd github_backup_user_repos
python github_backup_user_repos.py <username> [<username2> <username3>...]
```
Examples :
```
$ python github_backup_user_repos.py Oros42
20 repositories from Oros42:
repo 1/20	: clone https://github.com/Oros42/tiny_DnDUp.git in ./repositories/Oros42/tiny_DnDUp
Clonage dans './repositories/Oros42/tiny_DnDUp'...
remote: Counting objects: 53, done.
remote: Total 53 (delta 0), reused 0 (delta 0), pack-reused 53
Dépaquetage des objets: 100% (53/53), fait.
Vérification de la connectivité... fait.
repo 2/20	: clone https://github.com/Oros42/IMSI-catcher.git in ./repositories/Oros42/IMSI-catcher
Clonage dans './repositories/Oros42/IMSI-catcher'...
remote: Counting objects: 48, done.
remote: Total 48 (delta 0), reused 0 (delta 0), pack-reused 48
Dépaquetage des objets: 100% (48/48), fait.
Vérification de la connectivité... fait.
repo 3/20	: clone https://github.com/Oros42/CDN_cache.git in ./repositories/Oros42/CDN_cache
Clonage dans './repositories/Oros42/CDN_cache'...
remote: Counting objects: 57, done.
remote: Total 57 (delta 0), reused 0 (delta 0), pack-reused 57
Dépaquetage des objets: 100% (57/57), fait.
Vérification de la connectivité... fait.
...
```
If you run it a second time, it will check the updates :
```
$ python github_backup_user_repos.py Oros42
20 repositories from Oros42:
repo 1/20	: no update for Oros42/tiny_DnDUp
repo 2/20	: no update for Oros42/IMSI-catcher
repo 3/20	: no update for Oros42/CDN_cache
repo 4/20	: no update for Oros42/ARP_poisoning_detector
repo 5/20	: no update for Oros42/github_backup
repo 6/20	: no update for Oros42/js_galerie
repo 7/20	: no update for Oros42/hubic_gpg
repo 8/20	: no update for Oros42/shaarlis_list
repo 9/20	: no update for Oros42/network_map
repo 10/20	: no update for Oros42/uncensor_deviantart
repo 11/20	: no update for Oros42/find_shaarlis
repo 12/20	: no update for Oros42/flickr_downloader
repo 13/20	: no update for Oros42/Pi
repo 14/20	: no update for Oros42/BooruMirror
repo 15/20	: no update for Oros42/CustomDebianSetup
repo 16/20	: no update for Oros42/CustomDebian
repo 17/20	: no update for Oros42/Playlist-generator
repo 18/20	: no update for Oros42/proxy_spider
repo 19/20	: no update for Oros42/js_terminal
repo 20/20	: no update for Oros42/github_backup_user_repos
```
