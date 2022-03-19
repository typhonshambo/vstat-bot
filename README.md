<center><img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=VSTAT&fontSize=80&fontAlignY=35&animation=twinkling&fontColor=gradient" /></center>


# Table Of Contents

<img align="right" alt="GIF" src="https://i.imgur.com/bRuHLso.png" width="200"/>

1. [Installation](#installation)
2. [Database Note](#database-note)
3. [Database Setup](#database-setup)
4. [Command List](#command-list)
5. [Region List](#region-list)
6. [Required Packages](#required-packages)
7. [Screenshots](#screenshots)
8. [Support Server](#support-server)
9. [Bot Invite](#bot-invite)
10. [BOT showcase](#BOT-showcase)
11. [Support Server](#support-server)
12. [Contributors](#contributors)
13. [Donation](#donation) 





# A discord bot made with ❤️ 
That can :<br>
<ul>
    <li>Show current server <b>status</b> of valorant for a given region, whether the servers are <b>UP or DOWN</b> </li>
    <li>Show <b> Your ingame SHOP in discord </b> </li>
    <li>Show <b> description of maps </b> </li>
    <li>Show <b> description of agents </b> </li>
    <li>Show <b> information about Weapons</b> </li>   
</ul>

More Things coming... stay tuned to find out :)

## INSTALLATION

make sure to put the necessary keys in `config.json` file [present here](https://github.com/typhonshambo/Valorant-server-stat-bot/blob/main/config/config.json) for the bot to work properly.

```json
{
    "token":"PUT_YOUR_TOKEN_HERE",
    "prefix": "!",
    "database_url":"PUT_YOUR_POSTGRES_DATABASE_URL_HERE"
}
```
### DATABASE-NOTE

Here for the bot we are using `POSTGRES SQL DATABASE`, if the database URL is not provided `in config.json` the `shop` command will not work.
If you dont know how to make a postgres database feel free to learn it from youtube or anywhere else. You can also make one postgres SQL DB in heroku
it is easy to do :)

### DATABASE-SETUP

Your database must contain a table called `acclink` and the table should contain following columns with datatypes :

|  column name             | datatype                                |
| ------------------------ | --------------------------------------- |
| userid                   | character varying                       |
| name                     | character varying                       |
| tagline                  | character varying                       |
| puuid                    | character varying                       |
| region                   | character varying                       |


 

## COMMAND-LIST


[List of commands are available here](https://github.com/typhonshambo/Valorant-server-stat-bot/blob/slash/extension/help.json)


## REGION-LIST
```css
NA      - North America
EU      - Europe
BR      - Brazil
AP      - Asia Pacific
KR      - Korea
LATAM   - Latin America
```

## REQUIRED-PACKAGES
 - discord.py
 - valoStatus
 - discord-components
 - asyncpg

you can run these commands in CMD to install the packages
```python
pip install discord.py
```
```python
pip install valoStatus
```
```python
pip install discord-components
```
## Bot-Invite
here is one ready made bot, which you can add in your server :)

<a href="https://top.gg/bot/864451929346539530">
  <img src="https://top.gg/api/widget/864451929346539530.svg">
</a>


## BOT-showcase

<img src="https://raw.githubusercontent.com/typhonshambo/Valorant-server-stat-bot/724542ab94f7409b8c5d5b3102740775143a0666/assets/VSTAT.svg" width="850"/> 



## SUPPORT-SERVER
[![Support Server](https://discord.com/api/guilds/556197206147727391/widget.png?style=banner2)](https://discord.gg/m5mSyTV7RR)


## NOTE
Although, the code of Vstat is open-source, still i do not promote cloning of my BOT. There is always a chance that you will get error if you try to self-host the BOT, in such a case no support will be provided by us. 
So, i would recommend inviting the original BOT for hassel free experience [click here](#BOT-Invite) :D

## Contributors
![GitHub Contributors Image](https://contrib.rocks/image?repo=typhonshambo/Valorant-server-stat-bot)

## Donation
[![paypal.me/typhonshambo](https://ionicabizau.github.io/badges/paypal.svg)](https://www.paypal.me/typhonshambo) - Buy me a coffee ❤️


