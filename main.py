import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
import lyricsgenius

class LyricsExtractorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Lyrics Extractor")
        master.geometry("600x500")
        master.configure(bg="#f0f0f0")

        # Genius API client
        self.genius = lyricsgenius.Genius("ADD_API_KEY")

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Song Title Entry
        tk.Label(self.master, text="Song Title:", bg="#f0f0f0").pack(pady=(20,5))
        self.title_entry = tk.Entry(self.master, width=50)
        self.title_entry.pack()

        # Artist Name Entry
        tk.Label(self.master, text="Artist Name:", bg="#f0f0f0").pack(pady=(10,5))
        self.artist_entry = tk.Entry(self.master, width=50)
        self.artist_entry.pack()

        # Search Button
        self.search_button = tk.Button(self.master, text="Search Lyrics", command=self.search_lyrics)
        self.search_button.pack(pady=20)

        # Lyrics Display
        self.lyrics_display = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=70, height=20)
        self.lyrics_display.pack(pady=10)

    def search_lyrics(self):
        song_title = self.title_entry.get()
        artist_name = self.artist_entry.get()

        if not song_title or not artist_name:
            messagebox.showerror("Error", "Please enter both song title and artist name.")
            return

        try:
            song = self.genius.search_song(song_title, artist_name)
            if song:
                self.lyrics_display.delete(1.0, tk.END)
                self.lyrics_display.insert(tk.END, song.lyrics)
            else:
                messagebox.showinfo("Not Found", "Lyrics not found for the given song and artist.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LyricsExtractorGUI(root)
    root.mainloop()