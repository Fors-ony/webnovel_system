# WebNovel System Recommender 📜

An interactive Python terminal application that generates personalized WebNovel recommendations formatted like an anime or light novel status card. Built as a project for Stanford's **Code in Place**.



## 🌟 About the Project

Finding a good WebNovel to read usually means endless scrolling. This tool prompts the user for their reader name, favorite tropes, and desired vibe, then leverages an LLM wrapper to return a single tailored recommendation complete with a trope breakdown, synopsis, and binge-risk warning.

## 🚀 Features

- **Interactive Terminal UI:** Collects reading preferences directly from user input.
- **System Persona:** Uses prompt engineering to deliver recommendations from a dramatic "WebNovel System" spirit.
- **Structured Status Cards:** Formats the output with clean visual borders, trope tags, binge ratings, and funny warnings.

---

## 💻 How to Run

1. Open the project inside the **Code in Place** workspace.
2. Run `main.py`.
3. Follow the terminal prompts to enter your reader name, favorite trope, and desired vibe.

---

## 📋 Sample Output

```text
========================================
  📜 THE HEAVENLY WEBNOVEL ARCHIVE 📜   
========================================

Enter your reader name: Alex
Favorite trope (e.g., Reincarnation, System UI, Cultivation): System UI
Desired vibe (e.g., Dark, Funny, OP MC, Trashy Binge): Dark

----------------------------------------
📖 TITLE: Solo Leveling
🏷️ TROPE: System UI, Dungeon Crawler, OP MC
⭐ BINGE RATING: 10/10

SYNOPSIS:
When a low-rank hunter gains access to a mysterious quest system that only he can see, he begins leveling up beyond human limits. As shadow armies rise at his command, he uncovers the terrifying origin behind the dungeons threatening world destruction.

SYSTEM'S WARNING TO ALEX:
If you start reading this past 11 PM, accept that your sleep schedule is officially dead.
----------------------------------------

