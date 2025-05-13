# 🎩 Prompt Genie

Prompt Genie is a sleek, responsive, real-time prompt enhancer for AI tools like ChatGPT. It helps you convert vague ideas into powerful, context-rich prompts using a preloaded library of over 100 optimized prompt templates.

---

## 🌟 Features

- 🧠 ChatGPT-like UI with real-time prompt refinement  
- 🔍 Smart prompt matching using fuzzy logic  
- 📚 100+ categorized prompt templates (resume, coding, marketing, health, etc.)  
- 📋 One-click copy to clipboard  
- 📱 Fully mobile-friendly and responsive  

---

## 🚀 Live Demo

> 💡 Simply open `index.html` in any modern web browser.

---

## 🛠️ How to Use Prompt Genie (Step-by-Step)

1. **Download or clone the repository**  

https://github.com/CrokoDam/prompt-genie.git

2. **Open the app**  
- No server needed — just double-click `index.html` or open it in your browser.

3. **Enter your raw prompt**  
- Example: `make my resume better`

4. **Click “✨ Refine Prompt”**  
- The app uses fuzzy matching to find the most relevant optimized prompt.

5. **Copy the refined result**  
- Hit the “Copy” button and paste it into ChatGPT, Claude, or any LLM interface.

---

## 🧩 File Structure


---

## 🧠 Adding Custom Prompts

To expand the library:

1. Open `prompts.json`
2. Add to any category like so:

```json
"custom_category": {
  "new prompt example": "Act as a [role] and help with [task] using this format: ..."
}
