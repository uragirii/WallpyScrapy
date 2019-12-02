# WallpyScrapy

We all like awesome wallpapers and some subreddits on reddits have really awesome wallpapers. So this script downloads top 5 wallpapers from the given subreddits and save it in the destinaation folder.

In `Windows` you can set that folder for slideshow for your Desktop Background.

You need to create an app for your reddit account and obtain `client_secret` and `client_id` for that app. If you don't know how to create this, [follow these instructions](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps)

The configurations for this must be saved in the `config.json` file. The `config.json` must include following keys:
- `client_secret`: Your `client_secret` for the created app.
- `client_id` : Your `client_id` for the created app.
- `destination` : Directory, where you want to save images.
- `subreddits` : String which contain list of subreddits you want to crawl for images.
- `upvote` : Whether you want to upvote the post, you are downloading or not. You should consider to upvote the posts.
- `username` : [Optional] This is only required, if `upvote` is set to `"True"`. Provide username of your bot or account.
- `password` : [Optional] This is only required, if `upvote` is set to `"True"`. Provide password of your bot or account.


for example you donot want to upvote the posts, then your `config.json` must look like this.
```
{
    "client_secret" : "gko_LXELoV07ZBNUXrvWZfzE3aI",
    "client_id" : "p-jcoLKBynTLew",
    "destination" : "Wallpapers",
    "subreddits" : "['wallpapers', 'wallpaper']",
    "upvote" : "False"
}
```

But if you want to upvote the posts, then your `config.json` must look like :
```
{
    "username" : "reddit_bot",
    "password" : "snoo"
    "client_secret" : "gko_LXELoV07ZBNUXrvWZfzE3aI",
    "client_id" : "p-jcoLKBynTLew",
    "destination" : "Wallpapers",
    "subreddits" : "['wallpapers', 'wallpaper']",
    "upvote" : "True"
}
```



_Please note that above examples values have been taken from [this website](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps). Please create your own reddit app for this script to run and you must **never** share `client_id` and `client_secret` with anyone or on public forum. If you don't know how to create your reddit app, please [follow these instructions](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps)_
