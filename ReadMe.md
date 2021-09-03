# Post Forwarder Bot

This bot can send all new messages from one channel, directly to another channel (or group, just in case), without the forwarded tag!

## Setting up 
* First:
> `APP_ID` and `API_HASH` - Get it from my.telegram.org   
> `BOT_TOKEN` - Get it from [@BotFather](https://t.me/BotFather)   
> `FROM_CHANNEL` - The ID of the main channel from where posts have to be copied.  
> `TO_CHANNEL` - The ID of the channel to which the posts are to be sent.  
   
* Chose a platform to deploy on:
<details>
<summary>Deploy on Heroku</summary>

<p align="left">
  <a href="https://heroku.com/deploy?template=https://github.com/stark-Prince/PostForwarderBot">
     <img height="30px" src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku">
  </a>
</p>

</details>

<details>
<summary>Local Deploys</summary>
<br>
- Clone the repo:   <code>git clone https://github.com/stark-Prince/PostForwarderBot</code></br>
- Make a <code>.env</code> file in the root of the repo and fill in the values.</br>
- Use <code>python3 bot.py</code> to start the bot.</br>  
</details>

## Usage
Add the bot to both channels with admin permission
All new messages will be auto-posted!!

Updates Channel [Bots Hub](https://t.me/roBots_Hub) for help.
Support Chat [Bots Hub Support](https://t.me/roBots_HubSupport) for help.   
