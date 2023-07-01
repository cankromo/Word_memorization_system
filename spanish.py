import random as r
from gtts import gTTS
import pygame, os

word_list = [
("La Palabra", "Kelime"),
("El Hambre", "Açlık"),
("El Olor", "Koku"),
("La Comida", "Yemek"),
("El Tiempo", "Zaman"),
("El Vestido", "Elbise"),
("La Casa", "Ev"),
("La Tierra", "Toprak"),
("El Mundo", "Dünya"),
("El Supermercado", "Market"),
("El Hombre", "Adam"),
("La Mujer", "Kadın"),
("La Imagen", "Görüntü"),
("La Luz", "Işık"),
("El Día", "Gün"),
("El Año", "Yıl"),
("El Nombre", "İsim"),
("El Movimiento", "Hareket"),
("La Persona", "Kişi"),
("El Número", "Sayı"),
("La Llamada", "Arama", "Çağrı"),
("La Página", "Sayfa"),
("El País", "Ülke"),
("La Respuesta", "Cevap"),
("Caliente", "Sıcak"),
("Grande", "Büyük"),
("Pequeño", "Küçük")
,("Todo", "Her şey", "Hepsi"),
("Primero", "Birinci","İlk"),
("Ahora", "Şimdi"),
("El Espejo", "Ayna"),
("La Puerta", "Kapı"),
("El Cristal", "Cam"),
("El Agua", "Su"),
("El Bosque", "Orman"),
("El Árbol", "Ağaç"),
("La Pregunta", "Soru"),
("La Escuela", "Okul"),
("La Planta", "Bitki"),
("El Alimento", "Gıda"),
("La Silla", "Sandalye"),
("La Guerra", "Savaş"),
("El reloj", "Saat"),
("La maceta", "Saksı"),
("Lunes", "Pazartesi"),
("Martes", "Salı"),
("Mıercoles", "Çarşamba"),
("Juvenes", "Perşembe"),
("Vıernes", "Cuma"),
("Sabado", "Cumartesi"),
("Domingo", "Pazar"),
("Mejor" ,"En iyi"),
("Sólo" ,"Sadece"),
("Solo:", "Tek başına" , "Yalnız"),
("El zapato", "Ayakkabı"),
("El sombrero", "Şapka"),
("El pantalón", "Pantolon"),
("yo", "Ben"),
("tú", "Sen"),
("él", "O(Erkek)"),
("ella", "O(Kadın)"),
("nosotros", "Biz(Erkek)"),
("nosotras", "Biz(Kadın)"),
("vosotros", "Siz(Erkek)"),
("vosotras", "Siz(Kadın)"),
("ellos", "Onlar(Erkek)"),
("ellas", "Onlar(Kadın)"),
("usted", "Siz"),
("ustedes", "Siz"),
("El libro", "Kitap"),
("El coche", "Araba"),
("La gafa", "Gözlük"),
("Lapiz", "Kalem"),
("La Luna", "Ay"),
("El Sol", "Güneş"),
("Duro", "Sert"),
("La Historia", "Tarih"),
("El / La Mar", "Deniz"),
("La Piscina", "Havuz"),
("La Cine", "Sinema"),
("El Periódico", "Gazete"),
("Tarde", "Geç"),
("Blando", "Yumuşak"),
("Hablar", "Konusmak"),
("Comer", "Yemek"),
("Vivir", "Yaşamak"),
("Estar (konum, duygu, durum icin)", "Olmak"),
("Ser", "Olmak"),
("Tener", "Sahip olmak"),
("Poner", "Koymak"),
("Tomar", "Almak"),
("Dar", "Vermek"),
("Ir", "Gitmek"),
("Decir", "Söylemek"),
("Hacer", "Yapmak"),
("Poder", "Bilmek"),
("Andar", "Yurumek"),
("Hoy", "Bugün")
,("Mañana", "Yarın"),
("Ayer", "Dün"),
("Ahora", "Şimdi"),
("Siempre", "Her zaman"),
("Nunca", "Hiç"),
("desde", "den beri"),
("de vez en cuando", "Ara sıra"),
("a veces", "Bazen"),
("Anoche ", "Dün gece"),
("ya", "Zaten"),
("Luego", "Sonra"),
("Todavía", "Hala"),
("También", "Ayrıca"),
("pronto", "Yakında"),
("inermediamente", "Hemen"),
("dormir", "Uyumak"),
("nececitar", "İhtiyacı olmak"),
("querer", "İstemek"),
("abrır", "Açmak"),
("cerrar", "Kapatmak"),
("comprar", "Satın almak"),
("Agarrar", "Tutmak"),
("caminar", "Yürümek"),
("beber", "İçmek"),
("buscar", "Aramak"),
("leer", "Okumak"),
("la escalaera", "Merdiven"),
("ızquierda", "Sol"),
("derecha", "Sağ"),
("el norte", "Kuzey"),
("el sur", "Güney"),
("la vida", "Hayat"),
("poco", "Az"),
("la habitación", "Oda"),
("el/la aspiradora", "Elektrik süpürgesi"),
("cienca", "Bilim"),
("rojo", "Kırmızı"),
("azul", "Mavi"),
("verde", "Yeşil"),
("amarillo", "Sarı"),
("blanco", "Beyaz"),
("negro", "Siyah"),
("naranja" , "turuncu"),
("marron", "kahverengi"),
("la cocina", "mutfak"),
("el dormitorio", "yatak odası"),
("el chico", "erkek"),
("La Chica", "kız"),
("La Hembra", "dişi"),
("El Color", "renk"),
("El Caro", "pahalı"),
("El Barato", "ucuz"),
("La Cara", "yüz"),
("La Madera", "tahta"),
("El Hierro", "demir")

]

true_known=0
false_known=0
first_len=len(word_list)

pygame.init()

#şapka,,orman,
for _ in range(len(word_list)):
    pygame.mixer.init()

    random_word = r.choice(word_list)
    word_list.remove(random_word)
    print(random_word[0])
    
    tts = gTTS(text=random_word[0], lang='es')

    tts.save('word.mp3')

    # Play the music
    pygame.mixer.music.load('word.mp3')
    pygame.mixer.music.play()

    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        
        pygame.time.Clock().tick(10)

    # Stop the music and release the file handle
    pygame.mixer.music.stop()

    pygame.mixer.music.fadeout(1000)
    pygame.mixer.quit()

    os.remove('word.mp3')



    a = input("Please enter a Turkish word: (/ for exit)")
    
    translations = [translation.lower() for translation in random_word[1:]]
    if a.lower() in translations:
        print("True")
        print("------------------")
        true_known += 1
        
    elif a==("/"):
        break
    else:
        print("False")
        print(random_word[1])
        print("Continue to other word")
        print("--------------------")
        false_known=false_known+1
pygame.quit()

"""
pygame.mixer.init()
for _ in range(len(word_list)):
    pygame.mixer.init()

    random_word = r.choice(word_list)
    word_list.remove(random_word)
    print(random_word[1])
    
    tts = gTTS(text=random_word[1], lang='tr')

    tts.save('word.mp3')

    # Play the music
    pygame.mixer.music.load('word.mp3')
    pygame.mixer.music.play()

    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        
        pygame.time.Clock().tick(10)

    # Stop the music and release the file handle
    pygame.mixer.music.stop()

    pygame.mixer.music.fadeout(1000)
    pygame.mixer.quit()

    os.remove('word.mp3')



    a = input("Please enter a Spanish: (/ for exit)")
    
    translations = [translation.lower() for translation in random_word[1:]]
    if a.lower() in translations:
        print("True")
        print("------------------")
        true_known += 1
        
    elif a==("/"):
        break
    else:
        print("False")
        print(random_word[0])
        print("Continue to other word")
        print("--------------------")
        false_known=false_known+1

pygame.quit()
"""
print(str(true_known) ,"/",str(true_known+false_known))