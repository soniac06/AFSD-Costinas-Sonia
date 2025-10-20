sir="""   Victoria’s Secret a revenit pe podiumul din New York într-un spectacol spectaculos, plin de strălucire, energie și emoție. După ani de pauză și controverse, celebra casă de modă a reușit să aducă înapoi magia show-urilor sale, cu o combinație de nostalgie și diversitate modernă. Sub direcția creativă a designerului Adam Selman, ediția din 2025 a fost descrisă drept „amplă, puternică și jucăușă”. 
Show-ul a fost transmis în direct din New York și a adus înapoi pe podium o parte dintre cele mai mari nume din istoria brandului: Adriana Lima, Alessandra Ambrosio, Barbara Palvin, Behati Prinsloo, Joan Smalls, Doutzen Kroes, Candice Swanepoel și Liu Wen. Lor li s-au alăturat o nouă generație de „îngeri” și muzee moderne: Bella și Gigi Hadid, Ashley Graham, Anok Yai, Paloma Elsesser, Imaan Hammam și Alex Consani. 
Printre debutante s-au numărat actrița Barbie Ferreira, sportiva Angel Reese, gimnasta olimpică Suni Lee și modelul Emily Ratajkowski. Spectacolul a avut loc miercuri, 15 octombrie, în Brooklyn, și a inclus momente live cu TWICE, Karol G, Missy Elliott și Madison Beer. Potrivit People, a fost „o coliziune glorioasă de nostalgie și energie nouă”. Pe covorul roz, atmosfera a fost relaxată și plină de emoții."""
jumatate=len(sir)//2
prima_parte=sir[:jumatate]
a_doua_parte=sir[jumatate:]

prima_parte=prima_parte.upper()
prima_parte=prima_parte.strip()

a_doua_parte=a_doua_parte[::-1]
a_doua_parte=a_doua_parte.capitalize()
a_doua_parte=a_doua_parte.replace(".", "")
a_doua_parte=a_doua_parte.replace(",", "")
a_doua_parte=a_doua_parte.replace("!", "")
a_doua_parte=a_doua_parte.replace("?", "")

final=prima_parte+a_doua_parte
print(final)