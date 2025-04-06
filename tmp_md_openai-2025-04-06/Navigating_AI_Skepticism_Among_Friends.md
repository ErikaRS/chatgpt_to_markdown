# Navigating AI Skepticism Among Friends

Created: 2024-10-31 09:41:46
Last Updated: 2024-10-31 09:44:21

### User

*[user_editable_context content]*

### User - 2024-10-31 09:41:46

I have a group of friends I meet with for dinner every night. They are skeptical about generative AI and it comes up as a conversation frequently. I work on AI coding assistants, and while I don't want to tell people they can't talk about certain subjects or can't be skeptical, it is hard for me at the end of a work day to come into conversations so regularly that are negative about what I've been spending my energy on, especially from a group of good friends. A number of those friends work in the game industry, so the metaphor that comes to mind is if our conversations regularly revolved around the claim that video games make people violent.

I want to send the group a message that expresses my concern and asks them to tone it down a little. But I don't want it to come off as blaming or me as a victim. Also, note that my husband and I host the gathering, which impacts the dynamics. 

Draft a 3-5 sentence draft I could send to my friends. 

### Assistant - 2024-10-31 09:41:49



### Assistant - 2024-10-31 09:41:49

{
  "name": "dinner_talk",
  "type": "document",
  "content": "Hey everyone, I wanted to share something that's been on my mind. I know our conversations about generative AI often come up naturally, and I get that there's a lot to be skeptical about. That said, since I spend my workdays deeply involved in this stuff, it can be a bit draining for me to keep diving into critiques of it every night. I'd really appreciate it if we could mix things up a bit or give the AI talk a rest some evenings\u2014it would mean a lot to me. Thanks for understanding!"
}

### Tool (canmore.create_textdoc) - 2024-10-31 09:41:49

{"result": "Successfully created text document 'dinner_talk' which will be referenced in all future messages with the unique identifier textdoc_id: '6723b34c738c81919f5d36765a741366'", "textdoc_id": "6723b34c738c81919f5d36765a741366", "name": "dinner_talk"}

### Assistant - 2024-10-31 09:41:49

Does this feel like it strikes the right balance, or is there anything you'd like me to adjust? I'm here to tweak it until it feels just right for you.

### User - 2024-10-31 09:42:22

Change the tone from "every night" to "often"

### Assistant - 2024-10-31 09:42:24

{
  "updates": [
    {
      "pattern": "every night",
      "multiple": false,
      "replacement": "often"
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-31 09:42:24

{"result": "Successfully updated text document with textdoc_id '6723b34c738c81919f5d36765a741366'", "textdoc_id": "6723b34c738c81919f5d36765a741366"}

### Assistant - 2024-10-31 09:42:24

I've updated the phrasing to change "every night" to "often." Let me know if there's anything else you'd like to adjust!

### User - 2024-10-31 09:43:03

The last sentence isn't really resonating with me. Try an alternative that asks to take a break but makes it less about mixing it up. We have lots of conversations on different topics

### Assistant - 2024-10-31 09:43:06

{
  "updates": [
    {
      "pattern": "I'd really appreciate it if we could mix things up a bit or give the AI talk a rest some evenings.*",
      "multiple": false,
      "replacement": "I'd really appreciate it if we could take a break from the AI talk now and then—it would mean a lot to me."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-31 09:43:06

{"result": "Successfully updated text document with textdoc_id '6723b34c738c81919f5d36765a741366'", "textdoc_id": "6723b34c738c81919f5d36765a741366"}

### Assistant - 2024-10-31 09:43:06

I've modified the last sentence to focus on taking a break from the AI talk without emphasizing mixing things up. Let me know if this feels better or if you'd like any more adjustments!

### User - 2024-10-31 09:44:18

Add a sentence somewhere appropriate with the video game violence analogy

### Assistant - 2024-10-31 09:44:20

{
  "updates": [
    {
      "pattern": "(I get that there's a lot to be skeptical about\\.)",
      "multiple": false,
      "replacement": "I get that there's a lot to be skeptical about. It sometimes feels a bit like when people used to claim that video games make people violent—it's understandable, but it can be tough when it's a big part of your work."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-31 09:44:20

{"result": "Successfully updated text document with textdoc_id '6723b34c738c81919f5d36765a741366'", "textdoc_id": "6723b34c738c81919f5d36765a741366"}

### Assistant - 2024-10-31 09:44:20

I've added the analogy about video game violence to help illustrate your perspective. Let me know if this fits well or if you'd like any further tweaks!

