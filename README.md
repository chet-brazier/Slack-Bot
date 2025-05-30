# python slackbot that returns a reminder

At ZeroEyes, the AI weapon-detection company I currently work for, we have strict procedures to follow in the event that a 
real gun is detected. We have a checklist on Monday.com to reference, but lately things have been falling through the cracks. We track these
things using slack, so this is a Slack bot that in the instance of a real gun detection returns a reminder to the user to follow
the checklist on Monday.com.
---

## Architecture diagram

![Slackbot Architecture](slackbot-architecture.png)

---

## Stack used:

- Python 3
- Slack Bolt SDK
- Railway (cloud deployment)
- GitHub (version control)

---

## How it works:

1. Slack event trigger- a user posts a message in our designated slack channel
2. Bolt App receives messages, capturing text, user, and channel data
3. Detects our specific keywords that are posted in the Slack channel and verifies it with the channel ID
4. If all conditions are met, the bot sends an ephemeral reminder back to the user- "For True Positives, please be sure to follow the checklist on Monday!"
5. Securely uses tokens via environment variables in Railway cloud
   

