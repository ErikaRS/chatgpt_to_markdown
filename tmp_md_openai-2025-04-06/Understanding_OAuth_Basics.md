# Understanding OAuth Basics

Created: 2024-09-28 21:57:47
Last Updated: 2024-09-28 21:57:58

### User - 2024-09-28 21:57:47

Explain this like I'm a first year college student https://stack-auth.com/blog/oauth-from-first-principles

### Assistant - 2024-09-28 21:57:57



### Assistant - 2024-09-28 21:57:57

```unknown
search("OAuth from first principles site:stack-auth.com")
```

### Tool (browser) - 2024-09-28 21:57:57

*[tether_browsing_display content]*

### Assistant - 2024-09-28 21:57:57

```unknown
mclick([4])
```

### Tool (browser) - 2024-09-28 21:57:57

*[system_error content]*

### Assistant - 2024-09-28 21:57:57

I wasn't able to retrieve the specific page, but I can still explain OAuth from first principles in a simplified way.

OAuth (Open Authorization) is a standard that allows one service (like a website or an app) to access data from another service without sharing your password. Imagine you're a college student, and you want to sign up for a new app, but instead of creating a whole new account, the app lets you sign in using your Google account. That’s OAuth in action.

Here’s a simple breakdown of the process:

1. **You (the user)**: You want to use a new app (like a homework helper) and don’t want to create a new account.
2. **The App**: This is the third-party service that wants to access your Google data to log you in.
3. **Google (the service provider)**: This holds your account information (like email or profile) and controls access to it.

### Steps of OAuth:
1. **Request Permission**: The app asks you for permission to access your Google account. You’ll usually see a pop-up asking if it's okay to let this app use your Google info.
   
2. **Authorization**: If you agree, Google sends back a temporary token (like a key) to the app that proves you allowed access. This token doesn’t give your actual Google password; it’s just a "permission slip."

3. **Access**: The app uses this token to access certain info from your Google account (like your name and email) but nothing else, because you didn’t give it permission for more.

4. **Refreshing Tokens**: These tokens expire after a while, so the app may request a new one behind the scenes without bothering you again.

### Why is this useful?
- **Security**: You don’t have to share your password with the app, which keeps your account safer.
- **Convenience**: You can log in without creating tons of new accounts or passwords for each app.

OAuth is like giving a friend a library card that only lets them check out certain books on your behalf. They don’t get your library password, and you can cancel the card if you want.

