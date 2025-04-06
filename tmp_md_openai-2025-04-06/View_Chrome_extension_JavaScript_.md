# View Chrome extension JavaScript.

Created: 2023-03-29 15:02:16
Last Updated: 2023-03-29 15:54:54

### User - 2023-03-29 15:02:16

How do I view the javascript for an installed chrome extension?

### Assistant - 2023-03-29 15:02:32

To view the JavaScript code for an installed Chrome extension, you can follow these steps:

1. Open the Google Chrome browser and click on the three dots icon in the top right corner.

2. Select "More tools" from the dropdown menu, and then click on "Extensions".

3. Find the extension you want to view the code for and click on the "Details" button.

4. Scroll down to the bottom of the page and click on the "View files" button. This will open the extension's folder in your file explorer.

5. Look for a file named "background.js" or "content.js". These are the files that contain the extension's JavaScript code.

6. Open the file in a text editor to view the code.

Note that some extensions may use minified or obfuscated code, which can make it more difficult to read and understand. Additionally, be careful when editing extension code as it could potentially break the functionality of the extension.

### User - 2023-03-29 15:54:29

Define a chrome extension which recolors google tasks on google calendar blue

### Assistant - 2023-03-29 15:54:42

A Chrome extension is a software program that can be installed into the Google Chrome browser to add new features or modify existing functionality. In this case, a Chrome extension could be created to recolor Google Tasks on Google Calendar blue.

The extension would need to modify the CSS styles for Google Tasks to change the color scheme. This could be done by injecting custom CSS rules into the page when it loads, using the Chrome extension API.

The extension would also need to detect when the user is viewing their Google Calendar and ensure that the recolored tasks are visible on the calendar. This could be done by listening for events on the page and updating the styles as necessary.

Overall, the extension would provide a more visually appealing and customized experience for users who frequently use Google Tasks and Google Calendar together.

### User - 2023-03-29 15:54:54

Output code for a chrome extension which recolors google tasks on google calendar blue

### Assistant - 2023-03-29 15:55:24

Here is some sample code for a Chrome extension that recolors Google Tasks on Google Calendar to blue:

manifest.json:
```
{
  "manifest_version": 2,
  "name": "Google Tasks Recolor",
  "version": "1.0",
  "description": "Recolors Google Tasks on Google Calendar to blue",
  "permissions": ["https://calendar.google.com/*"],
  "content_scripts": [
    {
      "matches": ["https://calendar.google.com/*"],
      "js": ["content.js"],
      "run_at": "document_idle"
    }
  ]
}
```

content.js:
```
function recolorTasks() {
  const taskList = document.querySelectorAll('.vH8W6e-LgbsSe');
  taskList.forEach((task) => {
    task.style.backgroundColor = 'blue';
  });
}

const observer = new MutationObserver((mutationsList) => {
  for (let mutation of mutationsList) {
    if (mutation.type === 'childList' && mutation.target.id === 'grid-container') {
      recolorTasks();
    }
  }
});

observer.observe(document.body, { childList: true, subtree: true });

recolorTasks();
```

This code adds a content script to the extension that runs on Google Calendar pages. The script uses a MutationObserver to listen for changes to the page and recolors Google Tasks to blue using the `recolorTasks()` function. The function selects all task elements with a specific class name and changes their background color to blue.

Note that this code is just an example and may need to be adjusted based on changes to the Google Calendar website. Additionally, it is important to ensure that the extension only modifies the DOM elements it is intended to modify and does not interfere with other functionality on the page.

