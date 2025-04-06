# Technical Depth Interview Rubric

Created: 2024-10-11 15:26:17
Last Updated: 2024-10-11 15:38:31

### User - 2024-10-11 15:26:17

Write up a description and rubric for an interview question based on this note:
Trevor / Devon: Maybe let’s make it “Technical Depth” for IC2 (rather than necessarily domain knowledge) and the description can be something like “The interviewer asks the candidate questions about a domain relevant both to the candidate’s experience and to our needs. The interviewer is looking for technical depth, ability to learn and dive deep, clear communication”

The format of the question and rubric should match this. (This example is from the System Design interview which is what we previously used for IC2 candidates)

- **Details:** The candidate should be ready to design a system with conflicting or ambiguous requirements from scratch. The interviewer will choose a question appropriate for the target level. ask open-ended questions and work with the candidate collaboratively to design the system. The interviewer will ask clarifying questions to understand the decisions they make when designing system architectures. There is no specific candidate preparation required, but the candidate should be comfortable thinking through architecture in real-time, resolving ambiguities, and making trade-offs. Familiarity with system design principles and the ability to handle open-ended scenarios will be helpful.
    - The interviewer should stop digging when it’s time for Q&A. Finishing the exercise is not the goal. The goal is to get as much signal as possible.
    - The interviewer should work as a colleague, offering help if the candidate gets stuck.
    - The interviewer should choose the question to assess domain specific knowledge relevant to the role. The [backend systems architecture prompts](https://github.com/sourcegraph/interviews/blob/main/engineering/software-engineer/architecture/backend-systems/backend-systems.md) are a good starting point.
- **What to look for:**
    - How does the candidate identify and resolve ambiguity?
    - How do they make tradeoffs?
    - How do they communicate their proposal?
    - What is it like to work with them on a problem they haven’t seen before?
    - What is their intuition about solutions that are likely to yield good results?

### Assistant - 2024-10-11 15:26:22



### Assistant - 2024-10-11 15:26:22

{
  "name": "technical_depth_ic2",
  "type": "document",
  "content": "- **Details:** The candidate should be ready to discuss a technical domain that aligns both with their experience and with areas relevant to our current needs. The interviewer will select a domain topic that is appropriate for the target level and ask probing questions to assess the candidate's technical depth, their ability to dive deep, and their capacity for learning. The interviewer will aim to create a conversation where the candidate can demonstrate how they approach problems, navigate complexities, and explain their thinking. There is no specific preparation required, but the candidate should be comfortable discussing technical details, exploring underlying principles, and articulating their understanding clearly. The interviewer will help guide the conversation if the candidate gets stuck, focusing on extracting as much signal as possible rather than \"completing\" the discussion.\n    - The interviewer should stop digging when it\u2019s time for Q&A. The goal is not to finish the exercise but to assess the depth and quality of the candidate's knowledge.\n    - The interviewer should work as a collaborator, offering support and direction if the candidate needs it.\n    - The interviewer should tailor the conversation to topics that reflect the candidate's background and our technical requirements.\n- **What to look for:**\n    - How deeply can the candidate discuss the domain?\n    - Do they demonstrate an ability to dive deep into underlying principles and complexities?\n    - How do they communicate technical concepts and articulate their reasoning?\n    - How do they respond when they encounter questions or challenges that push beyond their immediate experience?\n    - Do they show a willingness and ability to learn during the conversation?\n    - What is it like to collaborate with them on exploring a technical topic?"}

### Tool (canmore.create_textdoc) - 2024-10-11 15:26:22

{"result": "Successfully created text document 'technical_depth_ic2' which will be referenced in all future messages with the unique identifier textdoc_id: '6709a60caac0819198c1f2452fb63ee4'", "textdoc_id": "6709a60caac0819198c1f2452fb63ee4", "name": "technical_depth_ic2"}

### Assistant - 2024-10-11 15:26:22

This draft provides a structure for the interview question focused on technical depth, with specific guidelines for the interviewer and clear assessment criteria. Let me know if you'd like any adjustments or further details!

### User - 2024-10-11 15:27:40

Make it clear that this is not a resume deep dive / experience question. The interviewer should ask a question that assesses the candidate's ability to go in depth and learn.

Also clarify that while it is important that the area of conversation be somewhat relevant to sourcegraph, what's more important is the candidate showing their ability to go in depth and learn

### Assistant - 2024-10-11 15:27:46

{
  "updates": [
    {
      "pattern": ".*",
      "replacement": "- **Details:** The candidate should be ready to discuss a technical domain that aligns both with their experience and with areas relevant to our current needs. This is not a resume deep dive or an assessment of past experience; instead, the interviewer will select a domain topic that is appropriate for the target level and ask probing questions to assess the candidate's technical depth, their ability to dive deep, and their capacity for learning. The interviewer will aim to create a conversation where the candidate can demonstrate how they approach problems, navigate complexities, and explain their thinking. While it is important that the area of conversation be somewhat relevant to Sourcegraph, what is more important is the candidate showing their ability to go in depth and learn. There is no specific preparation required, but the candidate should be comfortable discussing technical details, exploring underlying principles, and articulating their understanding clearly. The interviewer will help guide the conversation if the candidate gets stuck, focusing on extracting as much signal as possible rather than \"completing\" the discussion.\n    - The interviewer should stop digging when it’s time for Q&A. The goal is not to finish the exercise but to assess the depth and quality of the candidate's knowledge.\n    - The interviewer should work as a collaborator, offering support and direction if the candidate needs it.\n    - The interviewer should tailor the conversation to topics that reflect the candidate's background and our technical requirements, while ensuring the focus remains on assessing their ability to go in depth and learn.\n- **What to look for:**\n    - How deeply can the candidate discuss the domain?\n    - Do they demonstrate an ability to dive deep into underlying principles and complexities?\n    - How do they communicate technical concepts and articulate their reasoning?\n    - How do they respond when they encounter questions or challenges that push beyond their immediate experience?\n    - Do they show a willingness and ability to learn during the conversation?\n    - What is it like to collaborate with them on exploring a technical topic?"
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-11 15:27:46

{"result": "Successfully updated text document with textdoc_id '6709a60caac0819198c1f2452fb63ee4'", "textdoc_id": "6709a60caac0819198c1f2452fb63ee4"}

### Assistant - 2024-10-11 15:27:46

I've clarified that this is not a resume deep dive and emphasized the focus on the candidate's ability to go in depth and learn. Let me know if this works for you or if further adjustments are needed.

### User - 2024-10-11 15:28:04

Now make this description more fluid and concise. Keep the points, but improve the flow and polish

### Assistant - 2024-10-11 15:28:09

{
  "updates": [
    {
      "pattern": ".*",
      "replacement": "- **Details:** The candidate should be ready to discuss a technical domain that aligns with their experience and our needs. This is not a resume review or assessment of past experience; instead, the interviewer will choose a relevant topic and ask probing questions to evaluate the candidate's technical depth, ability to dive deep, and capacity for learning. The conversation should allow the candidate to demonstrate how they approach problems, navigate complexities, and explain their thinking. While relevance to Sourcegraph is ideal, the main focus is on the candidate's ability to learn and explore deeply. No specific preparation is required, but the candidate should be comfortable discussing technical details, underlying principles, and articulating their understanding. The interviewer will guide the conversation if needed, aiming to gather as much insight as possible rather than \"completing\" the discussion.\n    - The interviewer should stop digging when it’s time for Q&A. The goal is to assess the depth and quality of the candidate's knowledge, not to finish the exercise.\n    - The interviewer should work collaboratively, offering support if the candidate gets stuck.\n    - The interviewer should choose topics relevant to the candidate's background and our needs, while ensuring the focus is on assessing depth and learning ability.\n- **What to look for:**\n    - How deeply can the candidate discuss the domain?\n    - Do they demonstrate an ability to dive into underlying principles and complexities?\n    - How clearly do they communicate technical concepts and articulate their reasoning?\n    - How do they handle questions or challenges that push beyond their immediate experience?\n    - Do they show a willingness and ability to learn during the conversation?\n    - What is it like to collaborate with them on a technical topic?"
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-11 15:28:09

{"result": "Successfully updated text document with textdoc_id '6709a60caac0819198c1f2452fb63ee4'", "textdoc_id": "6709a60caac0819198c1f2452fb63ee4"}

### Assistant - 2024-10-11 15:28:09

I've made the description more concise and improved the flow for better readability. Let me know if this works or if you'd like further adjustments.

### User - 2024-10-11 15:32:27

"capacity for learning" sounds a little condescending toward the candidate. Update the phrasing

### Assistant - 2024-10-11 15:32:29

{
  "updates": [
    {
      "pattern": "capacity for learning",
      "replacement": "ability to learn and adapt"
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-11 15:32:29

{"result": "Successfully updated text document with textdoc_id '6709a60caac0819198c1f2452fb63ee4'", "textdoc_id": "6709a60caac0819198c1f2452fb63ee4"}

### Assistant - 2024-10-11 15:32:29

I've updated the phrasing to "ability to learn and adapt" to make it sound more respectful toward the candidate. Let me know if there's anything else you'd like to adjust.

### User - 2024-10-11 15:34:08

This will be shared with the candidate and the interviewer. So if there are any other ways to make this more respectful from the candidate without losing clarity and high standard, please make those changes

### Assistant - 2024-10-11 15:34:13

{
  "updates": [
    {
      "pattern": ".*",
      "replacement": "- **Details:** The candidate should be prepared to discuss a technical domain that aligns with their experience. The interviewer will choose a relevant topic and ask probing questions to explore the candidate's technical knowledge, depth of understanding, and ability to learn and adapt. The conversation is designed to give the candidate an opportunity to demonstrate how they approach problems, navigate complexities, and explain their thinking. While it's ideal if the topic is relevant to Sourcegraph, the primary focus is on the candidate's ability to learn and explore deeply. No specific preparation is required, but the candidate should be comfortable discussing technical details, underlying principles, and articulating their understanding. The interviewer will guide the conversation as needed, focusing on gathering meaningful insights rather than \"completing\" the discussion.\n  - The interviewer should transition to Q&A when appropriate. The goal is to assess the depth and quality of the candidate's knowledge, not to finish the exercise.\n  - The interviewer should work collaboratively, offering support if the candidate needs it.\n  - The interviewer should select topics that reflect the candidate's background and our needs, while keeping the focus on assessing depth and learning ability.\n- **What to look for:**\n  - How deeply can the candidate discuss the domain?\n  - Do they demonstrate an ability to dive into underlying principles and complexities?\n  - How clearly do they communicate technical concepts and articulate their reasoning?\n  - How do they handle questions or challenges that push beyond their immediate experience?\n  - Do they show a willingness and ability to learn during the conversation?\n  - What is it like to collaborate with them on a technical topic?"
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-11 15:34:13

{"result": "Successfully updated text document with textdoc_id '6709a60caac0819198c1f2452fb63ee4'", "textdoc_id": "6709a60caac0819198c1f2452fb63ee4"}

### Assistant - 2024-10-11 15:34:13

I've made adjustments to make the language more respectful and candidate-friendly while maintaining clarity and high standards. Let me know if there's anything else you'd like to refine.

### User - 2024-10-11 15:35:35

This sentence feels a bit redundant with the rest of the details + what to look for. Simplify or remove it to get rid of the redundancies: The conversation is designed to give the candidate an opportunity to demonstrate how they approach problems, navigate complexities, and explain their thinking. 

### Assistant - 2024-10-11 15:35:37

{
  "updates": [
    {
      "pattern": "The conversation is designed to give the candidate an opportunity to demonstrate how they approach problems, navigate complexities, and explain their thinking\\. ",
      "replacement": ""
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-11 15:35:37

{"result": "Successfully updated text document with textdoc_id '6709a60caac0819198c1f2452fb63ee4'", "textdoc_id": "6709a60caac0819198c1f2452fb63ee4"}

### Assistant - 2024-10-11 15:35:37

I've removed the redundant sentence to improve conciseness. Let me know if there's anything else you'd like to adjust.

### User - 2024-10-11 15:35:45

Remove other redundancies

### Assistant - 2024-10-11 15:35:50

{
  "updates": [
    {
      "pattern": "The interviewer will choose a relevant topic and ask probing questions to explore the candidate's technical knowledge, depth of understanding, and ability to learn and adapt\\. ",
      "replacement": "The interviewer will choose a relevant topic and ask questions to explore the candidate's technical knowledge and ability to learn and adapt. "
    },
    {
      "pattern": "The interviewer will guide the conversation as needed, focusing on gathering meaningful insights rather than \"completing\" the discussion\\. ",
      "replacement": "The interviewer will guide the conversation to gather meaningful insights. "
    },
    {
      "pattern": "The interviewer should select topics that reflect the candidate's background and our needs, while keeping the focus on assessing depth and learning ability\\.",
      "replacement": "The interviewer should select topics relevant to the candidate's background and our needs."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-11 15:35:50

Failed with error. Fix the error and try again before replying to the user.

updates.1.pattern: pattern not found in the document: /The interviewer will guide the conversation as needed, focusing on gathering meaningful insights rather than "completing" the discussion\. / pattern must be a python regular expression with valid escape sequences

### Assistant - 2024-10-11 15:35:50

{
  "updates": [
    {
      "pattern": "The interviewer will choose a relevant topic and ask probing questions to explore the candidate's technical knowledge, depth of understanding, and ability to learn and adapt\\.",
      "replacement": "The interviewer will choose a relevant topic and ask questions to explore the candidate's technical knowledge and ability to learn and adapt."
    },
    {
      "pattern": "The interviewer will guide the conversation as needed, focusing on gathering meaningful insights rather than \\\"completing\\\" the discussion\\.",
      "replacement": "The interviewer will guide the conversation to gather meaningful insights."
    },
    {
      "pattern": "The interviewer should select topics that reflect the candidate's background and our needs, while keeping the focus on assessing depth and learning ability\\.",
      "replacement": "The interviewer should select topics relevant to the candidate's background and our needs."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-11 15:35:50

{"result": "Successfully updated text document with textdoc_id '6709a60caac0819198c1f2452fb63ee4'", "textdoc_id": "6709a60caac0819198c1f2452fb63ee4"}

### Assistant - 2024-10-11 15:35:50

I've removed redundancies to make the text more concise while retaining the key points. Let me know if there's anything else you'd like to adjust.

### User - 2024-10-11 15:37:14

This line does not feel aligned with the type of question (it was originally from a collaborative design question). Replace it with something that keeps the spirit of the conversation being collaboartive without making it sound like a design question: The interviewer should work collaboratively, offering support if the candidate needs it.

### Assistant - 2024-10-11 15:37:16

{
  "updates": [
    {
      "pattern": "The interviewer should work collaboratively, offering support if the candidate needs it\\.",
      "replacement": "The interviewer should foster an open discussion, providing guidance and support as needed to help the candidate demonstrate their depth of understanding."
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-11 15:37:16

{"result": "Successfully updated text document with textdoc_id '6709a60caac0819198c1f2452fb63ee4'", "textdoc_id": "6709a60caac0819198c1f2452fb63ee4"}

### Assistant - 2024-10-11 15:37:16

I've updated the line to better reflect the nature of the conversation, emphasizing collaboration without making it sound like a design question. Let me know if this works or if you'd like further adjustments.

### User - 2024-10-11 15:38:28

This one feels vague. "What is it like to collaborate with them on a technical topic?"

Align it more with "The interviewer should foster an open discussion, directing the conversation help the candidate demonstrate their depth of understanding. Avoid trivia or "gotcha" style questions."

### Assistant - 2024-10-11 15:38:30

{
  "updates": [
    {
      "pattern": "What is it like to collaborate with them on a technical topic\\?",
      "replacement": "How effectively do they engage in an open discussion, demonstrating their depth of understanding without needing trivia or \"gotcha\" questions?"
    }
  ]
}

### Tool (canmore.update_textdoc) - 2024-10-11 15:38:30

{"result": "Successfully updated text document with textdoc_id '6709a60caac0819198c1f2452fb63ee4'", "textdoc_id": "6709a60caac0819198c1f2452fb63ee4"}

### Assistant - 2024-10-11 15:38:30

I've updated the line to better align with the collaborative and supportive approach of the interview. Let me know if there's anything else you'd like to modify.

