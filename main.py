# import os
# import shutil

# example_dir = "Nümunə"
# os.makedirs(example_dir, exist_ok=True)

# subdirect_dir = os.path.join(example_dir, "altqovluq")
# os.makedirs(subdirect_dir, exist_ok=True)

# text_file_path = os.path.join(subdirect_dir, "nümunə.txt")

# with open(text_file_path, "w", encoding='utf-8') as f:
#     f.write("Bu bir nümunə mətn faylıdır.")

# current_directory = os.getcwd()
# image_file_name = "foto.jpg"
# image_file_path = os.path.join(current_directory, image_file_name)


# if os.path.exists(image_file_path):
#     shutil.copy(image_file_path, subdirect_dir)
# else:
#     print(f"Şəkil faylı '{image_file_name}' hal hazırda olduğunuz qovluqda mövcud deyil.")
# for file_name in os.listdir(subdirect_dir):
#     if file_name.endswith(".txt"):
#         destination_path = os.path.join(example_dir, file_name)
#         if os.path.exists(destination_path):
#             base, extension = os.path.splitext(file_name)
#             new_file_name = f"{base}_yeni{extension}"
#             destination_path = os.path.join(example_dir, new_file_name)
#         shutil.move(os.path.join(subdirect_dir, file_name), destination_path)

# example_contents = os.listdir(example_dir)
# subdirect_contents = os.listdir(subdirect_dir)

# print("Nümunə qovluğunun məzmunu:", example_contents)
# print("Altqovluq qovluğunun məzmunu:", subdirect_contents)




# def yer_tap(xallar):
#     # Xalları böyükdən kiçiyə doğru sırala və indekslərini al
#     sıralanmış_indeksler = sorted(range(len(xallar)), key=lambda k: xallar[k], reverse=True)
    
#     # Yerlər listini yarat
#     yerler = [None] * len(xallar)
#     for sıra, indeks in enumerate(sıralanmış_indeksler):
#         if sıra == 0:
#             yerler[indeks] = "1-ci"
#         elif sıra == 1:
#             yerler[indeks] = "2-ci"
#         elif sıra == 2:
#             yerler[indeks] = "3-cü"
#         else:
#             yerler[indeks] = f"{sıra+1}-ci"
    
#     return yerler

# # Test məlumatları
# xallar = [5, 3, 4, 2, 1]

# # Fonksiyonu çağırıb nəticəni çap et
# print(yer_tap(xallar))


