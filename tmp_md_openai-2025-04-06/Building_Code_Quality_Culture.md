# Building Code Quality Culture

Created: 2024-12-04 14:00:15
Last Updated: 2024-12-05 06:24:40

### User

*[user_editable_context content]*

### User - 2024-12-04 14:00:15

As a head of engineering, how do I build a culture of high quality code? I am an experienced engineer myself, but I spent most of my time at Google, where the baseline code and technical quality of engineers was high even for the most junior of candidates. I've never before had to take a culture that has a mix of some folks with high quality coding standards and others who are more slap and dash.

### Assistant - 2024-12-04 14:00:29



### Assistant - 2024-12-04 14:00:29

The user is a head of engineering with experience at Google, where the baseline code and technical quality were high even for junior candidates. They are now working to build a culture of high-quality code in an organization with mixed coding standards.

### Tool (bio) - 2024-12-04 14:00:29

Model set context updated.

### Assistant - 2024-12-04 14:00:29

Building a culture of high-quality code in a mixed environment can be quite challenging, especially when transitioning from a place like Google, where high standards are a given. Here are some approaches that can help foster a culture that values quality:

### **1. Shared Vision of Code Quality**
First and foremost, work with your team to create a shared understanding of what high-quality code means in your context. What does it look like, and why is it important? Some engineers may not have internalized the importance of aspects like maintainability, readability, scalability, or test coverage. A practical way to do this is through workshops or discussions where you outline examples of good code and highlight the long-term benefits for individual developers, team efficiency, and business outcomes.

- **Suggestion for Bond Building:** Consider involving your senior engineers in creating this shared definition. It can help build trust by showing that you're relying on their expertise, and also engage them as role models for others.

### **2. Implement and Enforce Standards**
Introduce code quality standards and document them clearly. This can be done through well-defined coding guidelines, best practices documentation, and a solid checklist for code reviews. Make sure these standards are accessible and visible.

- Introduce **linters**, **automated testing**, and **static code analysis** tools as gatekeepers.
- Ensure everyone follows a consistent **code review process**, where high standards are enforced constructively.

### **3. Thoughtful Code Review Culture**
Establish a code review culture where quality is discussed openly. This may require creating an atmosphere of trust, where feedback is seen as a means of learning rather than a personal attack. Encourage everyone to leave comments that aren’t just about fixing bugs but also about improving quality—such as maintainability or design suggestions.

- **Building Respect and Trust:** Set the example by participating in code reviews yourself. Take time to highlight the good practices you see alongside pointing out opportunities for improvement. Your senior engineers can also be excellent role models if you guide them to do the same.

### **4. Pairing and Mentoring**
Implement **pair programming** or mentoring relationships that allow the more experienced engineers to work alongside those who need to raise their quality standards. This helps share knowledge in real-time and directly demonstrates good practices, while also serving as a way to bond engineers who otherwise may have different habits.

- Try experimenting with **cross-team pairing** where a senior from one team pairs with a less experienced developer from another. This helps spread best practices more evenly throughout the organization.

### **5. Celebrate High-Quality Work**
Recognize and reward quality contributions. Sometimes people are unaware of the impact that well-written, maintainable code can have. Call out particularly well-written pieces of code or improvements in the codebase, both privately and publicly. This helps highlight the value that the company places on quality.

- **Human Connection Aspect:** You could hold regular "code showcase" sessions where people present parts of the code they’re particularly proud of and explain the improvements they made. It's a great way to learn, create a shared sense of pride, and recognize good work.

### **6. Create Learning Opportunities**
You mentioned the quality bar was high at Google, partly due to the hiring process. In your current situation, consider how you can **upskill** your team:
- Organize **brown bag sessions** or workshops on specific coding practices like test-driven development (TDD), clean architecture, or even specific language idioms that are essential to your codebase.
- Give people space to fail and then learn—create exercises that reflect areas where they might be weak and let them tackle those areas in a non-judgmental environment.

### **7. Make Technical Debt Visible**
Low-quality code often comes from rushed delivery, lack of understanding, or lack of seeing consequences. You can work on making **technical debt** visible by creating a technical debt board or incorporating technical debt issues into your sprint planning. This can help developers understand that short-term gains from cutting corners lead to longer-term costs.

### **Ask Yourself:**
Can you see yourself being able to lead some of these efforts yourself, or would it make sense for some of your senior engineers to take the lead? Engaging your senior engineers as partners in this transformation will help spread accountability for code quality throughout the team.

### **Next Steps:**
Which of these steps do you think you could start experimenting with next week? It might be helpful to start with a couple of easy wins, like beginning to shape a shared definition of quality and kicking off a more deliberate code review culture.

And remember to **reflect** on how these initial steps go—think about what resonated with your team, and what might need tweaking. After a couple of weeks, we can debrief and adjust based on what you observe. 

Let me know if you’d like help designing any specific part of this process, or if you need support on how to handle resistance from individuals on the team.

### User - 2024-12-05 06:23:47

Draft up something that touches on the first three through the lens of "coding standards when working with AI coding assistants". 

### Assistant - 2024-12-05 06:24:38



### Assistant - 2024-12-05 06:24:38

Here’s a draft addressing coding standards through the lens of **AI coding assistants**:

---

### **Establishing Coding Standards in an Era of AI Coding Assistants**

As we embrace the potential of AI coding assistants to speed up development and tackle repetitive tasks, it’s critical that we establish robust coding standards to ensure the quality of our output. While these tools can enhance productivity, they also introduce unique challenges—such as a potential over-reliance on suggestions or shortcuts that may not align with long-term maintainability. Here's how we can set ourselves up for success:

---

### **1. Define and Document Standards**
AI coding assistants generate code quickly, but speed doesn’t guarantee correctness, readability, or maintainability. To make sure AI outputs align with our goals, we need clearly defined and universally understood coding standards.

- **Actionable Step**: Create a document outlining our coding conventions—such as naming conventions, code structure, and testing expectations. Include examples of what “good” and “bad” implementations look like when working with AI-generated suggestions.
- **Why It Matters**: AI tools often default to generic patterns or rely on training data that may not reflect our unique needs. A clear guide ensures outputs meet our expectations and makes deviations easier to spot and correct.

---

### **2. Leverage AI as a Collaborator in Code Reviews**
Code reviews should include a deliberate focus on outputs generated by AI tools. While AI can assist with initial drafts, reviewers play a crucial role in ensuring that generated code meets both technical and contextual standards.

- **Best Practices**:
  - During reviews, reviewers should call out any AI-generated code that seems overly complex, lacks proper commenting, or doesn’t adhere to project standards.
  - Use review comments as a teaching opportunity—explain how the AI’s suggestion could be improved, and why the change is important.
- **Tooling Opportunities**: Where possible, integrate linters, static analysis, or automated testing tools into your workflow to catch obvious misalignments with standards before review.

---

### **3. Build a Culture of Accountability and Learning**
AI tools can sometimes lull teams into a false sense of security, leading to lower personal ownership of quality. To combat this, we must foster a culture where team members take responsibility for the quality of their code, whether written by them or suggested by AI.

- **Promote Best Practices**: Encourage developers to treat AI-generated suggestions as starting points rather than final implementations. This means reviewing, refactoring, and ensuring compliance with project goals.
- **Introduce AI-Specific Standards**: For example, mandate that developers:
  - Run AI-suggested code through all tests.
  - Avoid blindly copying large blocks of generated code without fully understanding it.
  - Leave comments for any AI-generated code explaining the reasoning behind using it.
- **Cultural Emphasis**: Position AI tools as enablers, not crutches. Highlight examples of team members refining AI outputs to improve readability or scalability, and celebrate those contributions.

---

### **Next Steps**
To solidify these principles:
1. **Document AI-Driven Code Standards**: Extend existing coding guidelines to explicitly address AI usage, including tips for evaluating and refining generated code.
2. **Run Training Sessions**: Host workshops or pairing sessions demonstrating best practices for using AI tools effectively.
3. **Iterate**: Solicit feedback on the integration of AI tools into coding and review processes, and refine our standards as needed.

---

By framing our coding standards around the effective use of AI tools, we can unlock the productivity benefits of AI while maintaining (and even enhancing) our commitment to high-quality code.

---

Would you like to brainstorm more concrete examples or workshop some scenarios to include in a team rollout plan?

