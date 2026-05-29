import random
import os
import time

print("======================================")
print("🎬🎵 AI RECOMMENDATION SYSTEM 🎵🎬")
print("======================================")

name = input("Enter your name: ")

# Movie data
movies = {
    "action": ["Avengers", "John Wick", "Batman"],
    "comedy": ["3 Idiots", "Mr. Bean", "Jumanji"],
    "horror": ["Conjuring", "IT", "Annabelle"],
    "sci-fi": ["Interstellar", "Avatar", "Inception"]
}

# Music data
music = {
    "happy": ["Shape of You", "Believer", "On My Way"],
    "sad": ["Let Her Go", "Someone Like You", "Faded"],
    "party": ["DJ Waley Babu", "Kala Chashma", "Levitating"],
    "relax": ["Perfect", "Night Changes", "Until I Found You"]
}

# Book data
books = {
    "motivation": ["Atomic Habits", "Rich Dad Poor Dad"],
    "programming": ["Python Crash Course", "Clean Code"],
    "story": ["Harry Potter", "The Alchemist"]
}

while True:

    print("\n========= MENU =========")
    print("1. 🎬 Movie Recommendation")
    print("2. 🎵 Music Recommendation")
    print("3. 📚 Book Recommendation")
    print("4. ⭐ Rate System")
    print("5. ❌ Exit")

    choice = input("Enter your choice: ")

    # Movie recommendation
    if choice == "1":

        print("\nMovie Categories:")
        for category in movies:
            print("➡", category)

        genre = input("Enter category: ").lower()

        if genre in movies:
            print("\n🎥 Recommended Movies:")
            for movie in movies[genre]:
                print("⭐", movie)

        else:
            print("❌ Category not found!")

    # Music recommendation
    elif choice == "2":

        print("\nMusic Moods:")
        for mood in music:
            print("🎵", mood)

        mood_choice = input("Enter mood: ").lower()

        if mood_choice in music:
            print("\n🎧 Recommended Songs:")
            for song in music[mood_choice]:
                print("♪", song)

            # Optional: play music file
            play = input("\nDo you want to play music? (yes/no): ").lower()

            if play == "yes":
                print("▶ Playing Music...")
                
                # Replace song.mp3 with your music file
                os.system("start song.mp3")

        else:
            print("❌ Mood not found!")

    # Book recommendation
    elif choice == "3":

        print("\nBook Categories:")
        for category in books:
            print("📖", category)

        genre = input("Enter category: ").lower()

        if genre in books:
            print("\n📚 Recommended Books:")
            for book in books[genre]:
                print("⭐", book)

        else:
            print("❌ Category not found!")

    # Rating system
    elif choice == "4":

        rating = int(input("Rate our system (1-5): "))

        if rating >= 4:
            print("😊 Thank you for your positive feedback!")
        else:
            print("🙂 We will improve the system!")

    # Exit
    elif choice == "5":

        print(f"\n👋 Goodbye {name}!")
        print("Thank you for using AI Recommendation System")
        break

    else:
        print("❌ Invalid choice!")