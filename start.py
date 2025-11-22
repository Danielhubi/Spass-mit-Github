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
    "Hallo nochmal, Welt! @PythonUser123"
]

# Eine Liste von Wörtern, die moderiert werden sollen
forbidden_words = ["SPAM", "Billig", "kaufen"]

#Teil 1

def analyze_post(post_text):
    # Länge des Posts
    post_length = len(post_text)

    # Prüfen, ob verdächtig
    is_suspicious = post_length < 10 or post_length > 80

    # Hashtag zählen
    hashtag_count = post_text.count("#")

    # Ergebnisse zurückgeben
    return (is_suspicious, post_length, hashtag_count)

print("Hallo Welt! #python", analyze_post("Hallo Welt! #python"))
print("Kurz", analyze_post("Kurz"))