# Deploy to Render

This guide will walk you through deploying your Telegram Multiple Channel Bridge Bot to Render.

## Prerequisites

- A GitHub repository with your bot code (already done: https://github.com/phanphoun/telegram-multiple-channel.git)
- A Render account (free at https://render.com)
- Your Telegram API credentials and Bot Token

## Step 1: Prepare Your Repository

Your repository is already set up with:
- ✅ `app.py` - Main bot code
- ✅ `requirements.txt` - Dependencies
- ✅ `.env.example` - Environment variables template
- ✅ `.gitignore` - Excludes sensitive files

## Step 2: Create a Render Account

1. Go to https://render.com
2. Sign up or log in
3. Connect your GitHub account to Render

## Step 3: Create a New Web Service

1. In Render dashboard, click **"New +"** → **"Web Service"**
2. Select your repository: `phanphoun/telegram-multiple-channel`
3. Configure the service:

### Basic Settings

- **Name**: `telegram-bridge-bot` (or any name you prefer)
- **Region**: Choose the region closest to your users
- **Branch**: `main`

### Runtime Settings

- **Runtime**: `Python`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python app.py`

### Environment Variables

Add the following environment variables in Render:

| Key | Value | Description |
|-----|-------|-------------|
| `API_ID` | Your API ID | From https://my.telegram.org |
| `API_HASH` | Your API Hash | From https://my.telegram.org |
| `BOT_TOKEN` | Your Bot Token | From @BotFather |
| `CHANNELS` | `minnnsara,targetcambo,channel3chat,channel4chatcam` | Comma-separated channel list |
| `TARGET_GROUP` | `disscussioncam` | Discussion group username |

**Important**: Make sure to use your actual values, not the placeholders from `.env.example`.

## Step 4: Deploy

1. Click **"Create Web Service"**
2. Render will build and deploy your bot
3. Wait for the deployment to complete (usually 2-5 minutes)

## Step 5: Monitor Your Bot

1. Go to your service dashboard in Render
2. Click on **"Logs"** to see your bot's output
3. You should see: `Professional Bridge Bot is running...`

## Step 6: Test Your Bot

1. Post a message in one of your monitored channels
2. Check the logs in Render to see if the message was forwarded
3. Verify the button appears on the original post

## Important Notes

### Free Tier Limitations

- Render's free tier spins down services after 15 minutes of inactivity
- Your bot will wake up when a new message is received (may have a slight delay)
- For 24/7 operation, consider upgrading to a paid plan ($7/month)

### Keeping Your Bot Alive (Free Tier)

If you want to keep your bot running on the free tier, you can:
1. Use a cron job to ping your bot every 10-14 minutes
2. Use a service like UptimeRobot to ping your Render service URL

### Session Files

Telethon creates session files to store authentication data. On Render:
- Session files are stored in the service's filesystem
- They persist between deployments but may be lost if the service is rebuilt
- For production, consider storing session files in Render's disk or a cloud storage

### Troubleshooting

**Bot not forwarding messages:**
- Check environment variables are set correctly
- Verify the bot is a member of the discussion group
- Check the bot has "Edit Messages" permission in channels

**Deployment fails:**
- Check the build logs in Render
- Ensure `requirements.txt` is up to date
- Verify Python version compatibility

**Bot keeps restarting:**
- Check the logs for errors
- Ensure API credentials are correct
- Verify the bot token is valid

## Alternative: Using Render CLI

If you prefer using the command line:

1. Install Render CLI:
```bash
npm install -g @render/cli
```

2. Login:
```bash
render login
```

3. Create a `render.yaml` file in your repository:
```yaml
services:
  - type: web
    name: telegram-bridge-bot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
    envVars:
      - key: API_ID
        sync: false
      - key: API_HASH
        sync: false
      - key: BOT_TOKEN
        sync: false
      - key: CHANNELS
        value: minnnsara,targetcambo,channel3chat,channel4chatcam
      - key: TARGET_GROUP
        value: disscussioncam
```

4. Deploy:
```bash
render deploy
```

## Updating Your Bot

To update your bot after making changes:

1. Push changes to GitHub:
```bash
git add .
git commit -m "Update bot"
git push
```

2. Render will automatically detect the changes and redeploy

## Support

If you encounter issues:
- Check Render's documentation: https://render.com/docs
- Check Telethon's documentation: https://docs.telethon.dev
- Review the logs in your Render dashboard
