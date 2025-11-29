# Der "Feed" – eine Liste von Social-Media-Posts (als Strings)
# Jeder Post ist ein String in unserer Liste.
feed_data = [
    "Hallo Welt! Mein erstes Python-Projekt. #python #neu",
    "Ich liebe Listen! Listen sind so vielseitig. #python",
    "Was sind eigentlich Seiteneffekte? #frage",
    "SPAM! Kaufen Sie jetzt! Billig! SPAM!",
    "Sets sind super für einzigartige Elemente. #tipp",
    "Python ist nicht nur eine Schlange. @PythonUser123",
    "Wer hat Lust auf ein weiteres Projekt? #python",
    "Dieser Post ist nur Fülltext.",
    "SPAM! Nicht klicken! SPAM!",
    "Ich mag Tupel, weil sie unveränderlich sind.",
    "Hallo nochmal, Welt! @PythonUser123",
    "hallo"
]

# Eine Liste von Wörtern, die moderiert werden sollen
forbidden_words = ["SPAM", "Billig", "kaufen"]

#Teil 1

def analyze_post(post_text):
    # Länge des Posts
    post_length = len(post_text)

    # Prüfen ob verdächtig, wenn weniger als 10 und mehr als 80 zeichen
    is_suspicious = post_length < 10 or post_length > 80

    # Hashtag zählen
    hashtag_count = post_text.count("#")

    return (is_suspicious, post_length, hashtag_count)

print("Hallo Welt! #python", analyze_post("Hallo Welt! #python"))
print("Kurz", analyze_post("Kurz"))
print("SPAM! Kaufen Sie jetzt! Billig! SPAM!", analyze_post("SPAM! Kaufen Sie jetzt! Billig! SPAM!"))
print("Hallo Welt! Mein erstes Python-Projekt. #python #neu", analyze_post("Hallo Welt! Mein erstes Python-Projekt. #python #neu"))



# 1. Anlegen
valid_posts = []
suspicious_posts = []

# 2. Verarbeiten
for item in feed_data:
    analysis_result = analyze_post(item)        # Funktion aufrufen
    is_suspicious, length, hashtags = analysis_result  # Tupel entpacken

    # 3. Sortieren
    if is_suspicious:
        suspicious_posts.append(item)
    else:
        valid_posts.append(item)

print("Analyse abgeschlossen.")
print("Anzahl valider Posts:", len(valid_posts))
print("Anzahl verdächtiger Posts:", len(suspicious_posts))


unique_mentions = set()   # 1. Leeres Set

for post in valid_posts:  # 2. Durch valid_posts iterieren
    words = post.split()  # 3. Post in Wörter teilen

    for word in words:    # 4. Durch jedes Wort iterieren
        if word.startswith("@"):  # 5. Check: Mentions beginnen mit "@"
            
            # 6. Bereinigen: Satzzeichen entfernen (z.B. ",", "!")
            cleaned = word.strip(".,!?;:")

            unique_mentions.add(cleaned)

# 7. Ergebnis ausgeben
print("Einzigartige Mentions:", unique_mentions)


forbidden_set=set(forbidden_words)

def censor_feed(post_list, forbidden_set):
    for i in range(len(post_list)):        # Wir brauchen den Index
        post = post_list[i]                # Originalpost holen

        for word in forbidden_set:         # Durch verbotene Wörter iterieren
            post = post.replace(word, "***")

        post_list[i] = post

censor_feed(valid_posts, forbidden_set)

print("Zensierte valid_posts:")
for post in valid_posts:
    print(post)


while True:
    print("\n--- Social-Media-O-Mat 9000 ---")
    print("1: Neuen Post hinzufügen")
    print("2: Alle validen Posts anzeigen")
    print("3: Alle verdächtigen Posts anzeigen")
    print("4: Einzigartige Mentions anzeigen")
    print("q: Beenden")

    choice = input("Wähle eine Option: ")

 
    if choice == "q":
        print("Programm beendet. Auf Wiedersehen!")
        break

 
    elif choice == "1":
        new_post = input("Gib den neuen Post ein: ")

       
        is_suspicious, length, hashtags = analyze_post(new_post)

     
        if is_suspicious:
            suspicious_posts.append(new_post)
            print("Post wurde als VERDÄCHTIG gespeichert.")
        else:
            valid_posts.append(new_post)
            print("Post wurde als VALIDE gespeichert.")

   
    elif choice == "2":
        print("\n--- Valide Posts ---")
        if len(valid_posts) == 0:
            print("(Keine vorhanden)")
        else:
            for p in valid_posts:
                print("-", p)

    
    elif choice == "3":
        print("\n--- Verdächtige Posts ---")
        if len(suspicious_posts) == 0:
            print("(Keine vorhanden)")
        else:
            for p in suspicious_posts:
                print("-", p)


    elif choice == "4":
        print("\n--- Einzigartige Mentions ---")
        if len(unique_mentions) == 0:
            print("(Keine vorhanden)")
        else:
            for mention in unique_mentions:
                print("-", mention)

    else:
        print("Ungültige Eingabe. Bitte erneut versuchen.")