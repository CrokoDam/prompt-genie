// Load prompts and wait for DOM
document.addEventListener("DOMContentLoaded", () => {
  let promptTemplates = {};

  fetch("prompts.json")
    .then(res => res.json())
    .then(data => promptTemplates = data)
    .catch(err => console.error("Failed to load prompts.json:", err));

  const generateBtn = document.getElementById("generateBtn");
  const userInput = document.getElementById("userInput");
  const refinedPrompt = document.getElementById("refinedPrompt");
  const outputBox = document.getElementById("outputBox");
  const copyBtn = document.getElementById("copyBtn");
  const copyMsg = document.getElementById("copyMsg");

  generateBtn.addEventListener("click", () => {
    const raw = userInput.value.trim();
    if (!raw) {
      alert("Please enter a raw prompt.");
      return;
    }

    const match = findBestPrompt(raw, promptTemplates);
    if (!match) {
      refinedPrompt.value = "No suitable prompt found. Try rephrasing.";
    } else {
      refinedPrompt.value = match;
    }

    outputBox.classList.remove("hidden");
    copyMsg.classList.add("hidden");
  });

  copyBtn.addEventListener("click", () => {
    navigator.clipboard.writeText(refinedPrompt.value)
      .then(() => {
        copyMsg.classList.remove("hidden");
        setTimeout(() => copyMsg.classList.add("hidden"), 2000);
      })
      .catch(() => alert("Failed to copy to clipboard"));
  });

  function findBestPrompt(input, library) {
    const options = [];
    for (const category in library) {
      for (const query in library[category]) {
        options.push({
          category,
          query,
          prompt: library[category][query],
          score: similarity(input.toLowerCase(), query.toLowerCase())
        });
      }
    }

    const best = options.sort((a, b) => b.score - a.score)[0];
    return best && best.score > 0.3 ? best.prompt : null;
  }

  // Basic similarity check using Dice's coefficient
  function similarity(a, b) {
    const bigrams = s => new Set([...s].slice(0, -1).map((_, i) => s.slice(i, i + 2)));
    const aPairs = bigrams(a);
    const bPairs = bigrams(b);
    const intersection = new Set([...aPairs].filter(x => bPairs.has(x)));
    return (2 * intersection.size) / (aPairs.size + bPairs.size || 1);
  }
});
