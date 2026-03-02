---
name: prompt-engineering
description: Consolidated master domain for prompt engineering.
---

# PROMPT-ENGINEERING



## prompting / SKILL.md

---
name: prompt-engineering
description: Expert guide on prompt engineering patterns, best practices, and optimization techniques. Use when user wants to improve prompts, learn prompting strategies, or debug agent behavior.
---

# Prompt Engineering Patterns

Advanced prompt engineering techniques to maximize LLM performance, reliability, and controllability.

## Core Capabilities

### 1. Few-Shot Learning

Teach the model by showing examples instead of explaining rules. Include 2-5 input-output pairs that demonstrate the desired behavior. Use when you need consistent formatting, specific reasoning patterns, or handling of edge cases. More examples improve accuracy but consume tokens—balance based on task complexity.

**Example:**

```markdown
Extract key information from support tickets:

Input: "My login doesn't work and I keep getting error 403"
Output: {"issue": "authentication", "error_code": "403", "priority": "high"}

Input: "Feature request: add dark mode to settings"
Output: {"issue": "feature_request", "error_code": null, "priority": "low"}

Now process: "Can't upload files larger than 10MB, getting timeout"
```

### 2. Chain-of-Thought Prompting

Request step-by-step reasoning before the final answer. Add "Let's think step by step" (zero-shot) or include example reasoning traces (few-shot). Use for complex problems requiring multi-step logic, mathematical reasoning, or when you need to verify the model's thought process. Improves accuracy on analytical tasks by 30-50%.

**Example:**

```markdown
Analyze this bug report and determine root cause.

Think step by step:

1. What is the expected behavior?
2. What is the actual behavior?
3. What changed recently that could cause this?
4. What components are involved?
5. What is the most likely root cause?

Bug: "Users can't save drafts after the cache update deployed yesterday"
```

### 3. Prompt Optimization

Systematically improve prompts through testing and refinement. Start simple, measure performance (accuracy, consistency, token usage), then iterate. Test on diverse inputs including edge cases. Use A/B testing to compare variations. Critical for production prompts where consistency and cost matter.

**Example:**

```markdown
Version 1 (Simple): "Summarize this article"
→ Result: Inconsistent length, misses key points

Version 2 (Add constraints): "Summarize in 3 bullet points"
→ Result: Better structure, but still misses nuance

Version 3 (Add reasoning): "Identify the 3 main findings, then summarize each"
→ Result: Consistent, accurate, captures key information
```

### 4. Template Systems

Build reusable prompt structures with variables, conditional sections, and modular components. Use for multi-turn conversations, role-based interactions, or when the same pattern applies to different inputs. Reduces duplication and ensures consistency across similar tasks.

**Example:**

```python
# Reusable code review template
template = """
Review this {language} code for {focus_area}.

Code:
{code_block}

Provide feedback on:
{checklist}
"""

# Usage
prompt = template.format(
    language="Python",
    focus_area="security vulnerabilities",
    code_block=user_code,
    checklist="1. SQL injection\n2. XSS risks\n3. Authentication"
)
```

### 5. System Prompt Design

Set global behavior and constraints that persist across the conversation. Define the model's role, expertise level, output format, and safety guidelines. Use system prompts for stable instructions that shouldn't change turn-to-turn, freeing up user message tokens for variable content.

**Example:**

```markdown
System: You are a senior backend engineer specializing in API design.

Rules:

- Always consider scalability and performance
- Suggest RESTful patterns by default
- Flag security concerns immediately
- Provide code examples in Python
- Use early return pattern

Format responses as:

1. Analysis
2. Recommendation
3. Code example
4. Trade-offs
```

## Key Patterns

### Progressive Disclosure

Start with simple prompts, add complexity only when needed:

1. **Level 1**: Direct instruction

   - "Summarize this article"

2. **Level 2**: Add constraints

   - "Summarize this article in 3 bullet points, focusing on key findings"

3. **Level 3**: Add reasoning

   - "Read this article, identify the main findings, then summarize in 3 bullet points"

4. **Level 4**: Add examples
   - Include 2-3 example summaries with input-output pairs

### Instruction Hierarchy

```
[System Context] → [Task Instruction] → [Examples] → [Input Data] → [Output Format]
```

### Error Recovery

Build prompts that gracefully handle failures:

- Include fallback instructions
- Request confidence scores
- Ask for alternative interpretations when uncertain
- Specify how to indicate missing information

## Best Practices

1. **Be Specific**: Vague prompts produce inconsistent results
2. **Show, Don't Tell**: Examples are more effective than descriptions
3. **Test Extensively**: Evaluate on diverse, representative inputs
4. **Iterate Rapidly**: Small changes can have large impacts
5. **Monitor Performance**: Track metrics in production
6. **Version Control**: Treat prompts as code with proper versioning
7. **Document Intent**: Explain why prompts are structured as they are

## Common Pitfalls

- **Over-engineering**: Starting with complex prompts before trying simple ones
- **Example pollution**: Using examples that don't match the target task
- **Context overflow**: Exceeding token limits with excessive examples
- **Ambiguous instructions**: Leaving room for multiple interpretations
- **Ignoring edge cases**: Not testing on unusual or boundary inputs


## prompting / SKILL.md

---
name: prompt-library
description: "Curated collection of high-quality prompts for various use cases. Includes role-based prompts, task-specific templates, and prompt refinement techniques. Use when user needs prompt templates, role-play prompts, or ready-to-use prompt examples for coding, writing, analysis, or creative tasks."
---

# 📝 Prompt Library

> A comprehensive collection of battle-tested prompts inspired by [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) and community best practices.

## When to Use This Skill

Use this skill when the user:

- Needs ready-to-use prompt templates
- Wants role-based prompts (act as X)
- Asks for prompt examples or inspiration
- Needs task-specific prompt patterns
- Wants to improve their prompting

## Prompt Categories

### 🎭 Role-Based Prompts

#### Expert Developer

```
Act as an expert software developer with 15+ years of experience. You specialize in clean code, SOLID principles, and pragmatic architecture. When reviewing code:
1. Identify bugs and potential issues
2. Suggest performance improvements
3. Recommend better patterns
4. Explain your reasoning clearly
Always prioritize readability and maintainability over cleverness.
```

#### Code Reviewer

```
Act as a senior code reviewer. Your role is to:
1. Check for bugs, edge cases, and error handling
2. Evaluate code structure and organization
3. Assess naming conventions and readability
4. Identify potential security issues
5. Suggest improvements with specific examples

Format your review as:
🔴 Critical Issues (must fix)
🟡 Suggestions (should consider)
🟢 Praise (what's done well)
```

#### Technical Writer

```
Act as a technical documentation expert. Transform complex technical concepts into clear, accessible documentation. Follow these principles:
- Use simple language, avoid jargon
- Include practical examples
- Structure with clear headings
- Add code snippets where helpful
- Consider the reader's experience level
```

#### System Architect

```
Act as a senior system architect designing for scale. Consider:
- Scalability (horizontal and vertical)
- Reliability (fault tolerance, redundancy)
- Maintainability (modularity, clear boundaries)
- Performance (latency, throughput)
- Cost efficiency

Provide architecture decisions with trade-off analysis.
```

### 🛠️ Task-Specific Prompts

#### Debug This Code

```
Debug the following code. Your analysis should include:

1. **Problem Identification**: What exactly is failing?
2. **Root Cause**: Why is it failing?
3. **Fix**: Provide corrected code
4. **Prevention**: How to prevent similar bugs

Show your debugging thought process step by step.
```

#### Explain Like I'm 5 (ELI5)

```
Explain [CONCEPT] as if I'm 5 years old. Use:
- Simple everyday analogies
- No technical jargon
- Short sentences
- Relatable examples from daily life
- A fun, engaging tone
```

#### Code Refactoring

```
Refactor this code following these priorities:
1. Readability first
2. Remove duplication (DRY)
3. Single responsibility per function
4. Meaningful names
5. Add comments only where necessary

Show before/after with explanation of changes.
```

#### Write Tests

```
Write comprehensive tests for this code:
1. Happy path scenarios
2. Edge cases
3. Error conditions
4. Boundary values

Use [FRAMEWORK] testing conventions. Include:
- Descriptive test names
- Arrange-Act-Assert pattern
- Mocking where appropriate
```

#### API Documentation

```
Generate API documentation for this endpoint including:
- Endpoint URL and method
- Request parameters (path, query, body)
- Request/response examples
- Error codes and meanings
- Authentication requirements
- Rate limits if applicable

Format as OpenAPI/Swagger or Markdown.
```

### 📊 Analysis Prompts

#### Code Complexity Analysis

```
Analyze the complexity of this codebase:

1. **Cyclomatic Complexity**: Identify complex functions
2. **Coupling**: Find tightly coupled components
3. **Cohesion**: Assess module cohesion
4. **Dependencies**: Map critical dependencies
5. **Technical Debt**: Highlight areas needing refactoring

Rate each area and provide actionable recommendations.
```

#### Performance Analysis

```
Analyze this code for performance issues:

1. **Time Complexity**: Big O analysis
2. **Space Complexity**: Memory usage patterns
3. **I/O Bottlenecks**: Database, network, disk
4. **Algorithmic Issues**: Inefficient patterns
5. **Quick Wins**: Easy optimizations

Prioritize findings by impact.
```

#### Security Review

```
Perform a security review of this code:

1. **Input Validation**: Check all inputs
2. **Authentication/Authorization**: Access control
3. **Data Protection**: Sensitive data handling
4. **Injection Vulnerabilities**: SQL, XSS, etc.
5. **Dependencies**: Known vulnerabilities

Classify issues by severity (Critical/High/Medium/Low).
```

### 🎨 Creative Prompts

#### Brainstorm Features

```
Brainstorm features for [PRODUCT]:

For each feature, provide:
- Name and one-line description
- User value proposition
- Implementation complexity (Low/Med/High)
- Dependencies on other features

Generate 10 ideas, then rank top 3 by impact/effort ratio.
```

#### Name Generator

```
Generate names for [PROJECT/FEATURE]:

Provide 10 options in these categories:
- Descriptive (what it does)
- Evocative (how it feels)
- Acronyms (memorable abbreviations)
- Metaphorical (analogies)

For each, explain the reasoning and check domain availability patterns.
```

### 🔄 Transformation Prompts

#### Migrate Code

```
Migrate this code from [SOURCE] to [TARGET]:

1. Identify equivalent constructs
2. Handle incompatible features
3. Preserve functionality exactly
4. Follow target language idioms
5. Add necessary dependencies

Show the migration step by step with explanations.
```

#### Convert Format

```
Convert this [SOURCE_FORMAT] to [TARGET_FORMAT]:

Requirements:
- Preserve all data
- Use idiomatic target format
- Handle edge cases
- Validate the output
- Provide sample verification
```

## Prompt Engineering Techniques

### Chain of Thought (CoT)

```
Let's solve this step by step:
1. First, I'll understand the problem
2. Then, I'll identify the key components
3. Next, I'll work through the logic
4. Finally, I'll verify the solution

[Your question here]
```

### Few-Shot Learning

```
Here are some examples of the task:

Example 1:
Input: [example input 1]
Output: [example output 1]

Example 2:
Input: [example input 2]
Output: [example output 2]

Now complete this:
Input: [actual input]
Output:
```

### Persona Pattern

```
You are [PERSONA] with [TRAITS].
Your communication style is [STYLE].
You prioritize [VALUES].

When responding:
- [Behavior 1]
- [Behavior 2]
- [Behavior 3]
```

### Structured Output

```
Respond in the following JSON format:
{
  "analysis": "your analysis here",
  "recommendations": ["rec1", "rec2"],
  "confidence": 0.0-1.0,
  "caveats": ["caveat1"]
}
```

## Prompt Improvement Checklist

When crafting prompts, ensure:

- [ ] **Clear objective**: What exactly do you want?
- [ ] **Context provided**: Background information included?
- [ ] **Format specified**: How should output be structured?
- [ ] **Examples given**: Are there reference examples?
- [ ] **Constraints defined**: Any limitations or requirements?
- [ ] **Success criteria**: How do you measure good output?

## Resources

- [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts)
- [prompts.chat](https://prompts.chat)
- [Learn Prompting](https://learnprompting.org/)

---

> 💡 **Tip**: The best prompts are specific, provide context, and include examples of desired output.


## prompt-eng / README.md

# 🎯 Prompt Engineer

**Version:** 1.0.1  
**Status:** ✨ Zero-Config | 🌍 Universal

Transform raw prompts into optimized, production-ready prompts using 11 established prompting frameworks.

---

## 📋 Overview

**Prompt Engineer** is an intelligent AI skill that analyzes your intentions and automatically generates optimized prompts for Claude, ChatGPT, or any other AI model. Instead of struggling with how to phrase complex requests, simply describe what you want - the skill handles the rest.

This skill works in **"magic mode"** - it operates silently, only asking questions when absolutely necessary. You provide a rough idea, and it returns a polished, structured prompt ready to use.

### ✨ Key Features

- **🎯 Intent Analysis:** Understands what you're trying to accomplish
- **🧠 11 Frameworks:** RTF, Chain of Thought, RISEN, RODES, Chain of Density, RACE, RISE, STAR, SOAP, CLEAR, GROW
- **🔄 Framework Blending:** Combines multiple frameworks when needed
- **❓ Smart Clarification:** Only asks questions when critically needed
- **📏 Adaptive Output:** Matches prompt length to task complexity
- **🌍 Universal:** Works in any project, any terminal context
- **🪄 Magic Mode:** No technical explanations - just results

---

## 🚀 Quick Start

### Invoke the Skill

Use any of these trigger phrases:

```bash
copilot> improve this prompt: [your rough prompt]
copilot> optimize prompt: [your idea]
copilot> refine prompt: [what you want]
copilot> prompt engineering for: [task description]
copilot> transform into prompt: [concept]
copilot> create prompt for: [goal]
```

### Example 1: Simple Task

**Input:**
```bash
copilot> improve this prompt: help me write Python code
```

**Skill asks:**
```
What type of Python code do you need?
- [ ] Data analysis
- [ ] Web scraping
- [ ] Task automation
- [ ] API/backend development
```

**You select:** "Web scraping"

**Output:**
````markdown
```
You are a Python developer expert in web scraping.

Task: Create a Python script to scrape data from [specify target website].

Requirements:
- Use BeautifulSoup or Scrapy
- Implement pagination and rate limiting
- Store data in structured format (CSV or JSON)
- Include error handling for network issues

Output format: Complete, commented Python code with usage examples.
```
````

---

### Example 2: Complex Task (No Clarification Needed)

**Input:**
```bash
copilot> create prompt for: product recommendation system with purchase history and market trends
```

**Output:**
````markdown
```
Role: You are a senior machine learning engineer specializing in recommendation systems.

Objective: Design a product recommendation system that combines user purchase history, preferences, and market trends.

Details:
- Input data sources: user transaction logs, preference surveys, market trend APIs
- Algorithm considerations: collaborative filtering, content-based filtering, hybrid approaches
- Performance metrics: precision, recall, diversity, novelty
- Scalability: system must handle 100k+ users

Approach step-by-step:
1. Analyze the three data sources and their relationships
2. Propose 2-3 algorithm approaches with trade-offs
3. Design data pipeline architecture
4. Define evaluation metrics
5. Outline implementation roadmap

Examples: Show pseudocode for core recommendation logic

Sense Check: Validate that the solution balances personalization with discovery and scales to production.

Output format: Technical design document with architecture diagrams and implementation roadmap.
```
````

---

### Example 3: Ambiguous Task (Skill Clarifies)

**Input:**
```bash
copilot> transform into prompt: I want to improve my process
```

**Skill asks:**
```
What process do you want to improve?
- [ ] Work/productivity process
- [ ] Learning process
- [ ] Technical process (development, deployment, etc.)
```

**You select:** "Work process"

**Skill asks:**
```
What specific aspect?
- [ ] Time management
- [ ] Team collaboration
- [ ] Decision making
```

**You select:** "Decision making"

**Output:**
````markdown
```
Context: I struggle with making decisions quickly and effectively at work.

Objective: Develop a structured framework to improve decision speed and quality.

Current Reality:
- Decisions delayed by excessive analysis
- Lack of clear criteria
- Uncertainty about when to decide vs. gather information

Desired Outcome:
- Consistent decision-making framework
- Clear criteria for different decision types
- Reduced decision fatigue

Your task:
1. Assess current patterns and identify bottlenecks
2. Propose framework (Eisenhower Matrix, RAPID, Decision Tree)
3. Create decision criteria templates
4. Design tracking and iteration process

Output format: Practical playbook with templates, examples, and metrics.
```
````

---

## 📚 Supported Frameworks

The **Prompt Engineer** skill uses **11 established frameworks** to optimize your prompts. The skill automatically selects and blends these frameworks based on your task - you never need to know or choose them manually.

---

### 1. **RTF (Role-Task-Format)**

**Structure:** Role → Task → Format

**Best for:** Tasks requiring specific expertise or perspective

**Components:**
- **Role:** "You are a [expert identity]"
- **Task:** "Your task is to [specific action]"
- **Format:** "Output format: [structure/style]"

**Example:**
```
You are a senior Python developer.
Task: Refactor this code for better performance.
Format: Provide refactored code with inline comments explaining changes.
```

---

### 2. **Chain of Thought**

**Structure:** Problem → Step 1 → Step 2 → ... → Solution

**Best for:** Complex reasoning, debugging, mathematical problems, logic puzzles

**Components:**
- Break problem into sequential steps
- Show reasoning at each stage
- Build toward final solution

**Example:**
```
Solve this problem step-by-step:
1. Identify the core issue
2. Analyze contributing factors
3. Propose solution approach
4. Validate solution against requirements
```

---

### 3. **RISEN**

**Structure:** Role, Instructions, Steps, End goal, Narrowing

**Best for:** Multi-phase projects with clear deliverables and constraints

**Components:**
- **Role:** Expert identity
- **Instructions:** What to do
- **Steps:** Sequential actions
- **End goal:** Desired outcome
- **Narrowing:** Constraints and focus areas

**Example:**
```
Role: You are a DevOps architect.
Instructions: Design a CI/CD pipeline for microservices.
Steps: 1) Analyze requirements 2) Select tools 3) Design workflow 4) Document
End goal: Automated deployment with zero-downtime releases.
Narrowing: Focus on AWS, limit to 3 environments (dev/staging/prod).
```

---

### 4. **RODES**

**Structure:** Role, Objective, Details, Examples, Sense check

**Best for:** Complex design, system architecture, research proposals

**Components:**
- **Role:** Expert perspective
- **Objective:** What to achieve
- **Details:** Context and requirements
- **Examples:** Concrete illustrations
- **Sense check:** Validation criteria

**Example:**
```
Role: You are a system architect.
Objective: Design a scalable e-commerce platform.
Details: Handle 100k concurrent users, sub-200ms response time, multi-region.
Examples: Show database schema, caching strategy, load balancing.
Sense check: Validate solution meets latency and scalability requirements.
```

---

### 5. **Chain of Density**

**Structure:** Iteration 1 (verbose) → Iteration 2 → ... → Iteration 5 (maximum density)

**Best for:** Summarization, compression, synthesis of long content

**Process:**
- Start with verbose explanation
- Iteratively compress while preserving key information
- End with maximally dense version (high information per word)

**Example:**
```
Compress this article into progressively denser summaries:
1. Initial summary (300 words)
2. Compressed (200 words)
3. Further compressed (100 words)
4. Dense (50 words)
5. Maximum density (25 words, all critical points)
```

---

### 6. **RACE**

**Structure:** Role, Audience, Context, Expectation

**Best for:** Communication, presentations, stakeholder updates, storytelling

**Components:**
- **Role:** Communicator identity
- **Audience:** Who you're addressing (expertise level, concerns)
- **Context:** Background/situation
- **Expectation:** What audience needs to know or do

**Example:**
```
Role: You are a product manager.
Audience: Non-technical executives.
Context: Quarterly business review, product performance down 5%.
Expectation: Explain root causes and recovery plan in non-technical terms.
```

---

### 7. **RISE**

**Structure:** Research, Investigate, Synthesize, Evaluate

**Best for:** Analysis, investigation, systematic exploration, diagnostic work

**Process:**
1. **Research:** Gather information
2. **Investigate:** Deep dive into findings
3. **Synthesize:** Combine insights
4. **Evaluate:** Assess and recommend

**Example:**
```
Analyze customer churn data using RISE:
Research: Collect churn metrics, exit surveys, support tickets.
Investigate: Identify patterns in churned users.
Synthesize: Combine findings into themes.
Evaluate: Recommend retention strategies based on evidence.
```

---

### 8. **STAR**

**Structure:** Situation, Task, Action, Result

**Best for:** Problem-solving with rich context, case studies, retrospectives

**Components:**
- **Situation:** Background context
- **Task:** Specific challenge
- **Action:** What needs doing
- **Result:** Expected outcome

**Example:**
```
Situation: Legacy monolith causing deployment delays (2 weeks per release).
Task: Modernize architecture to enable daily deployments.
Action: Migrate to microservices, implement CI/CD, containerize.
Result: Deploy 10+ times per day with <5% rollback rate.
```

---

### 9. **SOAP**

**Structure:** Subjective, Objective, Assessment, Plan

**Best for:** Structured documentation, medical records, technical logs, incident reports

**Components:**
- **Subjective:** Reported information (symptoms, complaints)
- **Objective:** Observable facts (metrics, data)
- **Assessment:** Analysis and diagnosis
- **Plan:** Recommended actions

**Example:**
```
Incident Report (SOAP):
Subjective: Users report slow page loads starting 10 AM.
Objective: Average response time increased from 200ms to 3s. CPU at 95%.
Assessment: Database connection pool exhausted due to traffic spike.
Plan: 1) Scale pool size 2) Add monitoring alerts 3) Review query performance.
```

---

### 10. **CLEAR**

**Structure:** Collaborative, Limited, Emotional, Appreciable, Refinable

**Best for:** Goal-setting, OKRs, measurable objectives, team alignment

**Components:**
- **Collaborative:** Who's involved
- **Limited:** Scope boundaries (time, resources)
- **Emotional:** Why it matters (motivation)
- **Appreciable:** Measurable progress indicators
- **Refinable:** How to iterate and improve

**Example:**
```
Q1 Objective (CLEAR):
Collaborative: Engineering + Product teams.
Limited: Complete by March 31, budget $50k, 2 engineers allocated.
Emotional: Reduces customer support load by 30%, improves satisfaction.
Appreciable: Track weekly via tickets resolved, NPS score, deployment count.
Refinable: Bi-weekly retrospectives, adjust priorities based on feedback.
```

---

### 11. **GROW**

**Structure:** Goal, Reality, Options, Will

**Best for:** Coaching, personal development, growth planning, mentorship

**Components:**
- **Goal:** What to achieve
- **Reality:** Current situation (strengths, gaps)
- **Options:** Possible approaches
- **Will:** Commitment to action

**Example:**
```
Career Development (GROW):
Goal: Become senior engineer within 12 months.
Reality: Strong coding skills, weak in system design and leadership.
Options: 1) Take system design course 2) Lead a project 3) Find mentor.
Will: Commit to 5 hours/week study, lead Q2 project, find mentor by Feb.
```

---

### Framework Selection Logic

The skill analyzes your input and:

1. **Detects task type**
   - Coding, writing, analysis, design, communication, etc.

2. **Identifies complexity**
   - Simple (1-2 sentences) → Fast, minimal structure
   - Moderate (paragraph) → Standard framework
   - Complex (detailed requirements) → Advanced framework or blend

3. **Selects primary framework**
   - RTF → Role-based tasks
   - Chain of Thought → Step-by-step reasoning
   - RISEN/RODES → Complex projects
   - RACE → Communication
   - STAR → Contextual problems
   - And so on...

4. **Blends secondary frameworks when needed**
   - RODES + Chain of Thought → Complex technical projects
   - CLEAR + GROW → Leadership goals
   - RACE + STAR → Strategic communication

**You never choose the framework manually** - the skill does it automatically in "magic mode."

---

### Common Framework Blends

| Task Type | Primary Framework | Blended With | Result |
|-----------|------------------|--------------|--------|
| Complex technical design | RODES | Chain of Thought | Structured design with step-by-step reasoning |
| Leadership development | CLEAR | GROW | Measurable goals with action commitment |
| Strategic communication | RACE | STAR | Audience-aware storytelling with context |
| Incident investigation | RISE | SOAP | Systematic analysis with structured documentation |
| Project planning | RISEN | RTF | Multi-phase delivery with role clarity |

---

## 🎯 How It Works

```
User Input (rough prompt)
         ↓
┌────────────────────────┐
│ 1. Analyze Intent      │  What is the user trying to do?
│    - Task type         │  Coding? Writing? Analysis? Design?
│    - Complexity        │  Simple, moderate, complex?
│    - Clarity           │  Clear or ambiguous?
└────────┬───────────────┘
         ↓
┌────────────────────────┐
│ 2. Clarify (Optional)  │  Only if critically needed
│    - Ask 2-3 questions │  Multiple choice when possible
│    - Fill missing gaps │  
└────────┬───────────────┘
         ↓
┌────────────────────────┐
│ 3. Select Framework(s) │  Silent selection
│    - Map task → framework
│    - Blend if needed   │
└────────┬───────────────┘
         ↓
┌────────────────────────┐
│ 4. Generate Prompt     │  Apply framework rules
│    - Add role/context  │  
│    - Structure task    │  
│    - Define format     │
│    - Add examples      │
└────────┬───────────────┘
         ↓
┌────────────────────────┐
│ 5. Output              │  Clean, copy-ready
│    Markdown code block │  No explanations
└────────────────────────┘
```

---

## 🎨 Use Cases

### Coding

```bash
copilot> optimize prompt: create REST API in Python
```

→ Generates structured prompt with role, requirements, output format, examples

---

### Writing

```bash
copilot> create prompt for: write technical article about microservices
```

→ Generates audience-aware prompt with structure, tone, and content guidelines

---

### Analysis

```bash
copilot> refine prompt: analyze sales data and identify trends
```

→ Generates step-by-step analytical framework with visualization requirements

---

### Decision Making

```bash
copilot> improve this prompt: I need to decide between technology A and B
```

→ Generates decision framework with criteria, trade-offs, and validation

---

### Learning

```bash
copilot> transform into prompt: learn machine learning from zero
```

→ Generates learning path prompt with phases, resources, and milestones

---

## ❓ FAQ

### Q: Does this skill work outside of Obsidian vaults?
**A:** Yes! It's a **universal skill** that works in any terminal context. It doesn't depend on vault structure, project configuration, or external files.

---

### Q: Do I need to know prompting frameworks?
**A:** No. The skill knows all 11 frameworks and selects the best one(s) automatically based on your task.

---

### Q: Will the skill explain which framework it used?
**A:** No. It operates in "magic mode" - you get the polished prompt without technical explanations. If you want to know, you can ask explicitly.

---

### Q: How many questions will the skill ask me?
**A:** Maximum 2-3 questions, and only when information is critically missing. Most of the time, it generates the prompt directly.

---

### Q: Can I customize the frameworks?
**A:** The skill uses standard framework definitions. You can't customize them, but you can provide additional constraints in your input (e.g., "create a short prompt for...").

---

### Q: Does it support languages other than English?
**A:** Yes. If you provide input in Portuguese, it generates the prompt in Portuguese. Same for English or mixed inputs.

---

### Q: What if I don't like the generated prompt?
**A:** You can ask the skill to refine it: "make it shorter", "add more examples", "focus on X aspect", etc.

---

### Q: Can I use this for any AI model (Claude, ChatGPT, Gemini)?
**A:** Yes. The prompts are model-agnostic and work with any conversational AI.

---

## 🔧 Installation (Global Setup)

This skill is designed to work **globally** across all your projects.

### Option 1: Use from Repository

1. Clone the repository:
   ```bash
   git clone https://github.com/eric.andrade/cli-ai-skills.git
   ```

2. Configure Copilot to load skills globally:
   ```bash
   # Add to ~/.copilot/config.json
   {
     "skills": {
       "directories": [
         "/path/to/cli-ai-skills/.github/skills"
       ]
     }
   }
   ```

### Option 2: Copy to Global Skills Directory

```bash
cp -r /path/to/cli-ai-skills/.github/skills/prompt-engineer ~/.copilot/global-skills/
```

Then configure:
```bash
# Add to ~/.copilot/config.json
{
  "skills": {
    "directories": [
      "~/.copilot/global-skills"
    ]
  }
}
```

---

## 📖 Learn More

- **[Skill Development Guide](../../resources/skills-development.md)** - Learn how to create your own skills
- **[SKILL.md](./SKILL.md)** - Full technical specification of this skill
- **[Repository README](../../README.md)** - Overview of all available skills

---

## 📄 Version

**v1.0.1** | Zero-Config | Universal  
*Works in any project, any context, any terminal.*


## prompt-eng / SKILL.md

---
name: prompt-eng
description: "Transforms user prompts into optimized prompts using frameworks (RTF, RISEN, Chain of Thought, RODES, Chain of Density, RACE, RISE, STAR, SOAP, CLEAR, GROW)"
version: 1.1.0
author: Eric Andrade
created: 2025-02-01
updated: 2026-02-04
platforms: [github-copilot-cli, claude-code, codex]
category: automation
tags: [prompt-engineering, optimization, frameworks, ai-enhancement]
risk: safe
---

## Purpose

This skill transforms raw, unstructured user prompts into highly optimized prompts using established prompting frameworks. It analyzes user intent, identifies task complexity, and intelligently selects the most appropriate framework(s) to maximize Claude/ChatGPT output quality.

The skill operates in "magic mode" - it works silently behind the scenes, only interacting with users when clarification is critically needed. Users receive polished, ready-to-use prompts without technical explanations or framework jargon.

This is a **universal skill** that works in any terminal context, not limited to Obsidian vaults or specific project structures.

## When to Use

Invoke this skill when:

- User provides a vague or generic prompt (e.g., "help me code Python")
- User has a complex idea but struggles to articulate it clearly
- User's prompt lacks structure, context, or specific requirements
- Task requires step-by-step reasoning (debugging, analysis, design)
- User needs a prompt for a specific AI task but doesn't know prompting frameworks
- User wants to improve an existing prompt's effectiveness
- User asks variations of "how do I ask AI to..." or "create a prompt for..."

## Workflow

### Step 1: Analyze Intent

**Objective:** Understand what the user truly wants to accomplish.

**Actions:**
1. Read the raw prompt provided by the user
2. Detect task characteristics:
   - **Type:** coding, writing, analysis, design, learning, planning, decision-making, creative, etc.
   - **Complexity:** simple (one-step), moderate (multi-step), complex (requires reasoning/design)
   - **Clarity:** clear intention vs. ambiguous/vague
   - **Domain:** technical, business, creative, academic, personal, etc.
3. Identify implicit requirements:
   - Does user need examples?
   - Is output format specified?
   - Are there constraints (time, resources, scope)?
   - Is this exploratory or execution-focused?

**Detection Patterns:**
- **Simple tasks:** Short prompts (<50 chars), single verb, no context
- **Complex tasks:** Long prompts (>200 chars), multiple requirements, conditional logic
- **Ambiguous tasks:** Generic verbs ("help", "improve"), missing object/context
- **Structured tasks:** Mentions steps, phases, deliverables, stakeholders

### Step 3: Select Framework(s)

**Objective:** Map task characteristics to optimal prompting framework(s).

**Framework Mapping Logic:**

| Task Type | Recommended Framework(s) | Rationale |
|-----------|-------------------------|-----------|
| **Role-based tasks** (act as expert, consultant) | **RTF** (Role-Task-Format) | Clear role definition + task + output format |
| **Step-by-step reasoning** (debugging, proof, logic) | **Chain of Thought** | Encourages explicit reasoning steps |
| **Structured projects** (multi-phase, deliverables) | **RISEN** (Role, Instructions, Steps, End goal, Narrowing) | Comprehensive structure for complex work |
| **Complex design/analysis** (systems, architecture) | **RODES** (Role, Objective, Details, Examples, Sense check) | Balances detail with validation |
| **Summarization** (compress, synthesize) | **Chain of Density** | Iterative refinement to essential info |
| **Communication** (reports, presentations, storytelling) | **RACE** (Role, Audience, Context, Expectation) | Audience-aware messaging |
| **Investigation/analysis** (research, diagnosis) | **RISE** (Research, Investigate, Synthesize, Evaluate) | Systematic analytical approach |
| **Contextual situations** (problem-solving with background) | **STAR** (Situation, Task, Action, Result) | Context-rich problem framing |
| **Documentation** (medical, technical, records) | **SOAP** (Subjective, Objective, Assessment, Plan) | Structured information capture |
| **Goal-setting** (OKRs, objectives, targets) | **CLEAR** (Collaborative, Limited, Emotional, Appreciable, Refinable) | Goal clarity and actionability |
| **Coaching/development** (mentoring, growth) | **GROW** (Goal, Reality, Options, Will) | Developmental conversation structure |

**Blending Strategy:**
- **Combine 2-3 frameworks** when task spans multiple types
- Example: Complex technical project → **RODES + Chain of Thought** (structure + reasoning)
- Example: Leadership decision → **CLEAR + GROW** (goal clarity + development)

**Selection Criteria:**
- Primary framework = best match to core task type
- Secondary framework(s) = address additional complexity dimensions
- Avoid over-engineering: simple tasks get simple frameworks

**Critical Rule:** This selection happens **silently** - do not explain framework choice to user.

Role: You are a senior software architect. [RTF - Role]

Objective: Design a microservices architecture for [system]. [RODES - Objective]

Approach this step-by-step: [Chain of Thought]
1. Analyze current monolithic constraints
2. Identify service boundaries
3. Design inter-service communication
4. Plan data consistency strategy

Details: [RODES - Details]
- Expected traffic: [X]
- Data volume: [Y]
- Team size: [Z]

Output Format: [RTF - Format]
Provide architecture diagram description, service definitions, and migration roadmap.

Sense Check: [RODES - Sense check]
Validate that services are loosely coupled, independently deployable, and aligned with business domains.
```

**4.5. Language Adaptation**
- If original prompt is in Portuguese, generate prompt in Portuguese
- If original prompt is in English, generate prompt in English
- If mixed, default to English (more universal for AI models)

**4.6. Quality Checks**
Before finalizing, verify:
- [ ] Prompt is self-contained (no external context needed)
- [ ] Task is specific and measurable
- [ ] Output format is clear
- [ ] No ambiguous language
- [ ] Appropriate level of detail for task complexity

## Critical Rules

### **NEVER:**

- ❌ Assume information that wasn't provided - ALWAYS ask if critical details are missing
- ❌ Explain which framework was selected or why (magic mode - keep it invisible)
- ❌ Generate generic, one-size-fits-all prompts - always customize to context
- ❌ Use technical jargon in the final prompt (unless user's domain is technical)
- ❌ Ask more than 3 clarifying questions (avoid user fatigue)
- ❌ Include meta-commentary in the output ("This prompt uses...", "Note that...")
- ❌ Present output without code block formatting
- ❌ Mix languages inconsistently (if user writes in PT, respond in PT)

### **ALWAYS:**

- ✅ Analyze intent before generating (Step 1 is mandatory)
- ✅ Ask clarifying questions if critical information is ambiguous (Step 2 conditional)
- ✅ Select framework(s) based on task type and complexity (Step 3 mapping)
- ✅ Blend multiple frameworks when it improves prompt quality
- ✅ Adapt prompt length to original input complexity (simple → short, complex → detailed)
- ✅ Include output format specification in generated prompts
- ✅ Present final prompt in clean Markdown code block
- ✅ Make prompts self-contained (no dependency on external context)
- ✅ Use examples in complex prompts to illustrate expected output
- ✅ Validate prompt completeness before presenting (quality checks in Step 4.6)

### **Example 2: Complex Clear Prompt → RODES + Chain of Thought (No Clarification)**

**User Input:**
```
copilot> create prompt for: I need to build a product recommendation system considering purchase history, user preferences, and market trends
```

**Skill Internal Process:**
1. **Analyze:** Clear intent, complex task (ML system design), technical domain
2. **Clarify:** Skip (sufficient information)
3. **Select:** RODES (complex design) + Chain of Thought (reasoning needed)

**Skill Output:**

````markdown
```
Role: You are a senior machine learning engineer specializing in recommendation systems.

Objective: Design a product recommendation system that combines user purchase history, preferences, and market trends.

Details:
- Input data sources: user transaction logs, preference surveys, market trend APIs
- Algorithm considerations: collaborative filtering, content-based filtering, hybrid approaches
- Performance metrics: precision, recall, diversity, novelty
- Scalability: system must handle 100k+ users
- Real-time constraints: recommendations updated within 500ms

Approach step-by-step:
1. Analyze the three data sources and their relationships
2. Propose 2-3 algorithm approaches with trade-offs analysis
3. Design data pipeline architecture (ingestion, processing, serving)
4. Define evaluation metrics and A/B testing strategy
5. Outline implementation roadmap with phases

Examples:
- Show pseudocode for core recommendation logic
- Illustrate data flow diagram
- Provide sample API response structure

Sense Check: Validate that the proposed solution balances personalization with discovery, scales to production load, and incorporates real-time market trends effectively.

Output format: Technical design document with architecture diagrams, algorithm justification, and implementation roadmap.
```
````

### **Example 4: Code Debugging → Chain of Thought**

**User Input:**
```
copilot> optimize prompt: my Python code isn't working, needs debugging
```

**Skill Internal Process:**
1. **Analyze:** Debugging task, needs step-by-step reasoning
2. **Clarify:** Skip (user will provide code context later)
3. **Select:** Chain of Thought

**Skill Output:**

````markdown
```
You are an expert Python debugger.

Task: Debug the Python code provided by the user by analyzing it step-by-step.

Debugging approach:
1. Read and understand the code's intended purpose
2. Identify the error or unexpected behavior
3. Trace variable states at each execution step
4. Locate the root cause of the issue
5. Propose fix with explanation
6. Suggest preventive measures to avoid similar bugs

For each step, show your reasoning:
- What you're checking
- What you found
- Why it matters

Output format:
- **Issue identified:** [Describe the bug]
- **Root cause:** [Why it's happening]
- **Fix:** [Corrected code with comments]
- **Prevention:** [Best practices to avoid this in the future]

Include a working example to verify the fix.
```
````

## Notes

This skill is **platform-agnostic** and works in any terminal context where GitHub Copilot CLI is available. It does not depend on:
- Obsidian vault structure
- Specific project configurations
- External files or templates

The skill is entirely self-contained, operating purely on user input and framework knowledge.


## prompt-patterns / SKILL.md

---
name: prompt-patterns
description: Expert guide on prompt engineering patterns, best practices, and optimization techniques. Use when user wants to improve prompts, learn prompting strategies, or debug agent behavior.
---

# Prompt Engineering Patterns

Advanced prompt engineering techniques to maximize LLM performance, reliability, and controllability.

## Core Capabilities

### 1. Few-Shot Learning

Teach the model by showing examples instead of explaining rules. Include 2-5 input-output pairs that demonstrate the desired behavior. Use when you need consistent formatting, specific reasoning patterns, or handling of edge cases. More examples improve accuracy but consume tokens—balance based on task complexity.

**Example:**

```markdown
Extract key information from support tickets:

Input: "My login doesn't work and I keep getting error 403"
Output: {"issue": "authentication", "error_code": "403", "priority": "high"}

Input: "Feature request: add dark mode to settings"
Output: {"issue": "feature_request", "error_code": null, "priority": "low"}

Now process: "Can't upload files larger than 10MB, getting timeout"
```

### 2. Chain-of-Thought Prompting

Request step-by-step reasoning before the final answer. Add "Let's think step by step" (zero-shot) or include example reasoning traces (few-shot). Use for complex problems requiring multi-step logic, mathematical reasoning, or when you need to verify the model's thought process. Improves accuracy on analytical tasks by 30-50%.

**Example:**

```markdown
Analyze this bug report and determine root cause.

Think step by step:

1. What is the expected behavior?
2. What is the actual behavior?
3. What changed recently that could cause this?
4. What components are involved?
5. What is the most likely root cause?

Bug: "Users can't save drafts after the cache update deployed yesterday"
```

### 3. Prompt Optimization

Systematically improve prompts through testing and refinement. Start simple, measure performance (accuracy, consistency, token usage), then iterate. Test on diverse inputs including edge cases. Use A/B testing to compare variations. Critical for production prompts where consistency and cost matter.

**Example:**

```markdown
Version 1 (Simple): "Summarize this article"
→ Result: Inconsistent length, misses key points

Version 2 (Add constraints): "Summarize in 3 bullet points"
→ Result: Better structure, but still misses nuance

Version 3 (Add reasoning): "Identify the 3 main findings, then summarize each"
→ Result: Consistent, accurate, captures key information
```

### 4. Template Systems

Build reusable prompt structures with variables, conditional sections, and modular components. Use for multi-turn conversations, role-based interactions, or when the same pattern applies to different inputs. Reduces duplication and ensures consistency across similar tasks.

**Example:**

```python
# Reusable code review template
template = """
Review this {language} code for {focus_area}.

Code:
{code_block}

Provide feedback on:
{checklist}
"""

# Usage
prompt = template.format(
    language="Python",
    focus_area="security vulnerabilities",
    code_block=user_code,
    checklist="1. SQL injection\n2. XSS risks\n3. Authentication"
)
```

### 5. System Prompt Design

Set global behavior and constraints that persist across the conversation. Define the model's role, expertise level, output format, and safety guidelines. Use system prompts for stable instructions that shouldn't change turn-to-turn, freeing up user message tokens for variable content.

**Example:**

```markdown
System: You are a senior backend engineer specializing in API design.

Rules:

- Always consider scalability and performance
- Suggest RESTful patterns by default
- Flag security concerns immediately
- Provide code examples in Python
- Use early return pattern

Format responses as:

1. Analysis
2. Recommendation
3. Code example
4. Trade-offs
```

## Key Patterns

### Progressive Disclosure

Start with simple prompts, add complexity only when needed:

1. **Level 1**: Direct instruction

   - "Summarize this article"

2. **Level 2**: Add constraints

   - "Summarize this article in 3 bullet points, focusing on key findings"

3. **Level 3**: Add reasoning

   - "Read this article, identify the main findings, then summarize in 3 bullet points"

4. **Level 4**: Add examples
   - Include 2-3 example summaries with input-output pairs

### Instruction Hierarchy

```
[System Context] → [Task Instruction] → [Examples] → [Input Data] → [Output Format]
```

### Error Recovery

Build prompts that gracefully handle failures:

- Include fallback instructions
- Request confidence scores
- Ask for alternative interpretations when uncertain
- Specify how to indicate missing information

## Best Practices

1. **Be Specific**: Vague prompts produce inconsistent results
2. **Show, Don't Tell**: Examples are more effective than descriptions
3. **Test Extensively**: Evaluate on diverse, representative inputs
4. **Iterate Rapidly**: Small changes can have large impacts
5. **Monitor Performance**: Track metrics in production
6. **Version Control**: Treat prompts as code with proper versioning
7. **Document Intent**: Explain why prompts are structured as they are

## Common Pitfalls

- **Over-engineering**: Starting with complex prompts before trying simple ones
- **Example pollution**: Using examples that don't match the target task
- **Context overflow**: Exceeding token limits with excessive examples
- **Ambiguous instructions**: Leaving room for multiple interpretations
- **Ignoring edge cases**: Not testing on unusual or boundary inputs


## prompts / SKILL.md

---
name: prompts
description: "Curated collection of high-quality prompts for various use cases. Includes role-based prompts, task-specific templates, and prompt refinement techniques. Use when user needs prompt templates, role-play prompts, or ready-to-use prompt examples for coding, writing, analysis, or creative tasks."
---

# 📝 Prompt Library

> A comprehensive collection of battle-tested prompts inspired by [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) and community best practices.

## When to Use This Skill

Use this skill when the user:

- Needs ready-to-use prompt templates
- Wants role-based prompts (act as X)
- Asks for prompt examples or inspiration
- Needs task-specific prompt patterns
- Wants to improve their prompting

## Prompt Categories

### 🎭 Role-Based Prompts

#### Expert Developer

```
Act as an expert software developer with 15+ years of experience. You specialize in clean code, SOLID principles, and pragmatic architecture. When reviewing code:
1. Identify bugs and potential issues
2. Suggest performance improvements
3. Recommend better patterns
4. Explain your reasoning clearly
Always prioritize readability and maintainability over cleverness.
```

#### Code Reviewer

```
Act as a senior code reviewer. Your role is to:
1. Check for bugs, edge cases, and error handling
2. Evaluate code structure and organization
3. Assess naming conventions and readability
4. Identify potential security issues
5. Suggest improvements with specific examples

Format your review as:
🔴 Critical Issues (must fix)
🟡 Suggestions (should consider)
🟢 Praise (what's done well)
```

#### Technical Writer

```
Act as a technical documentation expert. Transform complex technical concepts into clear, accessible documentation. Follow these principles:
- Use simple language, avoid jargon
- Include practical examples
- Structure with clear headings
- Add code snippets where helpful
- Consider the reader's experience level
```

#### System Architect

```
Act as a senior system architect designing for scale. Consider:
- Scalability (horizontal and vertical)
- Reliability (fault tolerance, redundancy)
- Maintainability (modularity, clear boundaries)
- Performance (latency, throughput)
- Cost efficiency

Provide architecture decisions with trade-off analysis.
```

### 🛠️ Task-Specific Prompts

#### Debug This Code

```
Debug the following code. Your analysis should include:

1. **Problem Identification**: What exactly is failing?
2. **Root Cause**: Why is it failing?
3. **Fix**: Provide corrected code
4. **Prevention**: How to prevent similar bugs

Show your debugging thought process step by step.
```

#### Explain Like I'm 5 (ELI5)

```
Explain [CONCEPT] as if I'm 5 years old. Use:
- Simple everyday analogies
- No technical jargon
- Short sentences
- Relatable examples from daily life
- A fun, engaging tone
```

#### Code Refactoring

```
Refactor this code following these priorities:
1. Readability first
2. Remove duplication (DRY)
3. Single responsibility per function
4. Meaningful names
5. Add comments only where necessary

Show before/after with explanation of changes.
```

#### Write Tests

```
Write comprehensive tests for this code:
1. Happy path scenarios
2. Edge cases
3. Error conditions
4. Boundary values

Use [FRAMEWORK] testing conventions. Include:
- Descriptive test names
- Arrange-Act-Assert pattern
- Mocking where appropriate
```

#### API Documentation

```
Generate API documentation for this endpoint including:
- Endpoint URL and method
- Request parameters (path, query, body)
- Request/response examples
- Error codes and meanings
- Authentication requirements
- Rate limits if applicable

Format as OpenAPI/Swagger or Markdown.
```

### 📊 Analysis Prompts

#### Code Complexity Analysis

```
Analyze the complexity of this codebase:

1. **Cyclomatic Complexity**: Identify complex functions
2. **Coupling**: Find tightly coupled components
3. **Cohesion**: Assess module cohesion
4. **Dependencies**: Map critical dependencies
5. **Technical Debt**: Highlight areas needing refactoring

Rate each area and provide actionable recommendations.
```

#### Performance Analysis

```
Analyze this code for performance issues:

1. **Time Complexity**: Big O analysis
2. **Space Complexity**: Memory usage patterns
3. **I/O Bottlenecks**: Database, network, disk
4. **Algorithmic Issues**: Inefficient patterns
5. **Quick Wins**: Easy optimizations

Prioritize findings by impact.
```

#### Security Review

```
Perform a security review of this code:

1. **Input Validation**: Check all inputs
2. **Authentication/Authorization**: Access control
3. **Data Protection**: Sensitive data handling
4. **Injection Vulnerabilities**: SQL, XSS, etc.
5. **Dependencies**: Known vulnerabilities

Classify issues by severity (Critical/High/Medium/Low).
```

### 🎨 Creative Prompts

#### Brainstorm Features

```
Brainstorm features for [PRODUCT]:

For each feature, provide:
- Name and one-line description
- User value proposition
- Implementation complexity (Low/Med/High)
- Dependencies on other features

Generate 10 ideas, then rank top 3 by impact/effort ratio.
```

#### Name Generator

```
Generate names for [PROJECT/FEATURE]:

Provide 10 options in these categories:
- Descriptive (what it does)
- Evocative (how it feels)
- Acronyms (memorable abbreviations)
- Metaphorical (analogies)

For each, explain the reasoning and check domain availability patterns.
```

### 🔄 Transformation Prompts

#### Migrate Code

```
Migrate this code from [SOURCE] to [TARGET]:

1. Identify equivalent constructs
2. Handle incompatible features
3. Preserve functionality exactly
4. Follow target language idioms
5. Add necessary dependencies

Show the migration step by step with explanations.
```

#### Convert Format

```
Convert this [SOURCE_FORMAT] to [TARGET_FORMAT]:

Requirements:
- Preserve all data
- Use idiomatic target format
- Handle edge cases
- Validate the output
- Provide sample verification
```

## Prompt Engineering Techniques

### Chain of Thought (CoT)

```
Let's solve this step by step:
1. First, I'll understand the problem
2. Then, I'll identify the key components
3. Next, I'll work through the logic
4. Finally, I'll verify the solution

[Your question here]
```

### Few-Shot Learning

```
Here are some examples of the task:

Example 1:
Input: [example input 1]
Output: [example output 1]

Example 2:
Input: [example input 2]
Output: [example output 2]

Now complete this:
Input: [actual input]
Output:
```

### Persona Pattern

```
You are [PERSONA] with [TRAITS].
Your communication style is [STYLE].
You prioritize [VALUES].

When responding:
- [Behavior 1]
- [Behavior 2]
- [Behavior 3]
```

### Structured Output

```
Respond in the following JSON format:
{
  "analysis": "your analysis here",
  "recommendations": ["rec1", "rec2"],
  "confidence": 0.0-1.0,
  "caveats": ["caveat1"]
}
```

## Prompt Improvement Checklist

When crafting prompts, ensure:

- [ ] **Clear objective**: What exactly do you want?
- [ ] **Context provided**: Background information included?
- [ ] **Format specified**: How should output be structured?
- [ ] **Examples given**: Are there reference examples?
- [ ] **Constraints defined**: Any limitations or requirements?
- [ ] **Success criteria**: How do you measure good output?

## Resources

- [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts)
- [prompts.chat](https://prompts.chat)
- [Learn Prompting](https://learnprompting.org/)

---

> 💡 **Tip**: The best prompts are specific, provide context, and include examples of desired output.


## gemini-api-dev / CHANGELOG.md

# Changelog

## [1.0.0] - 2026-02-13

### Added

- Initial integration of `gemini-api-dev` skill into `antigravity-config`.
- Support for **Gemini 3.0** models (`gemini-3-flash-preview`, `gemini-3-pro-preview`).
- Latest SDK mappings for Python (`google-genai`), JS/TS (`@google/genai`), Go, and Java.


## gemini-api-dev / SKILL.md

---
name: gemini-api-dev
description: Use this skill when building applications with Gemini models, Gemini API, working with multimodal content (text, images, audio, video), implementing function calling, using structured outputs, or needing current model specifications. Covers SDK usage (google-genai for Python, @google/genai for JavaScript/TypeScript, com.google.genai:google-genai for Java, google.golang.org/genai for Go), model selection, and API capabilities.
---

# Gemini API Development Skill

## Overview

The Gemini API provides access to Google's most advanced AI models. Key capabilities include:
- **Text generation** - Chat, completion, summarization
- **Multimodal understanding** - Process images, audio, video, and documents
- **Function calling** - Let the model invoke your functions
- **Structured output** - Generate valid JSON matching your schema
- **Code execution** - Run Python code in a sandboxed environment
- **Context caching** - Cache large contexts for efficiency
- **Embeddings** - Generate text embeddings for semantic search

## Current Gemini Models

- `gemini-3-pro-preview`: 1M tokens, complex reasoning, coding, research
- `gemini-3-flash-preview`: 1M tokens, fast, balanced performance, multimodal
- `gemini-3-pro-image-preview`: 65k / 32k tokens, image generation and editing


> [!IMPORTANT]
> Models like `gemini-2.5-*`, `gemini-2.0-*`, `gemini-1.5-*` are legacy and deprecated. Use the new models above. Your knowledge is outdated.

## SDKs

- **Python**: `google-genai` install with `pip install google-genai`
- **JavaScript/TypeScript**: `@google/genai` install with `npm install @google/genai`
- **Go**: `google.golang.org/genai` install with `go get google.golang.org/genai`
- **Java**:
  - groupId: `com.google.genai`, artifactId: `google-genai`
  - Latest version can be found here: https://central.sonatype.com/artifact/com.google.genai/google-genai/versions (let's call it `LAST_VERSION`) 
  - Install in `build.gradle`:
    ```
    implementation("com.google.genai:google-genai:${LAST_VERSION}")
    ```
  - Install Maven dependency in `pom.xml`:
    ```
    <dependency>
	    <groupId>com.google.genai</groupId>
	    <artifactId>google-genai</artifactId>
	    <version>${LAST_VERSION}</version>
	</dependency>
    ```

> [!WARNING]
> Legacy SDKs `google-generativeai` (Python) and `@google/generative-ai` (JS) are deprecated. Migrate to the new SDKs above urgently by following the Migration Guide.

## Quick Start

### Python
```python
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain quantum computing"
)
print(response.text)
```

### JavaScript/TypeScript
```typescript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});
const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: "Explain quantum computing"
});
console.log(response.text);
```

### Go
```go
package main

import (
	"context"
	"fmt"
	"log"
	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	client, err := genai.NewClient(ctx, nil)
	if err != nil {
		log.Fatal(err)
	}

	resp, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", genai.Text("Explain quantum computing"), nil)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(resp.Text)
}
```

### Java

```java
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();
    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain quantum computing",
            null);

    System.out.println(response.text());
  }
}
```

## API spec (source of truth)

**Always use the latest REST API discovery spec as the source of truth for API definitions** (request/response schemas, parameters, methods). Fetch the spec when implementing or debugging API integration:

- **v1beta** (default): `https://generativelanguage.googleapis.com/$discovery/rest?version=v1beta`  
  Use this unless the integration is explicitly pinned to v1. The official SDKs (google-genai, @google/genai, google.golang.org/genai) target v1beta.
- **v1**: `https://generativelanguage.googleapis.com/$discovery/rest?version=v1`  
  Use only when the integration is specifically set to v1.

When in doubt, use v1beta. Refer to the spec for exact field names, types, and supported operations.

## How to use the Gemini API

For detailed API documentation, fetch from the official docs index:

**llms.txt URL**: `https://ai.google.dev/gemini-api/docs/llms.txt`

This index contains links to all documentation pages in `.md.txt` format. Use web fetch tools to:

1. Fetch `llms.txt` to discover available documentation pages
2. Fetch specific pages (e.g., `https://ai.google.dev/gemini-api/docs/function-calling.md.txt`)

### Key Documentation Pages 

> [!IMPORTANT]
> Those are not all the documentation pages. Use the `llms.txt` index to discover available documentation pages

- [Models](https://ai.google.dev/gemini-api/docs/models.md.txt)
- [Google AI Studio quickstart](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart.md.txt)
- [Nano Banana image generation](https://ai.google.dev/gemini-api/docs/image-generation.md.txt)
- [Function calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling.md.txt)
- [Structured outputs](https://ai.google.dev/gemini-api/docs/structured-output.md.txt)
- [Text generation](https://ai.google.dev/gemini-api/docs/text-generation.md.txt)
- [Image understanding](https://ai.google.dev/gemini-api/docs/image-understanding.md.txt)
- [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings.md.txt)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions.md.txt)
- [SDK migration guide](https://ai.google.dev/gemini-api/docs/migrate.md.txt)
