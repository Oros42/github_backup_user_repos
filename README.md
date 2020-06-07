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
python3 github_backup_user_repos.py -h
```
```
Usage: github_backup_user_repos.py: [options]

Options:
  -h, --help            show this help message and exit
  -u USERNAME, --user=USERNAME
                        Username (From https://github.com/<Username>)
  -o OUTPUT, --output=OUTPUT
                        Path to the output directory
```
```
python github_backup_user_repos.py -u <username> -o <output_directory>
```
  
Examples :
```
$ python github_backup_user_repos.py -u Oros42 -o ./repositories/
43 repositories from Oros42:
repo 1/43	: clone https://github.com/Oros42/tiny_DnDUp.git in ./repositories/Oros42/tiny_DnDUp
Clonage dans './repositories/Oros42/tiny_DnDUp'...
remote: Counting objects: 53, done.
remote: Total 53 (delta 0), reused 0 (delta 0), pack-reused 53
Dépaquetage des objets: 100% (53/53), fait.
Vérification de la connectivité... fait.
repo 2/43	: clone https://github.com/Oros42/IMSI-catcher.git in ./repositories/Oros42/IMSI-catcher
Clonage dans './repositories/Oros42/IMSI-catcher'...
remote: Counting objects: 48, done.
remote: Total 48 (delta 0), reused 0 (delta 0), pack-reused 48
Dépaquetage des objets: 100% (48/48), fait.
Vérification de la connectivité... fait.
repo 3/43	: clone https://github.com/Oros42/CDN_cache.git in ./repositories/Oros42/CDN_cache
Clonage dans './repositories/Oros42/CDN_cache'...
remote: Counting objects: 57, done.
remote: Total 57 (delta 0), reused 0 (delta 0), pack-reused 57
Dépaquetage des objets: 100% (57/57), fait.
Vérification de la connectivité... fait.
...
```
  
If you run it a second time, it will check for updates :
```
$ python github_backup_user_repos.py -u Oros42
43 repositories from Oros42:
repo 1/43	: no update for ./repositories/Oros42/tiny_DnDUp
repo 2/43	: no update for ./repositories/Oros42/IMSI-catcher
repo 3/43	: no update for ./repositories/Oros42/CDN_cache
repo 4/43	: no update for ./repositories/Oros42/ARP_poisoning_detector
...
```
  
If you run it again after a push on the repository :
```
$ python github_backup_user_repos.py -u Oros42
43 repositories from Oros42:
repo 1/43	: no update for ./repositories/Oros42/tiny_DnDUp
repo 2/43	: no update for ./repositories/Oros42/IMSI-catcher
repo 3/43	: no update for ./repositories/Oros42/CDN_cache
repo 4/43	: no update for ./repositories/Oros42/ARP_poisoning_detector
repo 5/43	: no update for ./repositories/Oros42/github_backup
repo 6/43	: no update for ./repositories/Oros42/js_galerie
repo 7/43	: no update for ./repositories/Oros42/hubic_gpg
repo 8/43	: no update for ./repositories/Oros42/shaarlis_list
repo 9/43	: no update for ./repositories/Oros42/network_map
repo 10/43	: no update for ./repositories/Oros42/uncensor_deviantart
repo 11/43	: no update for ./repositories/Oros42/find_shaarlis
repo 12/43	: no update for ./repositories/Oros42/flickr_downloader
repo 13/43	: no update for ./repositories/Oros42/Pi
repo 14/43	: no update for ./repositories/Oros42/BooruMirror
repo 15/43	: no update for ./repositories/Oros42/CustomDebianSetup
repo 16/43	: no update for ./repositories/Oros42/CustomDebian
repo 17/43	: no update for ./repositories/Oros42/Playlist-generator
repo 18/43	: no update for ./repositories/Oros42/proxy_spider
repo 19/43	: no update for ./repositories/Oros42/js_terminal
repo 20/43	: update https://github.com/Oros42/github_backup_user_repos.git in ./repositories/Oros42/github_backup_user_repos
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Dépaquetage des objets: 100% (3/3), fait.
Depuis https://github.com/Oros42/github_backup_user_repos
   ba9f7ed..1c2f7a3  master     -> origin/master
Mise à jour ba9f7ed..1c2f7a3
Fast-forward
 README.md | 70 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 70 insertions(+)
```
  
  
Now, you can make a cron to run github_backup_user_repos.py every X time to keep your backup up to date :-)
```
crontab -l | { cat; echo "42 2 * * * python /PATH_TO_GITHUB_BACKUP_USER_REPOS/github_backup_user_repos.py -u USERNAME -o  PATH_OUTPUT &> /PATH_TO_GITHUB_BACKUP_USER_REPOS/backup.log"; } | crontab -
```
Don't forget to replace PATH_TO_GITHUB_BACKUP_USER_REPOS, PATH_OUTPUT and USERNAME.  
